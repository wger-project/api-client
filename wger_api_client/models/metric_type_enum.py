from typing import Literal

MetricTypeEnum = Literal[
    "blood_oxygen",
    "blood_pressure",
    "blood_pressure_diastolic",
    "blood_pressure_systolic",
    "body_fat",
    "body_weight",
    "custom",
    "distance",
    "energy",
    "heart_rate",
    "height",
    "lean_body_mass",
    "resting_heart_rate",
    "sleep",
    "sleep_awake",
    "sleep_deep",
    "sleep_light",
    "sleep_rem",
    "sleep_total",
    "steps",
]

METRIC_TYPE_ENUM_VALUES: set[MetricTypeEnum] = {
    "blood_oxygen",
    "blood_pressure",
    "blood_pressure_diastolic",
    "blood_pressure_systolic",
    "body_fat",
    "body_weight",
    "custom",
    "distance",
    "energy",
    "heart_rate",
    "height",
    "lean_body_mass",
    "resting_heart_rate",
    "sleep",
    "sleep_awake",
    "sleep_deep",
    "sleep_light",
    "sleep_rem",
    "sleep_total",
    "steps",
}


def check_metric_type_enum(value: str) -> MetricTypeEnum:
    if value in METRIC_TYPE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {METRIC_TYPE_ENUM_VALUES!r}"
    )
