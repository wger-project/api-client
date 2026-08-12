from typing import Literal

TrophyListTrophyType = Literal[
    "count", "date", "other", "pr", "sequence", "time", "volume"
]

TROPHY_LIST_TROPHY_TYPE_VALUES: set[TrophyListTrophyType] = {
    "count",
    "date",
    "other",
    "pr",
    "sequence",
    "time",
    "volume",
}


def check_trophy_list_trophy_type(value: str) -> TrophyListTrophyType:
    if value in TROPHY_LIST_TROPHY_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TROPHY_LIST_TROPHY_TYPE_VALUES!r}"
    )
