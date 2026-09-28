from typing import Literal

DynamicTypeEnum = Literal["BMI", "NONE", "ONE_REP_MAX", "ONE_RM_TOTAL", "WHTR"]

DYNAMIC_TYPE_ENUM_VALUES: set[DynamicTypeEnum] = {
    "BMI",
    "NONE",
    "ONE_REP_MAX",
    "ONE_RM_TOTAL",
    "WHTR",
}


def check_dynamic_type_enum(value: str) -> DynamicTypeEnum:
    if value in DYNAMIC_TYPE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DYNAMIC_TYPE_ENUM_VALUES!r}"
    )
