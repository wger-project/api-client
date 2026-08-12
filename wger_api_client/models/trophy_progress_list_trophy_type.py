from typing import Literal

TrophyProgressListTrophyType = Literal[
    "count", "date", "other", "pr", "sequence", "time", "volume"
]

TROPHY_PROGRESS_LIST_TROPHY_TYPE_VALUES: set[TrophyProgressListTrophyType] = {
    "count",
    "date",
    "other",
    "pr",
    "sequence",
    "time",
    "volume",
}


def check_trophy_progress_list_trophy_type(value: str) -> TrophyProgressListTrophyType:
    if value in TROPHY_PROGRESS_LIST_TROPHY_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TROPHY_PROGRESS_LIST_TROPHY_TYPE_VALUES!r}"
    )
