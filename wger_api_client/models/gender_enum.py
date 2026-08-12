from typing import Literal

GenderEnum = Literal["1", "2"]

GENDER_ENUM_VALUES: set[GenderEnum] = {
    "1",
    "2",
}


def check_gender_enum(value: str) -> GenderEnum:
    if value in GENDER_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GENDER_ENUM_VALUES!r}"
    )
