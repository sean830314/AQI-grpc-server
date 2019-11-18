from setuptools import setup


version = '0.1'

INSTALL_REQUIRES = (
    'protobuf>=3.9.0',
    'grpcio>=1.22.0',
    'grpcio-tools>=1.22.0',
    'googleapis-common-protos>=1.6.0',
)

setup(name='aqi-api',
      version=version,
      description='AQI API interfaces',
      long_description_content_type="text/markdown",
      author='ekko771',
      author_email='ekko771@gmail.com',
      urls='https://github.com/ekko771/AQI-grpc-server.git',
      packages=[
          'aqi_api.v1alpha1.datahub.common',
          'aqi_api.v1alpha1.datahub.metrics',
          'aqi_api.v1alpha1.datahub.resources',
          'aqi_api.v1alpha1.datahub',
      ],
      package_dir={
          'aqi_api.v1alpha1.datahub.common': 'aqi_api/v1alpha1/datahub/common',
          'aqi_api.v1alpha1.datahub.metrics': 'aqi_api/v1alpha1/datahub/metrics',
          'aqi_api.v1alpha1.datahub.resources': 'aqi_api/v1alpha1/datahub/resources',
          'aqi_api.v1alpha1.datahub': 'aqi_api/v1alpha1/datahub',
      },
      install_requires=INSTALL_REQUIRES,
      zip_safe=False)
