# client.py

import grpc
from aqi_api.v1alpha1.datahub import server_pb2_grpc
from aqi_api.v1alpha1.datahub.metrics.service_pb2 import ListAQIMetricRequest, ListAQIMetricResponse
from aqi_api.v1alpha1.datahub.resources.metadata_pb2 import ObjectMeta
from google.protobuf.json_format import MessageToDict
import json
import argparse
def parse_args():
    """Parse the args from main."""
    parser = argparse.ArgumentParser(description='example code to play with InfluxDB')
    parser.add_argument('--County', type=str, required=False, default='', help='query condition with county')
    parser.add_argument('--SiteName', type=str, required=False, default='', help='query condition with SiteName')
    return parser.parse_args()
args = parse_args()
channel = grpc.insecure_channel('localhost:50051')

stub = server_pb2_grpc.AQIServiceStub(channel)

obj_list = [ObjectMeta(County=args.County, SiteName=args.SiteName)]
request = ListAQIMetricRequest(metadata=obj_list)

response = stub.ListAQIMetrics(request)
response_list = []
for v in response.aqi_metrics:
    metadata_dic = MessageToDict(v.metadata)
    sample_dic = MessageToDict(v.sample)
    response_list.append({**metadata_dic, **sample_dic})
print(response_list)
print(len(response.aqi_metrics))
response = {'Response': response_list[:1]}

with open('response.json', 'w') as file:
    file.write(json.dumps(response))