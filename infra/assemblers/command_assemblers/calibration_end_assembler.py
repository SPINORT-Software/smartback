import logging

from infra.assemblers.kafka_assembler import KafkaAssembler
from infra.domain.alert.alert import Alert
from infra.domain.alert.calibration_alert import CalibrationEndAlert
from infra.exceptions.filter_out import FilterOutException
from infra.models import *
from infra.domain.sensor_commands import SensorCommands
from infra.assemblers.command_assemblers.calibration.calibration_end_data_processor import CalibrationEndDataProcessor

logger = logging.getLogger(__name__)

"""
Command Name: Calibration_end
Command Received From: User Interface  
Command Purpose: Calibration phase is ended when this command is received from the user interface. 
                 The User Interface application will send the command to Kafka topic: IPC
                 The current Calibration Session is set to COMPLETED 
                 Clear_Session command is sent to the Sensors to clear the session ID from the sensor devices.   
"""


class CalibrationEndAssembler(KafkaAssembler):
    # TODO: Update command_data to ConsumerRecord type
    def assemble(self, command_data: dict) -> Alert:
        """
        :param command_data:
        :return:
        """
        logger.info(f"Received Calibration End command.")

        try:
            session_id = command_data.get("session")
            session = Session.objects.get(id=session_id)

            procedure_name = command_data.get("procedure")
            procedure = Procedure.objects.get(name=procedure_name)

            data_processor = CalibrationEndDataProcessor(session)
            data_processor.process_user_calibration_session_data(session, procedure)

            # Send calibration_stop command to user's sensors to stop the data sending process
            return CalibrationEndAlert(command=SensorCommands.set_calibration_end.name, session=session_id)
        except Exception as e:
            raise FilterOutException(__name__, e)
