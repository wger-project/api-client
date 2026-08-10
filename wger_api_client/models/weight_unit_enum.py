from enum import Enum


class WeightUnitEnum(str, Enum):
    KG = "kg"
    LB = "lb"

    def __str__(self) -> str:
        return str(self.value)
