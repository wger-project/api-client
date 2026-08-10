from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.day_structure import DayStructure


T = TypeVar("T", bound="RoutineStructure")


@_attrs_define
class RoutineStructure:
    """Routine structure serializer

    Attributes:
        id (int):
        created (datetime.datetime):
        start (datetime.date):
        end (datetime.date):
        days (list[DayStructure]):
        name (str | Unset):
        description (str | Unset):
        fit_in_week (bool | Unset):
    """

    id: int
    created: datetime.datetime
    start: datetime.date
    end: datetime.date
    days: list[DayStructure]
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    fit_in_week: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created = self.created.isoformat()

        start = self.start.isoformat()

        end = self.end.isoformat()

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        name = self.name

        description = self.description

        fit_in_week = self.fit_in_week

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "start": start,
                "end": end,
                "days": days,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if fit_in_week is not UNSET:
            field_dict["fit_in_week"] = fit_in_week

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.day_structure import DayStructure

        d = dict(src_dict)
        id = d.pop("id")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        start = datetime.date.fromisoformat(d.pop("start"))

        end = datetime.date.fromisoformat(d.pop("end"))

        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = DayStructure.from_dict(days_item_data)

            days.append(days_item)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        fit_in_week = d.pop("fit_in_week", UNSET)

        routine_structure = cls(
            id=id,
            created=created,
            start=start,
            end=end,
            days=days,
            name=name,
            description=description,
            fit_in_week=fit_in_week,
        )

        routine_structure.additional_properties = d
        return routine_structure

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
