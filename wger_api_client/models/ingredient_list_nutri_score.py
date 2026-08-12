from typing import Literal

IngredientListNutriScore = Literal["a", "b", "c", "d", "e"]

INGREDIENT_LIST_NUTRI_SCORE_VALUES: set[IngredientListNutriScore] = {
    "a",
    "b",
    "c",
    "d",
    "e",
}


def check_ingredient_list_nutri_score(value: str) -> IngredientListNutriScore:
    if value in INGREDIENT_LIST_NUTRI_SCORE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INGREDIENT_LIST_NUTRI_SCORE_VALUES!r}"
    )
