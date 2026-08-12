from typing import Literal

ImpressionEnum = Literal["1", "2", "3"]

IMPRESSION_ENUM_VALUES: set[ImpressionEnum] = {
    "1",
    "2",
    "3",
}


def check_impression_enum(value: str) -> ImpressionEnum:
    if value in IMPRESSION_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IMPRESSION_ENUM_VALUES!r}"
    )
