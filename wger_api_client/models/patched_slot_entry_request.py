from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exercise_type_enum import ExerciseTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSlotEntryRequest")


@_attrs_define
class PatchedSlotEntryRequest:
    """Slot entry serializer

    Attributes:
        slot (int | Unset):
        exercise (int | Unset):
        type_ (ExerciseTypeEnum | Unset): * `normal` - Normal
            * `warmup` - Warmup
            * `dropset` - Dropset
            * `myo` - Myo
            * `partial` - Partial
            * `forced` - Forced
            * `tut` - Tut
            * `iso` - Iso Hold
            * `jump` - Jump
        repetition_unit (int | None | Unset):
        repetition_rounding (None | str | Unset):
        weight_unit (int | None | Unset):
        weight_rounding (None | str | Unset):
        order (int | Unset):
        comment (str | Unset):
        config (Any | Unset):
    """

    slot: int | Unset = UNSET
    exercise: int | Unset = UNSET
    type_: ExerciseTypeEnum | Unset = UNSET
    repetition_unit: int | None | Unset = UNSET
    repetition_rounding: None | str | Unset = UNSET
    weight_unit: int | None | Unset = UNSET
    weight_rounding: None | str | Unset = UNSET
    order: int | Unset = UNSET
    comment: str | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slot = self.slot

        exercise = self.exercise

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        repetition_unit: int | None | Unset
        if isinstance(self.repetition_unit, Unset):
            repetition_unit = UNSET
        else:
            repetition_unit = self.repetition_unit

        repetition_rounding: None | str | Unset
        if isinstance(self.repetition_rounding, Unset):
            repetition_rounding = UNSET
        else:
            repetition_rounding = self.repetition_rounding

        weight_unit: int | None | Unset
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        else:
            weight_unit = self.weight_unit

        weight_rounding: None | str | Unset
        if isinstance(self.weight_rounding, Unset):
            weight_rounding = UNSET
        else:
            weight_rounding = self.weight_rounding

        order = self.order

        comment = self.comment

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slot is not UNSET:
            field_dict["slot"] = slot
        if exercise is not UNSET:
            field_dict["exercise"] = exercise
        if type_ is not UNSET:
            field_dict["type"] = type_
        if repetition_unit is not UNSET:
            field_dict["repetition_unit"] = repetition_unit
        if repetition_rounding is not UNSET:
            field_dict["repetition_rounding"] = repetition_rounding
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if weight_rounding is not UNSET:
            field_dict["weight_rounding"] = weight_rounding
        if order is not UNSET:
            field_dict["order"] = order
        if comment is not UNSET:
            field_dict["comment"] = comment
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        slot = d.pop("slot", UNSET)

        exercise = d.pop("exercise", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ExerciseTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ExerciseTypeEnum(_type_)

        def _parse_repetition_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        repetition_unit = _parse_repetition_unit(d.pop("repetition_unit", UNSET))

        def _parse_repetition_rounding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repetition_rounding = _parse_repetition_rounding(
            d.pop("repetition_rounding", UNSET)
        )

        def _parse_weight_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        def _parse_weight_rounding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weight_rounding = _parse_weight_rounding(d.pop("weight_rounding", UNSET))

        order = d.pop("order", UNSET)

        comment = d.pop("comment", UNSET)

        config = d.pop("config", UNSET)

        patched_slot_entry_request = cls(
            slot=slot,
            exercise=exercise,
            type_=type_,
            repetition_unit=repetition_unit,
            repetition_rounding=repetition_rounding,
            weight_unit=weight_unit,
            weight_rounding=weight_rounding,
            order=order,
            comment=comment,
            config=config,
        )

        patched_slot_entry_request.additional_properties = d
        return patched_slot_entry_request

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
