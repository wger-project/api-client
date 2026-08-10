from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..models.impression_enum import ImpressionEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedWorkoutSessionRequest")


@_attrs_define
class PatchedWorkoutSessionRequest:
    """Workout session serializer

    Attributes:
        id (UUID | Unset):
        routine (int | None | Unset):
        day (int | None | Unset):
        date (datetime.date | Unset):
        notes (None | str | Unset): Any notes you might want to save about this workout session.
        impression (ImpressionEnum | Unset): * `1` - Bad
            * `2` - Neutral
            * `3` - Good
        time_start (None | str | Unset):
        time_end (None | str | Unset):
    """

    id: UUID | Unset = UNSET
    routine: int | None | Unset = UNSET
    day: int | None | Unset = UNSET
    date: datetime.date | Unset = UNSET
    notes: None | str | Unset = UNSET
    impression: ImpressionEnum | Unset = UNSET
    time_start: None | str | Unset = UNSET
    time_end: None | str | Unset = UNSET
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

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        impression: str | Unset = UNSET
        if not isinstance(self.impression, Unset):
            impression = self.impression.value

        time_start: None | str | Unset
        if isinstance(self.time_start, Unset):
            time_start = UNSET
        else:
            time_start = self.time_start

        time_end: None | str | Unset
        if isinstance(self.time_end, Unset):
            time_end = UNSET
        else:
            time_end = self.time_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if routine is not UNSET:
            field_dict["routine"] = routine
        if day is not UNSET:
            field_dict["day"] = day
        if date is not UNSET:
            field_dict["date"] = date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if impression is not UNSET:
            field_dict["impression"] = impression
        if time_start is not UNSET:
            field_dict["time_start"] = time_start
        if time_end is not UNSET:
            field_dict["time_end"] = time_end

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id), "text/plain")))

        if not isinstance(self.routine, Unset):
            if isinstance(self.routine, int):
                files.append(
                    ("routine", (None, str(self.routine).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("routine", (None, str(self.routine).encode(), "text/plain"))
                )

        if not isinstance(self.day, Unset):
            if isinstance(self.day, int):
                files.append(("day", (None, str(self.day).encode(), "text/plain")))
            else:
                files.append(("day", (None, str(self.day).encode(), "text/plain")))

        if not isinstance(self.date, Unset):
            files.append(("date", (None, self.date.isoformat().encode(), "text/plain")))

        if not isinstance(self.notes, Unset):
            if isinstance(self.notes, str):
                files.append(("notes", (None, str(self.notes).encode(), "text/plain")))
            else:
                files.append(("notes", (None, str(self.notes).encode(), "text/plain")))

        if not isinstance(self.impression, Unset):
            files.append(
                (
                    "impression",
                    (None, str(self.impression.value).encode(), "text/plain"),
                )
            )

        if not isinstance(self.time_start, Unset):
            if isinstance(self.time_start, str):
                files.append(
                    ("time_start", (None, str(self.time_start).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("time_start", (None, str(self.time_start).encode(), "text/plain"))
                )

        if not isinstance(self.time_end, Unset):
            if isinstance(self.time_end, str):
                files.append(
                    ("time_end", (None, str(self.time_end).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("time_end", (None, str(self.time_end).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

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

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

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
            impression = ImpressionEnum(_impression)

        def _parse_time_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_start = _parse_time_start(d.pop("time_start", UNSET))

        def _parse_time_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time_end = _parse_time_end(d.pop("time_end", UNSET))

        patched_workout_session_request = cls(
            id=id,
            routine=routine,
            day=day,
            date=date,
            notes=notes,
            impression=impression,
            time_start=time_start,
            time_end=time_end,
        )

        patched_workout_session_request.additional_properties = d
        return patched_workout_session_request

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
