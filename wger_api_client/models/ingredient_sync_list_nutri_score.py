from typing import Literal

IngredientSyncListNutriScore = Literal["a", "b", "c", "d", "e"]

INGREDIENT_SYNC_LIST_NUTRI_SCORE_VALUES: set[IngredientSyncListNutriScore] = {
    "a",
    "b",
    "c",
    "d",
    "e",
}


def check_ingredient_sync_list_nutri_score(value: str) -> IngredientSyncListNutriScore:
    if value in INGREDIENT_SYNC_LIST_NUTRI_SCORE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INGREDIENT_SYNC_LIST_NUTRI_SCORE_VALUES!r}"
    )
