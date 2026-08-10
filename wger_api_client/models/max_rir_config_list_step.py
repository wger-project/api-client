from enum import Enum


class MaxRirConfigListStep(str, Enum):
    ABS = "abs"
    NA = "na"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
