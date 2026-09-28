from typing import Literal

MeasurementAggregateListSource = Literal["apple", "calculated", "google", "user"]

MEASUREMENT_AGGREGATE_LIST_SOURCE_VALUES: set[MeasurementAggregateListSource] = {
    "apple",
    "calculated",
    "google",
    "user",
}


def check_measurement_aggregate_list_source(
    value: str,
) -> MeasurementAggregateListSource:
    if value in MEASUREMENT_AGGREGATE_LIST_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEASUREMENT_AGGREGATE_LIST_SOURCE_VALUES!r}"
    )
