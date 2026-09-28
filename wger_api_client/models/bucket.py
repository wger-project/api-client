from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Bucket")


@_attrs_define
class Bucket:
    """One calendar bucket of a category's entries, see `api.aggregates`.

    Read-only: buckets are derived, there is nothing to write back.

        Attributes:
            category (UUID):
            start (datetime.datetime):
            unit (None | str):
            count (int):
            sum_ (str):
            min_ (str):
            max_ (str):
    """

    category: UUID
    start: datetime.datetime
    unit: None | str
    count: int
    sum_: str
    min_: str
    max_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = str(self.category)

        start = self.start.isoformat()

        unit: None | str
        unit = self.unit

        count = self.count

        sum_ = self.sum_

        min_ = self.min_

        max_ = self.max_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "start": start,
                "unit": unit,
                "count": count,
                "sum": sum_,
                "min": min_,
                "max": max_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = UUID(d.pop("category"))

        start = datetime.datetime.fromisoformat(d.pop("start"))

        def _parse_unit(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        unit = _parse_unit(d.pop("unit"))

        count = d.pop("count")

        sum_ = d.pop("sum")

        min_ = d.pop("min")

        max_ = d.pop("max")

        bucket = cls(
            category=category,
            start=start,
            unit=unit,
            count=count,
            sum_=sum_,
            min_=min_,
            max_=max_,
        )

        bucket.additional_properties = d
        return bucket

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
