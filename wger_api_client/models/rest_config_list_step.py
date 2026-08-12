from typing import Literal

RestConfigListStep = Literal["abs", "na", "percent"]

REST_CONFIG_LIST_STEP_VALUES: set[RestConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_rest_config_list_step(value: str) -> RestConfigListStep:
    if value in REST_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REST_CONFIG_LIST_STEP_VALUES!r}"
    )
