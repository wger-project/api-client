from typing import Literal

IngredientinfoListNutriScore = Literal["a", "b", "c", "d", "e"]

INGREDIENTINFO_LIST_NUTRI_SCORE_VALUES: set[IngredientinfoListNutriScore] = {
    "a",
    "b",
    "c",
    "d",
    "e",
}


def check_ingredientinfo_list_nutri_score(value: str) -> IngredientinfoListNutriScore:
    if value in INGREDIENTINFO_LIST_NUTRI_SCORE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INGREDIENTINFO_LIST_NUTRI_SCORE_VALUES!r}"
    )
