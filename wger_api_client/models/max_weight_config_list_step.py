from typing import Literal

MaxWeightConfigListStep = Literal["abs", "na", "percent"]

MAX_WEIGHT_CONFIG_LIST_STEP_VALUES: set[MaxWeightConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_max_weight_config_list_step(value: str) -> MaxWeightConfigListStep:
    if value in MAX_WEIGHT_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_WEIGHT_CONFIG_LIST_STEP_VALUES!r}"
    )
