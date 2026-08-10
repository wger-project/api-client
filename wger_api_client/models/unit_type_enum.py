from enum import Enum


class UnitTypeEnum(str, Enum):
    DISTANCE = "DISTANCE"
    REPETITIONS = "REPETITIONS"
    TIME = "TIME"

    def __str__(self) -> str:
        return str(self.value)
