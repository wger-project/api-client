from typing import Literal

MaxRirConfigListOperation = Literal["+", "-", "r"]

MAX_RIR_CONFIG_LIST_OPERATION_VALUES: set[MaxRirConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_max_rir_config_list_operation(value: str) -> MaxRirConfigListOperation:
    if value in MAX_RIR_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_RIR_CONFIG_LIST_OPERATION_VALUES!r}"
    )
