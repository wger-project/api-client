from typing import Literal

SourceEnum = Literal["apple", "calculated", "google", "user"]

SOURCE_ENUM_VALUES: set[SourceEnum] = {
    "apple",
    "calculated",
    "google",
    "user",
}


def check_source_enum(value: str) -> SourceEnum:
    if value in SOURCE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SOURCE_ENUM_VALUES!r}"
    )
