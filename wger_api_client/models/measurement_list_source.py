from typing import Literal

MeasurementListSource = Literal["apple", "calculated", "google", "user"]

MEASUREMENT_LIST_SOURCE_VALUES: set[MeasurementListSource] = {
    "apple",
    "calculated",
    "google",
    "user",
}


def check_measurement_list_source(value: str) -> MeasurementListSource:
    if value in MEASUREMENT_LIST_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEASUREMENT_LIST_SOURCE_VALUES!r}"
    )
