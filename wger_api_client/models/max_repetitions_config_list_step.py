from typing import Literal

MaxRepetitionsConfigListStep = Literal["abs", "na", "percent"]

MAX_REPETITIONS_CONFIG_LIST_STEP_VALUES: set[MaxRepetitionsConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_max_repetitions_config_list_step(value: str) -> MaxRepetitionsConfigListStep:
    if value in MAX_REPETITIONS_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_REPETITIONS_CONFIG_LIST_STEP_VALUES!r}"
    )
