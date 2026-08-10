from enum import Enum


class TrophyListTrophyType(str, Enum):
    COUNT = "count"
    DATE = "date"
    OTHER = "other"
    PR = "pr"
    SEQUENCE = "sequence"
    TIME = "time"
    VOLUME = "volume"

    def __str__(self) -> str:
        return str(self.value)
