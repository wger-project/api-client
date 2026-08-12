from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IngredientWeightUnit")


@_attrs_define
class IngredientWeightUnit:
    """IngredientWeightUnit serializer

    Attributes:
        id (int):
        uuid (UUID):
        ingredient (int):
        gram (int):
        name (str):
    """

    id: int
    uuid: UUID
    ingredient: int
    gram: int
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = str(self.uuid)

        ingredient = self.ingredient

        gram = self.gram

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "ingredient": ingredient,
                "gram": gram,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        ingredient = d.pop("ingredient")

        gram = d.pop("gram")

        name = d.pop("name")

        ingredient_weight_unit = cls(
            id=id,
            uuid=uuid,
            ingredient=ingredient,
            gram=gram,
            name=name,
        )

        ingredient_weight_unit.additional_properties = d
        return ingredient_weight_unit

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
