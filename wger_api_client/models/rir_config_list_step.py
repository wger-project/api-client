from enum import Enum


class RirConfigListStep(str, Enum):
    ABS = "abs"
    NA = "na"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
