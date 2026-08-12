from typing import Literal

WeightUnitEnum = Literal["kg", "lb"]

WEIGHT_UNIT_ENUM_VALUES: set[WeightUnitEnum] = {
    "kg",
    "lb",
}


def check_weight_unit_enum(value: str) -> WeightUnitEnum:
    if value in WEIGHT_UNIT_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEIGHT_UNIT_ENUM_VALUES!r}"
    )
