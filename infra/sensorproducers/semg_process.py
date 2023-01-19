from kafka.consumer import Consumer
from smartback.configuration import get_config
import argparse
import os

"""
==================
Commands Received
==================
1. set_session_alert: Set the session ID to the ENV or globally to be sent in the data payloads.
2. set_calibration_start: Start sending data for the calibration phase, step ID will be provided
"""


def accept_record():
    """
    Listen for alerts with the possible commands:
     1. set_session_alert
     2. set_calibration_start
    :return:
    """
    pass


def create_consumer(configuration, topic):
    return Consumer(
        configuration.get_kafka_consumer_configuration(),
        topic,
        callback_function=accept_record
    )


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "--environment", "-e", default="testing", help="environment where the app will run."
    )
    args = argument_parser.parse_args()

    environment = args.environment
    configuration = get_config(environment)
    semg_consumer = create_consumer(configuration, configuration.get_kafka_semg_sensor_topic())
    semg_consumer.start()
