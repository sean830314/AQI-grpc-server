# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from aqi_api.v1alpha1.datahub.metrics import service_pb2 as aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2


class AQIServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListAQIMetrics = channel.unary_unary(
        '/ekko771.aqi.v1alpha1.datahub.AQIService/ListAQIMetrics',
        request_serializer=aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2.ListAQIMetricRequest.SerializeToString,
        response_deserializer=aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2.ListAQIMetricResponse.FromString,
        )


class AQIServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListAQIMetrics(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AQIServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListAQIMetrics': grpc.unary_unary_rpc_method_handler(
          servicer.ListAQIMetrics,
          request_deserializer=aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2.ListAQIMetricRequest.FromString,
          response_serializer=aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2.ListAQIMetricResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ekko771.aqi.v1alpha1.datahub.AQIService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
