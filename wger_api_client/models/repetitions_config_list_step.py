from typing import Literal

RepetitionsConfigListStep = Literal["abs", "na", "percent"]

REPETITIONS_CONFIG_LIST_STEP_VALUES: set[RepetitionsConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_repetitions_config_list_step(value: str) -> RepetitionsConfigListStep:
    if value in REPETITIONS_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPETITIONS_CONFIG_LIST_STEP_VALUES!r}"
    )
