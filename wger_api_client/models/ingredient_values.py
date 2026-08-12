from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingredient_values_errors import IngredientValuesErrors


T = TypeVar("T", bound="IngredientValues")


@_attrs_define
class IngredientValues:
    """Nutritional values for a given amount and unit of an ingredient.

    Carries the form errors instead of usable values when the amount or unit
    query parameters don't validate.

        Attributes:
            energy (float):
            protein (float):
            carbohydrates (float):
            carbohydrates_sugar (float | None):
            fat (float):
            fat_saturated (float | None):
            fiber (float | None):
            sodium (float | None):
            errors (IngredientValuesErrors | Unset):
    """

    energy: float
    protein: float
    carbohydrates: float
    carbohydrates_sugar: float | None
    fat: float
    fat_saturated: float | None
    fiber: float | None
    sodium: float | None
    errors: IngredientValuesErrors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        energy = self.energy

        protein = self.protein

        carbohydrates = self.carbohydrates

        carbohydrates_sugar: float | None
        carbohydrates_sugar = self.carbohydrates_sugar

        fat = self.fat

        fat_saturated: float | None
        fat_saturated = self.fat_saturated

        fiber: float | None
        fiber = self.fiber

        sodium: float | None
        sodium = self.sodium

        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "energy": energy,
                "protein": protein,
                "carbohydrates": carbohydrates,
                "carbohydrates_sugar": carbohydrates_sugar,
                "fat": fat,
                "fat_saturated": fat_saturated,
                "fiber": fiber,
                "sodium": sodium,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ingredient_values_errors import IngredientValuesErrors

        d = dict(src_dict)
        energy = d.pop("energy")

        protein = d.pop("protein")

        carbohydrates = d.pop("carbohydrates")

        def _parse_carbohydrates_sugar(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        carbohydrates_sugar = _parse_carbohydrates_sugar(d.pop("carbohydrates_sugar"))

        fat = d.pop("fat")

        def _parse_fat_saturated(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        fat_saturated = _parse_fat_saturated(d.pop("fat_saturated"))

        def _parse_fiber(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        fiber = _parse_fiber(d.pop("fiber"))

        def _parse_sodium(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        sodium = _parse_sodium(d.pop("sodium"))

        _errors = d.pop("errors", UNSET)
        errors: IngredientValuesErrors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = IngredientValuesErrors.from_dict(_errors)

        ingredient_values = cls(
            energy=energy,
            protein=protein,
            carbohydrates=carbohydrates,
            carbohydrates_sugar=carbohydrates_sugar,
            fat=fat,
            fat_saturated=fat_saturated,
            fiber=fiber,
            sodium=sodium,
            errors=errors,
        )

        ingredient_values.additional_properties = d
        return ingredient_values

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
