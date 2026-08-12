from typing import Literal

SetsConfigListOperation = Literal["+", "-", "r"]

SETS_CONFIG_LIST_OPERATION_VALUES: set[SetsConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_sets_config_list_operation(value: str) -> SetsConfigListOperation:
    if value in SETS_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SETS_CONFIG_LIST_OPERATION_VALUES!r}"
    )
