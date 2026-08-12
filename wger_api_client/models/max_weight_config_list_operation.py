from typing import Literal

MaxWeightConfigListOperation = Literal["+", "-", "r"]

MAX_WEIGHT_CONFIG_LIST_OPERATION_VALUES: set[MaxWeightConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_max_weight_config_list_operation(value: str) -> MaxWeightConfigListOperation:
    if value in MAX_WEIGHT_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_WEIGHT_CONFIG_LIST_OPERATION_VALUES!r}"
    )
