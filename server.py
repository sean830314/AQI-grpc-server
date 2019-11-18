from concurrent import futures
import time
from aqi_api.v1alpha1.datahub import server_pb2_grpc
from aqi_api.v1alpha1.datahub.metrics.service_pb2 import ListAQIMetricRequest, ListAQIMetricResponse
from aqi_api.v1alpha1.datahub.common.metrics_pb2 import Sample
from aqi_api.v1alpha1.datahub.resources.metadata_pb2 import ObjectMeta
from aqi_api.v1alpha1.datahub.metrics.metrics_pb2 import AQIMetric
import grpc
import os
import yaml
import argparse
from influxdb import InfluxDBClient


class AQIServicer(server_pb2_grpc.AQIServiceServicer):
    def __init__(self, client, dbname, measurement):
        self._client = client
        self._dbname = dbname
        self._measurement = measurement

    def covert_result_into_ListAQIMetricResponse(self, result):
        aqi_list = list(result.get_points(measurement=self._measurement))
        aqi_metrics = []
        for v in aqi_list:
            sample = Sample(aqi=v['AQI'], co=v['CO'], co_8hr=v['CO_8hr'], no=v['NO'], no2=v['NO2'], nox=v['NOx'], o3=v['O3'],
                            o3_8hr=v['O3_8hr'], pm10=v['PM10'], pm10_avg=v['PM10_AVG'], pm25=v['PM2.5'], pm25_avg=v['PM2.5_AVG'],
                            so2=v['SO2'], so2_avg=v['SO2_AVG'], wind_direc=v['WindDirec'], wind_speed=v['WindSpeed'], time=v['time']
                            )
            objectmeta = ObjectMeta(County=v['County'], Latitude=v['Latitude'], Longitude=v['Longitude'], Pollutant=v['Pollutant'],
                                    SiteId=v['SiteId'], SiteName=v['SiteName'], Status=v['Status'],
                                    )
            aqi_metrics.append(AQIMetric(sample=sample, metadata=objectmeta))
        return ListAQIMetricResponse(aqi_metrics=aqi_metrics)

    def ListAQIMetrics(self, request, context):
        self._client.switch_database(self._dbname)
        query_where = 'select * from {}'.format(self._measurement)
        bind_params = []
        print(request.metadata[0].County)
        if request.metadata[0].County != "":
            bind_params = {'County': request.metadata[0].County}
            query_where = '{} where County=$County;'.format(query_where)
        elif request.metadata[0].SiteName != "":
            bind_params = {'SiteName': request.metadata[0].SiteName}
            query_where = '{} where SiteName=$SiteName;'.format(query_where)
        print("Querying data: " + query_where)
        result = self._client.query(query_where, bind_params=bind_params)
        response = self.covert_result_into_ListAQIMetricResponse(result)
        """
        # test code
        aqi_metrics = []
        sample = Sample(aqi="5", pm25="7")
        aqi_metric = AQIMetric(sample=sample)
        aqi_metrics.append(aqi_metric)
        sample = Sample(aqi="6", pm25="78")
        aqi_metric = AQIMetric(sample=sample)
        aqi_metrics.append(aqi_metric)
        response = ListAQIMetricResponse(aqi_metrics=aqi_metrics)
        """
        return response


def serve(args):
    config_file = os.path.join(os.getcwd(), args.config)
    with open(config_file) as file_:
        config = yaml.safe_load(file_)
    influx_config = config['influx_setting']
    dbname = influx_config['dbname']
    measurement = influx_config['measurement']
    if os.getenv("INFLUXDB_HOST"):
        influx_config['host'] = os.getenv("INFLUXDB_HOST")
    client = InfluxDBClient(influx_config['host'], influx_config['port'], influx_config['user'], influx_config['password'], dbname)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    server_pb2_grpc.add_AQIServiceServicer_to_server(AQIServicer(client, dbname, measurement), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


def parse_args():
    """Parse the args from main."""
    parser = argparse.ArgumentParser(description='example code to play with InfluxDB')
    parser.add_argument('--config', type=str, required=False, default='config/config.yaml', help='config file location')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    serve(args)