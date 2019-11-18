
FROM python:3.6-stretch

WORKDIR /AQI-AGENT

ADD . /AQI-AGENT

# install python library dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# set up env
ENV INFLUXDB_HOST=influxdb
CMD ["python", "./server.py"]