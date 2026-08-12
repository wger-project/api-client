from typing import Literal

WeightConfigListStep = Literal["abs", "na", "percent"]

WEIGHT_CONFIG_LIST_STEP_VALUES: set[WeightConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_weight_config_list_step(value: str) -> WeightConfigListStep:
    if value in WEIGHT_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEIGHT_CONFIG_LIST_STEP_VALUES!r}"
    )
