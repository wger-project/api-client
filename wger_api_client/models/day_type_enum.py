from typing import Literal

DayTypeEnum = Literal["afap", "amrap", "custom", "edt", "enom", "hiit", "rft", "tabata"]

DAY_TYPE_ENUM_VALUES: set[DayTypeEnum] = {
    "afap",
    "amrap",
    "custom",
    "edt",
    "enom",
    "hiit",
    "rft",
    "tabata",
}


def check_day_type_enum(value: str) -> DayTypeEnum:
    if value in DAY_TYPE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DAY_TYPE_ENUM_VALUES!r}"
    )
