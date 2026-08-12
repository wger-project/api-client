from typing import Literal

BlankEnum = Literal[""]

BLANK_ENUM_VALUES: set[BlankEnum] = {
    "",
}


def check_blank_enum(value: str) -> BlankEnum:
    if value in BLANK_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLANK_ENUM_VALUES!r}"
    )
