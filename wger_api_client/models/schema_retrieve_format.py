from typing import Literal

SchemaRetrieveFormat = Literal["json", "yaml"]

SCHEMA_RETRIEVE_FORMAT_VALUES: set[SchemaRetrieveFormat] = {
    "json",
    "yaml",
}


def check_schema_retrieve_format(value: str) -> SchemaRetrieveFormat:
    if value in SCHEMA_RETRIEVE_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEMA_RETRIEVE_FORMAT_VALUES!r}"
    )
