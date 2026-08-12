from typing import Literal

UnitTypeEnum = Literal["DISTANCE", "REPETITIONS", "TIME"]

UNIT_TYPE_ENUM_VALUES: set[UnitTypeEnum] = {
    "DISTANCE",
    "REPETITIONS",
    "TIME",
}


def check_unit_type_enum(value: str) -> UnitTypeEnum:
    if value in UNIT_TYPE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UNIT_TYPE_ENUM_VALUES!r}"
    )
