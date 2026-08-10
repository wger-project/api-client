from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MealItem")


@_attrs_define
class MealItem:
    """MealItem serializer

    Attributes:
        meal (UUID):
        ingredient (int):
        order (int):
        amount (str):
        id (UUID | Unset):
        weight_unit (int | None | Unset):
    """

    meal: UUID
    ingredient: int
    order: int
    amount: str
    id: UUID | Unset = UNSET
    weight_unit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meal = str(self.meal)

        ingredient = self.ingredient

        order = self.order

        amount = self.amount

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        weight_unit: int | None | Unset
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        else:
            weight_unit = self.weight_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meal": meal,
                "ingredient": ingredient,
                "order": order,
                "amount": amount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        meal = UUID(d.pop("meal"))

        ingredient = d.pop("ingredient")

        order = d.pop("order")

        amount = d.pop("amount")

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_weight_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        meal_item = cls(
            meal=meal,
            ingredient=ingredient,
            order=order,
            amount=amount,
            id=id,
            weight_unit=weight_unit,
        )

        meal_item.additional_properties = d
        return meal_item

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
