from typing import Literal

NutriscoreEnum = Literal["a", "b", "c", "d", "e"]

NUTRISCORE_ENUM_VALUES: set[NutriscoreEnum] = {
    "a",
    "b",
    "c",
    "d",
    "e",
}


def check_nutriscore_enum(value: str) -> NutriscoreEnum:
    if value in NUTRISCORE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUTRISCORE_ENUM_VALUES!r}"
    )
