from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ValueCount")


@_attrs_define
class ValueCount:
    """How often one value occurred, and when it was measured last. Read-only for
    the same reason as `BucketSerializer`.

        Attributes:
            category (UUID):
            value (str):
            unit (None | str):
            count (int):
            newest (datetime.datetime):
    """

    category: UUID
    value: str
    unit: None | str
    count: int
    newest: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = str(self.category)

        value = self.value

        unit: None | str
        unit = self.unit

        count = self.count

        newest = self.newest.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "value": value,
                "unit": unit,
                "count": count,
                "newest": newest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = UUID(d.pop("category"))

        value = d.pop("value")

        def _parse_unit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unit = _parse_unit(d.pop("unit"))

        count = d.pop("count")

        newest = datetime.datetime.fromisoformat(d.pop("newest"))

        value_count = cls(
            category=category,
            value=value,
            unit=unit,
            count=count,
            newest=newest,
        )

        value_count.additional_properties = d
        return value_count

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
