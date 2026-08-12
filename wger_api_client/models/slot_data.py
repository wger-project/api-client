from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.set_config_data import SetConfigData


T = TypeVar("T", bound="SlotData")


@_attrs_define
class SlotData:
    """Slot Data serializer

    Attributes:
        comment (str):
        is_superset (bool):
        exercises (list[int]):
        sets (list[SetConfigData]):
    """

    comment: str
    is_superset: bool
    exercises: list[int]
    sets: list[SetConfigData]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        is_superset = self.is_superset

        exercises = self.exercises

        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment": comment,
                "is_superset": is_superset,
                "exercises": exercises,
                "sets": sets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.set_config_data import SetConfigData

        d = dict(src_dict)
        comment = d.pop("comment")

        is_superset = d.pop("is_superset")

        exercises = cast(list[int], d.pop("exercises"))

        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = SetConfigData.from_dict(sets_item_data)

            sets.append(sets_item)

        slot_data = cls(
            comment=comment,
            is_superset=is_superset,
            exercises=exercises,
            sets=sets,
        )

        slot_data.additional_properties = d
        return slot_data

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
