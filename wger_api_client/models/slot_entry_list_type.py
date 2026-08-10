from enum import Enum


class SlotEntryListType(str, Enum):
    DROPSET = "dropset"
    FORCED = "forced"
    ISO = "iso"
    JUMP = "jump"
    MYO = "myo"
    NORMAL = "normal"
    PARTIAL = "partial"
    TUT = "tut"
    WARMUP = "warmup"

    def __str__(self) -> str:
        return str(self.value)
