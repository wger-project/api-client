from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="MealItemRequest")


@_attrs_define
class MealItemRequest:
    """MealItem serializer

    Attributes:
        meal (UUID):
        ingredient (int):
        amount (str):
        id (UUID | Unset):
        weight_unit (int | None | Unset):
    """

    meal: UUID
    ingredient: int
    amount: str
    id: UUID | Unset = UNSET
    weight_unit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meal = str(self.meal)

        ingredient = self.ingredient

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
                "amount": amount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("meal", (None, str(self.meal), "text/plain")))

        files.append(
            ("ingredient", (None, str(self.ingredient).encode(), "text/plain"))
        )

        files.append(("amount", (None, str(self.amount).encode(), "text/plain")))

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id), "text/plain")))

        if not isinstance(self.weight_unit, Unset):
            if isinstance(self.weight_unit, int):
                files.append(
                    (
                        "weight_unit",
                        (None, str(self.weight_unit).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "weight_unit",
                        (None, str(self.weight_unit).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        meal = UUID(d.pop("meal"))

        ingredient = d.pop("ingredient")

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

        meal_item_request = cls(
            meal=meal,
            ingredient=ingredient,
            amount=amount,
            id=id,
            weight_unit=weight_unit,
        )

        meal_item_request.additional_properties = d
        return meal_item_request

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
