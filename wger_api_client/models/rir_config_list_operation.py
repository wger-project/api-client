from typing import Literal

RirConfigListOperation = Literal["+", "-", "r"]

RIR_CONFIG_LIST_OPERATION_VALUES: set[RirConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_rir_config_list_operation(value: str) -> RirConfigListOperation:
    if value in RIR_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RIR_CONFIG_LIST_OPERATION_VALUES!r}"
    )
