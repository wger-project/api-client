from typing import Literal

MaxSetsConfigListOperation = Literal["+", "-", "r"]

MAX_SETS_CONFIG_LIST_OPERATION_VALUES: set[MaxSetsConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_max_sets_config_list_operation(value: str) -> MaxSetsConfigListOperation:
    if value in MAX_SETS_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_SETS_CONFIG_LIST_OPERATION_VALUES!r}"
    )
