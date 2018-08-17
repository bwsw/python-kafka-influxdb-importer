#!/usr/bin/python
# -*- coding: UTF-8 -*-


from kafka import KafkaConsumer
from kafka.errors import KafkaError
from influxdb import InfluxDBClient

import json
import os

kafkaBootstrapHosts = os.environ["KAFKA_BOOTSTRAP"]
kafkaTopic = os.environ["KAFKA_TOPIC"]
kafkaGroup = os.environ["KAFKA_GROUP"]

influxHost = os.environ["INFLUX_HOST"]
influxPort = int(os.environ["INFLUX_PORT"])
influxDB = os.environ["INFLUX_DB"]
influxUser = os.environ["INFLUX_USER"]
influxPassword = os.environ["INFLUX_PASSWORD"]

debug=os.environ["DEBUG"]

influxClient = InfluxDBClient(influxHost, influxPort, influxUser, influxPassword, influxDB)

consumer = KafkaConsumer(kafkaTopic,
                         group_id = kafkaGroup,
                         bootstrap_servers = kafkaBootstrapHosts.split(","),
                         value_deserializer = lambda m: json.loads(m.decode('ascii')))

for message in consumer:
    if debug == "true":
	print json.dumps(message.value)
    influxClient.write_points(message.value)
