from enum import Enum


class MaxWeightConfigListStep(str, Enum):
    ABS = "abs"
    NA = "na"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
