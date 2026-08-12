from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.thumbnail_alias import ThumbnailAlias


T = TypeVar("T", bound="ImageThumbnails")


@_attrs_define
class ImageThumbnails:
    """An image's thumbnails, one entry per available size, plus the original.

    Attributes:
        small (ThumbnailAlias): One generated thumbnail: where it is and the size it was generated for.
        medium (ThumbnailAlias): One generated thumbnail: where it is and the size it was generated for.
        original (str):
    """

    small: ThumbnailAlias
    medium: ThumbnailAlias
    original: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        small = self.small.to_dict()

        medium = self.medium.to_dict()

        original = self.original

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "small": small,
                "medium": medium,
                "original": original,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.thumbnail_alias import ThumbnailAlias

        d = dict(src_dict)
        small = ThumbnailAlias.from_dict(d.pop("small"))

        medium = ThumbnailAlias.from_dict(d.pop("medium"))

        original = d.pop("original")

        image_thumbnails = cls(
            small=small,
            medium=medium,
            original=original,
        )

        image_thumbnails.additional_properties = d
        return image_thumbnails

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
