from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedLogItemRequest")


@_attrs_define
class PatchedLogItemRequest:
    """LogItem serializer

    Attributes:
        id (UUID | Unset):
        plan (UUID | Unset):
        meal (None | Unset | UUID):
        ingredient (int | Unset):
        weight_unit (int | None | Unset):
        datetime_ (datetime.datetime | Unset):
        amount (str | Unset):
    """

    id: UUID | Unset = UNSET
    plan: UUID | Unset = UNSET
    meal: None | Unset | UUID = UNSET
    ingredient: int | Unset = UNSET
    weight_unit: int | None | Unset = UNSET
    datetime_: datetime.datetime | Unset = UNSET
    amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = str(self.plan)

        meal: None | str | Unset
        if isinstance(self.meal, Unset):
            meal = UNSET
        elif isinstance(self.meal, UUID):
            meal = str(self.meal)
        else:
            meal = self.meal

        ingredient = self.ingredient

        weight_unit: int | None | Unset
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        else:
            weight_unit = self.weight_unit

        datetime_: str | Unset = UNSET
        if not isinstance(self.datetime_, Unset):
            datetime_ = self.datetime_.isoformat()

        amount = self.amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if plan is not UNSET:
            field_dict["plan"] = plan
        if meal is not UNSET:
            field_dict["meal"] = meal
        if ingredient is not UNSET:
            field_dict["ingredient"] = ingredient
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if datetime_ is not UNSET:
            field_dict["datetime"] = datetime_
        if amount is not UNSET:
            field_dict["amount"] = amount

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _plan = d.pop("plan", UNSET)
        plan: UUID | Unset
        if isinstance(_plan, Unset):
            plan = UNSET
        else:
            plan = UUID(_plan)

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

        ingredient = d.pop("ingredient", UNSET)

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

        amount = d.pop("amount", UNSET)

        patched_log_item_request = cls(
            id=id,
            plan=plan,
            meal=meal,
            ingredient=ingredient,
            weight_unit=weight_unit,
            datetime_=datetime_,
            amount=amount,
        )

        patched_log_item_request.additional_properties = d
        return patched_log_item_request

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
