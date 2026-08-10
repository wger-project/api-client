from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlotRequest")


@_attrs_define
class SlotRequest:
    """Slot

    Attributes:
        day (int):
        order (int | Unset):
        comment (str | Unset):
        config (Any | Unset):
    """

    day: int
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
        field_dict.update(
            {
                "day": day,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if comment is not UNSET:
            field_dict["comment"] = comment
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("day", (None, str(self.day).encode(), "text/plain")))

        if not isinstance(self.order, Unset):
            files.append(("order", (None, str(self.order).encode(), "text/plain")))

        if not isinstance(self.comment, Unset):
            files.append(("comment", (None, str(self.comment).encode(), "text/plain")))

        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        day = d.pop("day")

        order = d.pop("order", UNSET)

        comment = d.pop("comment", UNSET)

        config = d.pop("config", UNSET)

        slot_request = cls(
            day=day,
            order=order,
            comment=comment,
            config=config,
        )

        slot_request.additional_properties = d
        return slot_request

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
