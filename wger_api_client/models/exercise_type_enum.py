from typing import Literal

ExerciseTypeEnum = Literal[
    "dropset", "forced", "iso", "jump", "myo", "normal", "partial", "tut", "warmup"
]

EXERCISE_TYPE_ENUM_VALUES: set[ExerciseTypeEnum] = {
    "dropset",
    "forced",
    "iso",
    "jump",
    "myo",
    "normal",
    "partial",
    "tut",
    "warmup",
}


def check_exercise_type_enum(value: str) -> ExerciseTypeEnum:
    if value in EXERCISE_TYPE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXERCISE_TYPE_ENUM_VALUES!r}"
    )
