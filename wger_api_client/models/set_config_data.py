from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SetConfigData")


@_attrs_define
class SetConfigData:
    """SetConfigData serializer

    Attributes:
        slot_entry_id (int):
        exercise (int):
        sets (int):
        max_sets (int | None):
        weight (str):
        max_weight (str):
        weight_unit (int | None):
        weight_rounding (str):
        repetitions (str):
        max_repetitions (str):
        repetitions_unit (int | None):
        repetitions_rounding (str):
        rir (str):
        max_rir (str):
        rpe (str):
        rest (str):
        max_rest (str):
        type_ (str):
        text_repr (str):
        comment (str):
    """

    slot_entry_id: int
    exercise: int
    sets: int
    max_sets: int | None
    weight: str
    max_weight: str
    weight_unit: int | None
    weight_rounding: str
    repetitions: str
    max_repetitions: str
    repetitions_unit: int | None
    repetitions_rounding: str
    rir: str
    max_rir: str
    rpe: str
    rest: str
    max_rest: str
    type_: str
    text_repr: str
    comment: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slot_entry_id = self.slot_entry_id

        exercise = self.exercise

        sets = self.sets

        max_sets: int | None
        max_sets = self.max_sets

        weight = self.weight

        max_weight = self.max_weight

        weight_unit: int | None
        weight_unit = self.weight_unit

        weight_rounding = self.weight_rounding

        repetitions = self.repetitions

        max_repetitions = self.max_repetitions

        repetitions_unit: int | None
        repetitions_unit = self.repetitions_unit

        repetitions_rounding = self.repetitions_rounding

        rir = self.rir

        max_rir = self.max_rir

        rpe = self.rpe

        rest = self.rest

        max_rest = self.max_rest

        type_ = self.type_

        text_repr = self.text_repr

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slot_entry_id": slot_entry_id,
                "exercise": exercise,
                "sets": sets,
                "max_sets": max_sets,
                "weight": weight,
                "max_weight": max_weight,
                "weight_unit": weight_unit,
                "weight_rounding": weight_rounding,
                "repetitions": repetitions,
                "max_repetitions": max_repetitions,
                "repetitions_unit": repetitions_unit,
                "repetitions_rounding": repetitions_rounding,
                "rir": rir,
                "max_rir": max_rir,
                "rpe": rpe,
                "rest": rest,
                "max_rest": max_rest,
                "type": type_,
                "text_repr": text_repr,
                "comment": comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        slot_entry_id = d.pop("slot_entry_id")

        exercise = d.pop("exercise")

        sets = d.pop("sets")

        def _parse_max_sets(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        max_sets = _parse_max_sets(d.pop("max_sets"))

        weight = d.pop("weight")

        max_weight = d.pop("max_weight")

        def _parse_weight_unit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit"))

        weight_rounding = d.pop("weight_rounding")

        repetitions = d.pop("repetitions")

        max_repetitions = d.pop("max_repetitions")

        def _parse_repetitions_unit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        repetitions_unit = _parse_repetitions_unit(d.pop("repetitions_unit"))

        repetitions_rounding = d.pop("repetitions_rounding")

        rir = d.pop("rir")

        max_rir = d.pop("max_rir")

        rpe = d.pop("rpe")

        rest = d.pop("rest")

        max_rest = d.pop("max_rest")

        type_ = d.pop("type")

        text_repr = d.pop("text_repr")

        comment = d.pop("comment")

        set_config_data = cls(
            slot_entry_id=slot_entry_id,
            exercise=exercise,
            sets=sets,
            max_sets=max_sets,
            weight=weight,
            max_weight=max_weight,
            weight_unit=weight_unit,
            weight_rounding=weight_rounding,
            repetitions=repetitions,
            max_repetitions=max_repetitions,
            repetitions_unit=repetitions_unit,
            repetitions_rounding=repetitions_rounding,
            rir=rir,
            max_rir=max_rir,
            rpe=rpe,
            rest=rest,
            max_rest=max_rest,
            type_=type_,
            text_repr=text_repr,
            comment=comment,
        )

        set_config_data.additional_properties = d
        return set_config_data

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
