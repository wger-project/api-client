from typing import Literal

MaxRirConfigListStep = Literal["abs", "na", "percent"]

MAX_RIR_CONFIG_LIST_STEP_VALUES: set[MaxRirConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_max_rir_config_list_step(value: str) -> MaxRirConfigListStep:
    if value in MAX_RIR_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_RIR_CONFIG_LIST_STEP_VALUES!r}"
    )
