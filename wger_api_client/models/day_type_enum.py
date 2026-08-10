from enum import Enum


class DayTypeEnum(str, Enum):
    AFAP = "afap"
    AMRAP = "amrap"
    CUSTOM = "custom"
    EDT = "edt"
    ENOM = "enom"
    HIIT = "hiit"
    RFT = "rft"
    TABATA = "tabata"

    def __str__(self) -> str:
        return str(self.value)
