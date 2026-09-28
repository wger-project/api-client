from typing import Literal

MeasurementAggregateListBucket = Literal["auto", "day", "hour", "month", "week"]

MEASUREMENT_AGGREGATE_LIST_BUCKET_VALUES: set[MeasurementAggregateListBucket] = {
    "auto",
    "day",
    "hour",
    "month",
    "week",
}


def check_measurement_aggregate_list_bucket(
    value: str,
) -> MeasurementAggregateListBucket:
    if value in MEASUREMENT_AGGREGATE_LIST_BUCKET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {MEASUREMENT_AGGREGATE_LIST_BUCKET_VALUES!r}"
    )
