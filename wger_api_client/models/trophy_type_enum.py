from typing import Literal

TrophyTypeEnum = Literal["count", "date", "other", "pr", "sequence", "time", "volume"]

TROPHY_TYPE_ENUM_VALUES: set[TrophyTypeEnum] = {
    "count",
    "date",
    "other",
    "pr",
    "sequence",
    "time",
    "volume",
}


def check_trophy_type_enum(value: str) -> TrophyTypeEnum:
    if value in TROPHY_TYPE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TROPHY_TYPE_ENUM_VALUES!r}"
    )
