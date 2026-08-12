from typing import Literal

RestConfigListOperation = Literal["+", "-", "r"]

REST_CONFIG_LIST_OPERATION_VALUES: set[RestConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_rest_config_list_operation(value: str) -> RestConfigListOperation:
    if value in REST_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REST_CONFIG_LIST_OPERATION_VALUES!r}"
    )
