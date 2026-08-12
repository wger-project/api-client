from typing import Literal

StyleEnum = Literal["1", "2", "3", "4", "5"]

STYLE_ENUM_VALUES: set[StyleEnum] = {
    "1",
    "2",
    "3",
    "4",
    "5",
}


def check_style_enum(value: str) -> StyleEnum:
    if value in STYLE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STYLE_ENUM_VALUES!r}"
    )
