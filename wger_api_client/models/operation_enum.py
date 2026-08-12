from typing import Literal

OperationEnum = Literal["+", "-", "r"]

OPERATION_ENUM_VALUES: set[OperationEnum] = {
    "+",
    "-",
    "r",
}


def check_operation_enum(value: str) -> OperationEnum:
    if value in OPERATION_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {OPERATION_ENUM_VALUES!r}"
    )
