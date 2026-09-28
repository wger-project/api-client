from typing import Literal

MeasurementCategoryListMetricType = Literal[
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

MEASUREMENT_CATEGORY_LIST_METRIC_TYPE_VALUES: set[MeasurementCategoryListMetricType] = {
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


def check_measurement_category_list_metric_type(
    value: str,
) -> MeasurementCategoryListMetricType:
    if value in MEASUREMENT_CATEGORY_LIST_METRIC_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEASUREMENT_CATEGORY_LIST_METRIC_TYPE_VALUES!r}"
    )
