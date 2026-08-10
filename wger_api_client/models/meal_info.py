from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meal_item_info import MealItemInfo
    from ..models.nutritional_values import NutritionalValues


T = TypeVar("T", bound="MealInfo")


@_attrs_define
class MealInfo:
    """Meal info serializer

    Attributes:
        plan (UUID):
        order (int):
        meal_items (list[MealItemInfo]):
        nutritional_values (NutritionalValues): Nutritional values serializer
        id (UUID | Unset):
        time (None | str | Unset):
        name (str | Unset): Give meals a textual description / name such as "Breakfast" or "after workout"
    """

    plan: UUID
    order: int
    meal_items: list[MealItemInfo]
    nutritional_values: NutritionalValues
    id: UUID | Unset = UNSET
    time: None | str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = str(self.plan)

        order = self.order

        meal_items = []
        for meal_items_item_data in self.meal_items:
            meal_items_item = meal_items_item_data.to_dict()
            meal_items.append(meal_items_item)

        nutritional_values = self.nutritional_values.to_dict()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
                "order": order,
                "meal_items": meal_items,
                "nutritional_values": nutritional_values,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if time is not UNSET:
            field_dict["time"] = time
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.meal_item_info import MealItemInfo
        from ..models.nutritional_values import NutritionalValues

        d = dict(src_dict)
        plan = UUID(d.pop("plan"))

        order = d.pop("order")

        meal_items = []
        _meal_items = d.pop("meal_items")
        for meal_items_item_data in _meal_items:
            meal_items_item = MealItemInfo.from_dict(meal_items_item_data)

            meal_items.append(meal_items_item)

        nutritional_values = NutritionalValues.from_dict(d.pop("nutritional_values"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time = _parse_time(d.pop("time", UNSET))

        name = d.pop("name", UNSET)

        meal_info = cls(
            plan=plan,
            order=order,
            meal_items=meal_items,
            nutritional_values=nutritional_values,
            id=id,
            time=time,
            name=name,
        )

        meal_info.additional_properties = d
        return meal_info

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
