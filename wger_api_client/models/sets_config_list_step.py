from typing import Literal

SetsConfigListStep = Literal["abs", "na", "percent"]

SETS_CONFIG_LIST_STEP_VALUES: set[SetsConfigListStep] = {
    "abs",
    "na",
    "percent",
}


def check_sets_config_list_step(value: str) -> SetsConfigListStep:
    if value in SETS_CONFIG_LIST_STEP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SETS_CONFIG_LIST_STEP_VALUES!r}"
    )
