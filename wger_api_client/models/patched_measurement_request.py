from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMeasurementRequest")


@_attrs_define
class PatchedMeasurementRequest:
    """Measurement serializer

    Attributes:
        id (UUID | Unset):
        category (UUID | Unset):
        date (datetime.datetime | Unset):
        value (float | Unset):
        notes (str | Unset):
    """

    id: UUID | Unset = UNSET
    category: UUID | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    value: float | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = str(self.category)

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        value = self.value

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if date is not UNSET:
            field_dict["date"] = date
        if value is not UNSET:
            field_dict["value"] = value
        if notes is not UNSET:
            field_dict["notes"] = notes

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

        _category = d.pop("category", UNSET)
        category: UUID | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = UUID(_category)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.datetime.fromisoformat(_date)

        value = d.pop("value", UNSET)

        notes = d.pop("notes", UNSET)

        patched_measurement_request = cls(
            id=id,
            category=category,
            date=date,
            value=value,
            notes=notes,
        )

        patched_measurement_request.additional_properties = d
        return patched_measurement_request

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
