import logging

from infra.assemblers.kafka_assembler import KafkaAssembler
from infra.domain.command_process import CommandProcess
from infra.exceptions.filter_out import FilterOutException
from infra.models import Session

logger = logging.getLogger(__name__)


class TreatmentStartAssembler(KafkaAssembler):
    def assemble(self, command_data: dict) -> CommandProcess:
        logger.info(f"Received Treatment Start command.")

        try:
            session_id = command_data.get("session")
            session = Session.objects.get(id=session_id)


        except Exception as e:
            raise FilterOutException(__name__, e)
