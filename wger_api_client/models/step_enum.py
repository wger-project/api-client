from typing import Literal

StepEnum = Literal["abs", "na", "percent"]

STEP_ENUM_VALUES: set[StepEnum] = {
    "abs",
    "na",
    "percent",
}


def check_step_enum(value: str) -> StepEnum:
    if value in STEP_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STEP_ENUM_VALUES!r}")
