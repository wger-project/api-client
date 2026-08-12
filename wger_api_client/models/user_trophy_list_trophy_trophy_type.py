from typing import Literal

UserTrophyListTrophyTrophyType = Literal[
    "count", "date", "other", "pr", "sequence", "time", "volume"
]

USER_TROPHY_LIST_TROPHY_TROPHY_TYPE_VALUES: set[UserTrophyListTrophyTrophyType] = {
    "count",
    "date",
    "other",
    "pr",
    "sequence",
    "time",
    "volume",
}


def check_user_trophy_list_trophy_trophy_type(
    value: str,
) -> UserTrophyListTrophyTrophyType:
    if value in USER_TROPHY_LIST_TROPHY_TROPHY_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_TROPHY_LIST_TROPHY_TROPHY_TYPE_VALUES!r}"
    )
