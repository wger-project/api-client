from typing import Literal

RirConfigListStep = Literal["abs", "na", "percent"]

RIR_CONFIG_LIST_STEP_VALUES: set[RirConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_rir_config_list_step(value: str) -> RirConfigListStep:
    if value in RIR_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RIR_CONFIG_LIST_STEP_VALUES!r}"
    )
