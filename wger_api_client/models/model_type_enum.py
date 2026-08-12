from typing import Literal

ModelTypeEnum = Literal["base", "image", "translation", "video"]

MODEL_TYPE_ENUM_VALUES: set[ModelTypeEnum] = {
    "base",
    "image",
    "translation",
    "video",
}


def check_model_type_enum(value: str) -> ModelTypeEnum:
    if value in MODEL_TYPE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MODEL_TYPE_ENUM_VALUES!r}"
    )
