from typing import Literal

RepetitionsConfigListOperation = Literal["+", "-", "r"]

REPETITIONS_CONFIG_LIST_OPERATION_VALUES: set[RepetitionsConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_repetitions_config_list_operation(
    value: str,
) -> RepetitionsConfigListOperation:
    if value in REPETITIONS_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REPETITIONS_CONFIG_LIST_OPERATION_VALUES!r}"
    )
