from enum import Enum

from infra.assemblers.command_assemblers.calibration_step_start_assembler import CalibrationStepStartAssembler
from infra.assemblers.command_assemblers.calibration_end_assembler import CalibrationEndAssembler
from infra.assemblers.command_assemblers.treatment_start_assembler import TreatmentStartAssembler
from infra.assemblers.command_assemblers.treatment_one_mind_send_assembler import TreatmentOneMindSendAssembler


class Commands(Enum):
    calibration_step_start = {"name": "calibration_step_start", "assembler": CalibrationStepStartAssembler()}
    calibration_end = {"name": "calibration_end", "assembler": CalibrationEndAssembler()}
    treatment_start = {"name": "treatment_start", "assembler": TreatmentStartAssembler()}
    treatment_one_min_send = {"name": "treatment_one_min_send", "assembler": TreatmentOneMindSendAssembler()}

    def __init__(self, value):
        if "name" not in value:
            raise ValueError("Key 'name' needs to be provided")
        if "assembler" not in value:
            raise ValueError("Key 'assembler' needs to be provided")

    @property
    def name(self):
        return self.value["name"]

    @property
    def assembler(self):
        return self.value["assembler"]

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)
