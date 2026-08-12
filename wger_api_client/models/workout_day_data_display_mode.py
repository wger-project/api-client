from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.day import Day
    from ..models.slot_data import SlotData


T = TypeVar("T", bound="WorkoutDayDataDisplayMode")


@_attrs_define
class WorkoutDayDataDisplayMode:
    """WorkoutDayData serializer - display mode

    Attributes:
        iteration (int):
        date (datetime.date):
        label (str):
        day (Day): Day serializer
        slots (list[SlotData]):
    """

    iteration: int
    date: datetime.date
    label: str
    day: Day
    slots: list[SlotData]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iteration = self.iteration

        date = self.date.isoformat()

        label = self.label

        day = self.day.to_dict()

        slots = []
        for slots_item_data in self.slots:
            slots_item = slots_item_data.to_dict()
            slots.append(slots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iteration": iteration,
                "date": date,
                "label": label,
                "day": day,
                "slots": slots,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.day import Day
        from ..models.slot_data import SlotData

        d = dict(src_dict)
        iteration = d.pop("iteration")

        date = datetime.date.fromisoformat(d.pop("date"))

        label = d.pop("label")

        day = Day.from_dict(d.pop("day"))

        slots = []
        _slots = d.pop("slots")
        for slots_item_data in _slots:
            slots_item = SlotData.from_dict(slots_item_data)

            slots.append(slots_item)

        workout_day_data_display_mode = cls(
            iteration=iteration,
            date=date,
            label=label,
            day=day,
            slots=slots,
        )

        workout_day_data_display_mode.additional_properties = d
        return workout_day_data_display_mode

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
