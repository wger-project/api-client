from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkoutLogRequest")


@_attrs_define
class WorkoutLogRequest:
    """Workout log serializer

    Attributes:
        exercise (int):
        id (UUID | Unset):
        date (datetime.datetime | Unset):
        session (None | Unset | UUID):
        routine (int | None | Unset):
        iteration (int | None | Unset):
        slot_entry (int | None | Unset):
        next_log (None | Unset | UUID):
        repetitions_unit (int | None | Unset):
        repetitions (None | str | Unset):
        repetitions_target (None | str | Unset):
        weight_unit (int | None | Unset):
        weight (None | str | Unset):
        weight_target (None | str | Unset):
        rir (None | str | Unset):
        rir_target (None | str | Unset):
        rest (int | None | Unset):
        rest_target (int | None | Unset):
    """

    exercise: int
    id: UUID | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    session: None | Unset | UUID = UNSET
    routine: int | None | Unset = UNSET
    iteration: int | None | Unset = UNSET
    slot_entry: int | None | Unset = UNSET
    next_log: None | Unset | UUID = UNSET
    repetitions_unit: int | None | Unset = UNSET
    repetitions: None | str | Unset = UNSET
    repetitions_target: None | str | Unset = UNSET
    weight_unit: int | None | Unset = UNSET
    weight: None | str | Unset = UNSET
    weight_target: None | str | Unset = UNSET
    rir: None | str | Unset = UNSET
    rir_target: None | str | Unset = UNSET
    rest: int | None | Unset = UNSET
    rest_target: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercise = self.exercise

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        session: None | str | Unset
        if isinstance(self.session, Unset):
            session = UNSET
        elif isinstance(self.session, UUID):
            session = str(self.session)
        else:
            session = self.session

        routine: int | None | Unset
        if isinstance(self.routine, Unset):
            routine = UNSET
        else:
            routine = self.routine

        iteration: int | None | Unset
        if isinstance(self.iteration, Unset):
            iteration = UNSET
        else:
            iteration = self.iteration

        slot_entry: int | None | Unset
        if isinstance(self.slot_entry, Unset):
            slot_entry = UNSET
        else:
            slot_entry = self.slot_entry

        next_log: None | str | Unset
        if isinstance(self.next_log, Unset):
            next_log = UNSET
        elif isinstance(self.next_log, UUID):
            next_log = str(self.next_log)
        else:
            next_log = self.next_log

        repetitions_unit: int | None | Unset
        if isinstance(self.repetitions_unit, Unset):
            repetitions_unit = UNSET
        else:
            repetitions_unit = self.repetitions_unit

        repetitions: None | str | Unset
        if isinstance(self.repetitions, Unset):
            repetitions = UNSET
        else:
            repetitions = self.repetitions

        repetitions_target: None | str | Unset
        if isinstance(self.repetitions_target, Unset):
            repetitions_target = UNSET
        else:
            repetitions_target = self.repetitions_target

        weight_unit: int | None | Unset
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        else:
            weight_unit = self.weight_unit

        weight: None | str | Unset
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        weight_target: None | str | Unset
        if isinstance(self.weight_target, Unset):
            weight_target = UNSET
        else:
            weight_target = self.weight_target

        rir: None | str | Unset
        if isinstance(self.rir, Unset):
            rir = UNSET
        else:
            rir = self.rir

        rir_target: None | str | Unset
        if isinstance(self.rir_target, Unset):
            rir_target = UNSET
        else:
            rir_target = self.rir_target

        rest: int | None | Unset
        if isinstance(self.rest, Unset):
            rest = UNSET
        else:
            rest = self.rest

        rest_target: int | None | Unset
        if isinstance(self.rest_target, Unset):
            rest_target = UNSET
        else:
            rest_target = self.rest_target

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exercise": exercise,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if session is not UNSET:
            field_dict["session"] = session
        if routine is not UNSET:
            field_dict["routine"] = routine
        if iteration is not UNSET:
            field_dict["iteration"] = iteration
        if slot_entry is not UNSET:
            field_dict["slot_entry"] = slot_entry
        if next_log is not UNSET:
            field_dict["next_log"] = next_log
        if repetitions_unit is not UNSET:
            field_dict["repetitions_unit"] = repetitions_unit
        if repetitions is not UNSET:
            field_dict["repetitions"] = repetitions
        if repetitions_target is not UNSET:
            field_dict["repetitions_target"] = repetitions_target
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_target is not UNSET:
            field_dict["weight_target"] = weight_target
        if rir is not UNSET:
            field_dict["rir"] = rir
        if rir_target is not UNSET:
            field_dict["rir_target"] = rir_target
        if rest is not UNSET:
            field_dict["rest"] = rest
        if rest_target is not UNSET:
            field_dict["rest_target"] = rest_target

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exercise = d.pop("exercise")

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.datetime.fromisoformat(_date)

        def _parse_session(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                session_type_0 = UUID(data)

                return session_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        session = _parse_session(d.pop("session", UNSET))

        def _parse_routine(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        routine = _parse_routine(d.pop("routine", UNSET))

        def _parse_iteration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        iteration = _parse_iteration(d.pop("iteration", UNSET))

        def _parse_slot_entry(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slot_entry = _parse_slot_entry(d.pop("slot_entry", UNSET))

        def _parse_next_log(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_log_type_0 = UUID(data)

                return next_log_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        next_log = _parse_next_log(d.pop("next_log", UNSET))

        def _parse_repetitions_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        repetitions_unit = _parse_repetitions_unit(d.pop("repetitions_unit", UNSET))

        def _parse_repetitions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repetitions = _parse_repetitions(d.pop("repetitions", UNSET))

        def _parse_repetitions_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repetitions_target = _parse_repetitions_target(
            d.pop("repetitions_target", UNSET)
        )

        def _parse_weight_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        def _parse_weight(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weight = _parse_weight(d.pop("weight", UNSET))

        def _parse_weight_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weight_target = _parse_weight_target(d.pop("weight_target", UNSET))

        def _parse_rir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rir = _parse_rir(d.pop("rir", UNSET))

        def _parse_rir_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rir_target = _parse_rir_target(d.pop("rir_target", UNSET))

        def _parse_rest(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rest = _parse_rest(d.pop("rest", UNSET))

        def _parse_rest_target(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rest_target = _parse_rest_target(d.pop("rest_target", UNSET))

        workout_log_request = cls(
            exercise=exercise,
            id=id,
            date=date,
            session=session,
            routine=routine,
            iteration=iteration,
            slot_entry=slot_entry,
            next_log=next_log,
            repetitions_unit=repetitions_unit,
            repetitions=repetitions,
            repetitions_target=repetitions_target,
            weight_unit=weight_unit,
            weight=weight,
            weight_target=weight_target,
            rir=rir,
            rir_target=rir_target,
            rest=rest,
            rest_target=rest_target,
        )

        workout_log_request.additional_properties = d
        return workout_log_request

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
