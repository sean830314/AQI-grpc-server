# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aqi_api/v1alpha1/datahub/server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aqi_api.v1alpha1.datahub.metrics import service_pb2 as aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aqi_api/v1alpha1/datahub/server.proto',
  package='ekko771.aqi.v1alpha1.datahub',
  syntax='proto3',
  serialized_options=_b('Z;github.com/ekko771/AQI-grpc-server/aqi_api/v1alpha1/datahub'),
  serialized_pb=_b('\n%aqi_api/v1alpha1/datahub/server.proto\x12\x1c\x65kko771.aqi.v1alpha1.datahub\x1a.aqi_api/v1alpha1/datahub/metrics/service.proto2\x9a\x01\n\nAQIService\x12\x8b\x01\n\x0eListAQIMetrics\x12:.ekko771.aqi.v1alpha1.datahub.metrics.ListAQIMetricRequest\x1a;.ekko771.aqi.v1alpha1.datahub.metrics.ListAQIMetricResponse\"\x00\x42=Z;github.com/ekko771/AQI-grpc-server/aqi_api/v1alpha1/datahubb\x06proto3')
  ,
  dependencies=[aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_AQISERVICE = _descriptor.ServiceDescriptor(
  name='AQIService',
  full_name='ekko771.aqi.v1alpha1.datahub.AQIService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=120,
  serialized_end=274,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListAQIMetrics',
    full_name='ekko771.aqi.v1alpha1.datahub.AQIService.ListAQIMetrics',
    index=0,
    containing_service=None,
    input_type=aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2._LISTAQIMETRICREQUEST,
    output_type=aqi__api_dot_v1alpha1_dot_datahub_dot_metrics_dot_service__pb2._LISTAQIMETRICRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AQISERVICE)

DESCRIPTOR.services_by_name['AQIService'] = _AQISERVICE

# @@protoc_insertion_point(module_scope)
