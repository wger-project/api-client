from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WeightEntry")


@_attrs_define
class WeightEntry:
    """Weight serializer

    Attributes:
        id (int):
        date (datetime.datetime):
        weight (str):
        user (int):
    """

    id: int
    date: datetime.datetime
    weight: str
    user: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        weight = self.weight

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "weight": weight,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        date = datetime.datetime.fromisoformat(d.pop("date"))

        weight = d.pop("weight")

        user = d.pop("user")

        weight_entry = cls(
            id=id,
            date=date,
            weight=weight,
            user=user,
        )

        weight_entry.additional_properties = d
        return weight_entry

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
