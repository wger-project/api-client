from typing import Literal

WeightConfigListOperation = Literal["+", "-", "r"]

WEIGHT_CONFIG_LIST_OPERATION_VALUES: set[WeightConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_weight_config_list_operation(value: str) -> WeightConfigListOperation:
    if value in WEIGHT_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEIGHT_CONFIG_LIST_OPERATION_VALUES!r}"
    )
