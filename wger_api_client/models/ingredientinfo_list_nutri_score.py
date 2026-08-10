from enum import Enum


class IngredientinfoListNutriScore(str, Enum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"
    E = "e"

    def __str__(self) -> str:
        return str(self.value)
