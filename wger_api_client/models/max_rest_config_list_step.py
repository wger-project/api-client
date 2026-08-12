from typing import Literal

MaxRestConfigListStep = Literal["abs", "na", "percent"]

MAX_REST_CONFIG_LIST_STEP_VALUES: set[MaxRestConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_max_rest_config_list_step(value: str) -> MaxRestConfigListStep:
    if value in MAX_REST_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_REST_CONFIG_LIST_STEP_VALUES!r}"
    )
