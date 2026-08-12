from typing import Literal

IntensityEnum = Literal["1", "2", "3"]

INTENSITY_ENUM_VALUES: set[IntensityEnum] = {
    "1",
    "2",
    "3",
}


def check_intensity_enum(value: str) -> IntensityEnum:
    if value in INTENSITY_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INTENSITY_ENUM_VALUES!r}"
    )
