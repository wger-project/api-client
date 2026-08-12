from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogItem")


@_attrs_define
class LogItem:
    """LogItem serializer

    Attributes:
        plan (UUID):
        ingredient (int):
        amount (str):
        id (UUID | Unset):
        meal (None | Unset | UUID):
        weight_unit (int | None | Unset):
        datetime_ (datetime.datetime | Unset):
    """

    plan: UUID
    ingredient: int
    amount: str
    id: UUID | Unset = UNSET
    meal: None | Unset | UUID = UNSET
    weight_unit: int | None | Unset = UNSET
    datetime_: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = str(self.plan)

        ingredient = self.ingredient

        amount = self.amount

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        meal: None | str | Unset
        if isinstance(self.meal, Unset):
            meal = UNSET
        elif isinstance(self.meal, UUID):
            meal = str(self.meal)
        else:
            meal = self.meal

        weight_unit: int | None | Unset
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        else:
            weight_unit = self.weight_unit

        datetime_: str | Unset = UNSET
        if not isinstance(self.datetime_, Unset):
            datetime_ = self.datetime_.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
                "ingredient": ingredient,
                "amount": amount,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if meal is not UNSET:
            field_dict["meal"] = meal
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        plan = UUID(d.pop("plan"))

        ingredient = d.pop("ingredient")

        amount = d.pop("amount")

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_meal(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meal_type_0 = UUID(data)

                return meal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        meal = _parse_meal(d.pop("meal", UNSET))

        def _parse_weight_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        _datetime_ = d.pop("datetime", UNSET)
        datetime_: datetime.datetime | Unset
        if isinstance(_datetime_, Unset):
            datetime_ = UNSET
        else:
            datetime_ = datetime.datetime.fromisoformat(_datetime_)

        log_item = cls(
            plan=plan,
            ingredient=ingredient,
            amount=amount,
            id=id,
            meal=meal,
            weight_unit=weight_unit,
            datetime_=datetime_,
        )

        log_item.additional_properties = d
        return log_item

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
