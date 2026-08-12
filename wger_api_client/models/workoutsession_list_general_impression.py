from typing import Literal

WorkoutsessionListGeneralImpression = Literal["1", "2", "3"]

WORKOUTSESSION_LIST_GENERAL_IMPRESSION_VALUES: set[
    WorkoutsessionListGeneralImpression
] = {
    "1",
    "2",
    "3",
}


def check_workoutsession_list_general_impression(
    value: str,
) -> WorkoutsessionListGeneralImpression:
    if value in WORKOUTSESSION_LIST_GENERAL_IMPRESSION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKOUTSESSION_LIST_GENERAL_IMPRESSION_VALUES!r}"
    )
