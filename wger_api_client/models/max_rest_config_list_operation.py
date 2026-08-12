from typing import Literal

MaxRestConfigListOperation = Literal["+", "-", "r"]

MAX_REST_CONFIG_LIST_OPERATION_VALUES: set[MaxRestConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_max_rest_config_list_operation(value: str) -> MaxRestConfigListOperation:
    if value in MAX_REST_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_REST_CONFIG_LIST_OPERATION_VALUES!r}"
    )
