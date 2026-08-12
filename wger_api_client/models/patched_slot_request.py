from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedSlotRequest")


@_attrs_define
class PatchedSlotRequest:
    """Slot

    Attributes:
        day (int | Unset):
        order (int | Unset):
        comment (str | Unset):
        config (Any | Unset):
    """

    day: int | Unset = UNSET
    order: int | Unset = UNSET
    comment: str | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        order = self.order

        comment = self.comment

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
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
        day = d.pop("day", UNSET)

        order = d.pop("order", UNSET)

        comment = d.pop("comment", UNSET)

        config = d.pop("config", UNSET)

        patched_slot_request = cls(
            day=day,
            order=order,
            comment=comment,
            config=config,
        )

        patched_slot_request.additional_properties = d
        return patched_slot_request

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
