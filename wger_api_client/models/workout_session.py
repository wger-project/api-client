from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.impression_enum import ImpressionEnum, check_impression_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkoutSession")


@_attrs_define
class WorkoutSession:
    """Workout session serializer

    Attributes:
        id (UUID | Unset):
        routine (int | None | Unset):
        day (int | None | Unset):
        notes (None | str | Unset): Any notes you might want to save about this workout session.
        impression (ImpressionEnum | Unset): * `1` - Bad
            * `2` - Neutral
            * `3` - Good
        datetime_start (datetime.datetime | Unset):
        datetime_end (datetime.datetime | None | Unset):
    """

    id: UUID | Unset = UNSET
    routine: int | None | Unset = UNSET
    day: int | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    impression: ImpressionEnum | Unset = UNSET
    datetime_start: datetime.datetime | Unset = UNSET
    datetime_end: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        routine: int | None | Unset
        if isinstance(self.routine, Unset):
            routine = UNSET
        else:
            routine = self.routine

        day: int | None | Unset
        if isinstance(self.day, Unset):
            day = UNSET
        else:
            day = self.day

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        impression: str | Unset = UNSET
        if not isinstance(self.impression, Unset):
            impression = self.impression

        datetime_start: str | Unset = UNSET
        if not isinstance(self.datetime_start, Unset):
            datetime_start = self.datetime_start.isoformat()

        datetime_end: None | str | Unset
        if isinstance(self.datetime_end, Unset):
            datetime_end = UNSET
        elif isinstance(self.datetime_end, datetime.datetime):
            datetime_end = self.datetime_end.isoformat()
        else:
            datetime_end = self.datetime_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if routine is not UNSET:
            field_dict["routine"] = routine
        if day is not UNSET:
            field_dict["day"] = day
        if notes is not UNSET:
            field_dict["notes"] = notes
        if impression is not UNSET:
            field_dict["impression"] = impression
        if datetime_start is not UNSET:
            field_dict["datetime_start"] = datetime_start
        if datetime_end is not UNSET:
            field_dict["datetime_end"] = datetime_end

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

        def _parse_routine(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        routine = _parse_routine(d.pop("routine", UNSET))

        def _parse_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        day = _parse_day(d.pop("day", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _impression = d.pop("impression", UNSET)
        impression: ImpressionEnum | Unset
        if isinstance(_impression, Unset):
            impression = UNSET
        else:
            impression = check_impression_enum(_impression)

        _datetime_start = d.pop("datetime_start", UNSET)
        datetime_start: datetime.datetime | Unset
        if isinstance(_datetime_start, Unset):
            datetime_start = UNSET
        else:
            datetime_start = datetime.datetime.fromisoformat(_datetime_start)

        def _parse_datetime_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                datetime_end_type_0 = datetime.datetime.fromisoformat(data)

                return datetime_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        datetime_end = _parse_datetime_end(d.pop("datetime_end", UNSET))

        workout_session = cls(
            id=id,
            routine=routine,
            day=day,
            notes=notes,
            impression=impression,
            datetime_start=datetime_start,
            datetime_end=datetime_end,
        )

        workout_session.additional_properties = d
        return workout_session

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
