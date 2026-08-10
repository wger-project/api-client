from enum import Enum


class SetsConfigListOperation(str, Enum):
    R = "r"
    VALUE_0 = "+"
    VALUE_1 = "-"

    def __str__(self) -> str:
        return str(self.value)
