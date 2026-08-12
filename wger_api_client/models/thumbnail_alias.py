from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.thumbnail_alias_settings import ThumbnailAliasSettings


T = TypeVar("T", bound="ThumbnailAlias")


@_attrs_define
class ThumbnailAlias:
    """One generated thumbnail: where it is and the size it was generated for.

    Attributes:
        url (str):
        settings (ThumbnailAliasSettings):
    """

    url: str
    settings: ThumbnailAliasSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.thumbnail_alias_settings import ThumbnailAliasSettings

        d = dict(src_dict)
        url = d.pop("url")

        settings = ThumbnailAliasSettings.from_dict(d.pop("settings"))

        thumbnail_alias = cls(
            url=url,
            settings=settings,
        )

        thumbnail_alias.additional_properties = d
        return thumbnail_alias

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
