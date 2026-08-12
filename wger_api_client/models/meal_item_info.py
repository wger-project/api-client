from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingredient_image import IngredientImage
    from ..models.ingredient_info import IngredientInfo
    from ..models.ingredient_weight_unit import IngredientWeightUnit


T = TypeVar("T", bound="MealItemInfo")


@_attrs_define
class MealItemInfo:
    """Meal Item info serializer

    Attributes:
        meal (UUID):
        ingredient (int):
        ingredient_obj (IngredientInfo): Ingredient info serializer
        weight_unit (int):
        weight_unit_obj (IngredientWeightUnit | None):
        image (IngredientImage | None):
        order (int):
        amount (str):
        id (UUID | Unset):
    """

    meal: UUID
    ingredient: int
    ingredient_obj: IngredientInfo
    weight_unit: int
    weight_unit_obj: IngredientWeightUnit | None
    image: IngredientImage | None
    order: int
    amount: str
    id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.ingredient_image import IngredientImage
        from ..models.ingredient_weight_unit import IngredientWeightUnit

        meal = str(self.meal)

        ingredient = self.ingredient

        ingredient_obj = self.ingredient_obj.to_dict()

        weight_unit = self.weight_unit

        weight_unit_obj: dict[str, Any] | None
        if isinstance(self.weight_unit_obj, IngredientWeightUnit):
            weight_unit_obj = self.weight_unit_obj.to_dict()
        else:
            weight_unit_obj = self.weight_unit_obj

        image: dict[str, Any] | None
        if isinstance(self.image, IngredientImage):
            image = self.image.to_dict()
        else:
            image = self.image

        order = self.order

        amount = self.amount

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meal": meal,
                "ingredient": ingredient,
                "ingredient_obj": ingredient_obj,
                "weight_unit": weight_unit,
                "weight_unit_obj": weight_unit_obj,
                "image": image,
                "order": order,
                "amount": amount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ingredient_image import IngredientImage
        from ..models.ingredient_info import IngredientInfo
        from ..models.ingredient_weight_unit import IngredientWeightUnit

        d = dict(src_dict)
        meal = UUID(d.pop("meal"))

        ingredient = d.pop("ingredient")

        ingredient_obj = IngredientInfo.from_dict(d.pop("ingredient_obj"))

        weight_unit = d.pop("weight_unit")

        def _parse_weight_unit_obj(data: object) -> IngredientWeightUnit | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weight_unit_obj_type_1 = IngredientWeightUnit.from_dict(data)

                return weight_unit_obj_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IngredientWeightUnit | None, data)

        weight_unit_obj = _parse_weight_unit_obj(d.pop("weight_unit_obj"))

        def _parse_image(data: object) -> IngredientImage | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_type_1 = IngredientImage.from_dict(data)

                return image_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IngredientImage | None, data)

        image = _parse_image(d.pop("image"))

        order = d.pop("order")

        amount = d.pop("amount")

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        meal_item_info = cls(
            meal=meal,
            ingredient=ingredient,
            ingredient_obj=ingredient_obj,
            weight_unit=weight_unit,
            weight_unit_obj=weight_unit_obj,
            image=image,
            order=order,
            amount=amount,
            id=id,
        )

        meal_item_info.additional_properties = d
        return meal_item_info

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
