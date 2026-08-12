from typing import Literal

MaxRepetitionsConfigListOperation = Literal["+", "-", "r"]

MAX_REPETITIONS_CONFIG_LIST_OPERATION_VALUES: set[MaxRepetitionsConfigListOperation] = {
    "+",
    "-",
    "r",
}


def check_max_repetitions_config_list_operation(
    value: str,
) -> MaxRepetitionsConfigListOperation:
    if value in MAX_REPETITIONS_CONFIG_LIST_OPERATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MAX_REPETITIONS_CONFIG_LIST_OPERATION_VALUES!r}"
    )
