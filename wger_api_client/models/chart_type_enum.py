from typing import Literal

ChartTypeEnum = Literal["bar", "delta", "distribution", "heatmap", "line"]

CHART_TYPE_ENUM_VALUES: set[ChartTypeEnum] = {
    "bar",
    "delta",
    "distribution",
    "heatmap",
    "line",
}


def check_chart_type_enum(value: str) -> ChartTypeEnum:
    if value in CHART_TYPE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHART_TYPE_ENUM_VALUES!r}"
    )
