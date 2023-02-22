import logging

from django.contrib.auth import get_user_model

from infra.assemblers.kafka_assembler import KafkaAssembler
from infra.models import Session, SessionTypes, StatusChoices
from infra.domain.alert.calibration_alert import CalibrationStartAlert
from infra.domain.sensor_commands import SensorCommands


from infra.domain.alert.alert import Alert
from infra.domain.session_type import SessionType

logger = logging.getLogger(__name__)

"""
Command Name: Calibration_Start
Command Received From: User Interface  
Command Purpose: Calibration phase is to be started when this command is received from the user interface. 
                 The User Interface application will send the command to Kafka topic: IPC topic
                 A new Calibration Session is created for the user and the SESSION ID is sent to the sensors. (produced to IPC topic) 
                 The message to send the SESSION ID is a generic message. Along with the SESSION ID, session type is also sent to the sensors. 
                 Sensors store the SESSION ID in their ENV until a new session ID is sent.  
"""


class CalibrationStartAssembler:
    def assemble(self, command_data: dict) -> Alert:
        logger.info(f"Received Calibration Start command.")

        if "user" not in command_data:
            logger.info("Calibration Start: User data not found in the message received from the user interface.")
            return False

        # Get the user who has triggered calibration start command
        user_id = command_data.get("user")

        # Create a calibration session to be set in all the sensors' ENV
        session = self._create_session(user_id)

        # Produce the session to sensors.
        alert = CalibrationStartAlert(command=SensorCommands.set_calibration_start.name,
                                      session=str(session.pk),
                                      session_type=SessionType.CALIBRATION.name.lower(),
                                      # devices=command_data.get("devices")
                                      )
        return alert

    def _create_session(self, user_id):
        user = get_user_model().objects.get(pk=user_id)
        session = Session(user=user, type=SessionTypes.CALIBRATION, status=StatusChoices.STARTED)
        session.save()
        return session
