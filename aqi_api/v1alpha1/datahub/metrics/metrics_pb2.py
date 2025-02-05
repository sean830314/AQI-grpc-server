# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aqi_api/v1alpha1/datahub/metrics/metrics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aqi_api.v1alpha1.datahub.resources import metadata_pb2 as aqi__api_dot_v1alpha1_dot_datahub_dot_resources_dot_metadata__pb2
from aqi_api.v1alpha1.datahub.common import metrics_pb2 as aqi__api_dot_v1alpha1_dot_datahub_dot_common_dot_metrics__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='aqi_api/v1alpha1/datahub/metrics/metrics.proto',
  package='ekko771.aqi.v1alpha1.datahub.metrics',
  syntax='proto3',
  serialized_options=_b('ZCgithub.com/ekko771/AQI-grpc-server/aqi_api/v1alpha1/datahub/metrics'),
  serialized_pb=_b('\n.aqi_api/v1alpha1/datahub/metrics/metrics.proto\x12$ekko771.aqi.v1alpha1.datahub.metrics\x1a\x31\x61qi_api/v1alpha1/datahub/resources/metadata.proto\x1a-aqi_api/v1alpha1/datahub/common/metrics.proto\"\x8d\x01\n\tAQIMetric\x12\x43\n\x08metadata\x18\x01 \x01(\x0b\x32\x31.ekko771.aqi.v1alpha1.datahub.metadata.ObjectMeta\x12;\n\x06sample\x18\x02 \x01(\x0b\x32+.ekko771.aqi.v1alpha1.datahub.common.SampleBEZCgithub.com/ekko771/AQI-grpc-server/aqi_api/v1alpha1/datahub/metricsb\x06proto3')
  ,
  dependencies=[aqi__api_dot_v1alpha1_dot_datahub_dot_resources_dot_metadata__pb2.DESCRIPTOR,aqi__api_dot_v1alpha1_dot_datahub_dot_common_dot_metrics__pb2.DESCRIPTOR,])




_AQIMETRIC = _descriptor.Descriptor(
  name='AQIMetric',
  full_name='ekko771.aqi.v1alpha1.datahub.metrics.AQIMetric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ekko771.aqi.v1alpha1.datahub.metrics.AQIMetric.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sample', full_name='ekko771.aqi.v1alpha1.datahub.metrics.AQIMetric.sample', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=328,
)

_AQIMETRIC.fields_by_name['metadata'].message_type = aqi__api_dot_v1alpha1_dot_datahub_dot_resources_dot_metadata__pb2._OBJECTMETA
_AQIMETRIC.fields_by_name['sample'].message_type = aqi__api_dot_v1alpha1_dot_datahub_dot_common_dot_metrics__pb2._SAMPLE
DESCRIPTOR.message_types_by_name['AQIMetric'] = _AQIMETRIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AQIMetric = _reflection.GeneratedProtocolMessageType('AQIMetric', (_message.Message,), {
  'DESCRIPTOR' : _AQIMETRIC,
  '__module__' : 'aqi_api.v1alpha1.datahub.metrics.metrics_pb2'
  # @@protoc_insertion_point(class_scope:ekko771.aqi.v1alpha1.datahub.metrics.AQIMetric)
  })
_sym_db.RegisterMessage(AQIMetric)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
