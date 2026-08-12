from typing import Literal

DeletionLogListModelType = Literal["base", "image", "translation", "video"]

DELETION_LOG_LIST_MODEL_TYPE_VALUES: set[DeletionLogListModelType] = {
    "base",
    "image",
    "translation",
    "video",
}


def check_deletion_log_list_model_type(value: str) -> DeletionLogListModelType:
    if value in DELETION_LOG_LIST_MODEL_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELETION_LOG_LIST_MODEL_TYPE_VALUES!r}"
    )
