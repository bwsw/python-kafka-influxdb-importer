FROM ubuntu:16.04

MAINTAINER Bitworks Software info@bitworks.software

ENV INFLUX_HOST influxhost.com
ENV INFLUX_PORT 8086
ENV INFLUX_DB puls
ENV INFLUX_USER puls
ENV INFLUX_PASSWORD secret

ENV KAFKA_BOOTSTRAP localhost:9092
ENV KAFKA_TOPIC kvm-metrics
ENV KAFKA_GROUP group

ENV PAUSE 20
ENV GATHER_HOST_STATS true
ENV DEBUG true

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-pip
RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install influxdb

COPY ./src /opt

WORKDIR /opt

CMD ["/bin/bash", "/opt/import-data"]


