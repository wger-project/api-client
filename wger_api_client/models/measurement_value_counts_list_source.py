from typing import Literal

MeasurementValueCountsListSource = Literal["apple", "calculated", "google", "user"]

MEASUREMENT_VALUE_COUNTS_LIST_SOURCE_VALUES: set[MeasurementValueCountsListSource] = {
    "apple",
    "calculated",
    "google",
    "user",
}


def check_measurement_value_counts_list_source(
    value: str,
) -> MeasurementValueCountsListSource:
    if value in MEASUREMENT_VALUE_COUNTS_LIST_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEASUREMENT_VALUE_COUNTS_LIST_SOURCE_VALUES!r}"
    )
