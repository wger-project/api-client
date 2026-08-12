from typing import Literal

MaxSetsConfigListStep = Literal["abs", "na", "percent"]

MAX_SETS_CONFIG_LIST_STEP_VALUES: set[MaxSetsConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_max_sets_config_list_step(value: str) -> MaxSetsConfigListStep:
    if value in MAX_SETS_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_SETS_CONFIG_LIST_STEP_VALUES!r}"
    )
