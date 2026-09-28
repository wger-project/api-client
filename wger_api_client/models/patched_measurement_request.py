from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_enum import SourceEnum, check_source_enum
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
        source (SourceEnum | Unset): * `user` - User
            * `google` - Google
            * `apple` - Apple
            * `calculated` - Calculated
        external_id (None | Unset | UUID):
        extra_data (Any | Unset):
    """

    id: UUID | Unset = UNSET
    category: UUID | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    value: float | Unset = UNSET
    notes: str | Unset = UNSET
    source: SourceEnum | Unset = UNSET
    external_id: None | Unset | UUID = UNSET
    extra_data: Any | Unset = UNSET
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

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        elif isinstance(self.external_id, UUID):
            external_id = str(self.external_id)
        else:
            external_id = self.external_id

        extra_data = self.extra_data

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
        if source is not UNSET:
            field_dict["source"] = source
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if extra_data is not UNSET:
            field_dict["extra_data"] = extra_data

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

        _source = d.pop("source", UNSET)
        source: SourceEnum | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_source_enum(_source)

        def _parse_external_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                external_id_type_0 = UUID(data)

                return external_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        extra_data = d.pop("extra_data", UNSET)

        patched_measurement_request = cls(
            id=id,
            category=category,
            date=date,
            value=value,
            notes=notes,
            source=source,
            external_id=external_id,
            extra_data=extra_data,
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
