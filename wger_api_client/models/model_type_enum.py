from enum import Enum


class ModelTypeEnum(str, Enum):
    BASE = "base"
    IMAGE = "image"
    TRANSLATION = "translation"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
