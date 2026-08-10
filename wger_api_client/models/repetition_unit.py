from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.unit_type_enum import UnitTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepetitionUnit")


@_attrs_define
class RepetitionUnit:
    """Repetition unit serializer

    Attributes:
        id (int):
        name (str):
        unit_type (UnitTypeEnum | Unset): * `REPETITIONS` - Repetitions
            * `TIME` - Time
            * `DISTANCE` - Distance
        multiplier (int | None | Unset): Multiplier to convert this unit to a base unit. Time units are converted
                    to seconds, distance units to meters, and repetitions remain unchanged. For example:
                    minutes -> 60, kilometers -> 1000. Leave empty if a multiplier does not apply.
    """

    id: int
    name: str
    unit_type: UnitTypeEnum | Unset = UNSET
    multiplier: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        unit_type: str | Unset = UNSET
        if not isinstance(self.unit_type, Unset):
            unit_type = self.unit_type.value

        multiplier: int | None | Unset
        if isinstance(self.multiplier, Unset):
            multiplier = UNSET
        else:
            multiplier = self.multiplier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if unit_type is not UNSET:
            field_dict["unit_type"] = unit_type
        if multiplier is not UNSET:
            field_dict["multiplier"] = multiplier

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        _unit_type = d.pop("unit_type", UNSET)
        unit_type: UnitTypeEnum | Unset
        if isinstance(_unit_type, Unset):
            unit_type = UNSET
        else:
            unit_type = UnitTypeEnum(_unit_type)

        def _parse_multiplier(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        multiplier = _parse_multiplier(d.pop("multiplier", UNSET))

        repetition_unit = cls(
            id=id,
            name=name,
            unit_type=unit_type,
            multiplier=multiplier,
        )

        repetition_unit.additional_properties = d
        return repetition_unit

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
