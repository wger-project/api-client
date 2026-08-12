from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Thumbnails")


@_attrs_define
class Thumbnails:
    """Shape of the ``thumbnails`` field, used for schema generation only.

    The aliases are read from settings.THUMBNAIL_ALIASES and are the same for
    every thumbnailed image in the API. Without this, the generated schema falls
    back to a plain string for the dict the method fields return.

        Attributes:
            small (str):
            medium (str):
    """

    small: str
    medium: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        small = self.small

        medium = self.medium

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "small": small,
                "medium": medium,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        small = d.pop("small")

        medium = d.pop("medium")

        thumbnails = cls(
            small=small,
            medium=medium,
        )

        thumbnails.additional_properties = d
        return thumbnails

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
