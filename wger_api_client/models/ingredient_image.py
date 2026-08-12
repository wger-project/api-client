from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngredientImage")


@_attrs_define
class IngredientImage:
    """Image serializer

    Attributes:
        id (int):
        uuid (UUID):
        ingredient_id (int | None):
        ingredient_uuid (str):
        image (str): Only PNG and JPEG formats are supported
        created (datetime.datetime):
        last_update (datetime.datetime):
        size (int):
        width (int):
        height (int):
        license_ (int | Unset):
        license_title (str | Unset):
        license_object_url (str | Unset):
        license_author (str | Unset): If you are not the author, enter the name or source here.
        license_author_url (str | Unset):
        license_derivative_source_url (str | Unset): Note that a derivative work is one which is not only based on a
            previous work, but which also contains sufficient new, creative content to entitle it to its own copyright.
    """

    id: int
    uuid: UUID
    ingredient_id: int | None
    ingredient_uuid: str
    image: str
    created: datetime.datetime
    last_update: datetime.datetime
    size: int
    width: int
    height: int
    license_: int | Unset = UNSET
    license_title: str | Unset = UNSET
    license_object_url: str | Unset = UNSET
    license_author: str | Unset = UNSET
    license_author_url: str | Unset = UNSET
    license_derivative_source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = str(self.uuid)

        ingredient_id: int | None
        ingredient_id = self.ingredient_id

        ingredient_uuid = self.ingredient_uuid

        image = self.image

        created = self.created.isoformat()

        last_update = self.last_update.isoformat()

        size = self.size

        width = self.width

        height = self.height

        license_ = self.license_

        license_title = self.license_title

        license_object_url: str | Unset
        if isinstance(self.license_object_url, Unset):
            license_object_url = UNSET
        else:
            license_object_url = self.license_object_url

        license_author = self.license_author

        license_author_url: str | Unset
        if isinstance(self.license_author_url, Unset):
            license_author_url = UNSET
        else:
            license_author_url = self.license_author_url

        license_derivative_source_url: str | Unset
        if isinstance(self.license_derivative_source_url, Unset):
            license_derivative_source_url = UNSET
        else:
            license_derivative_source_url = self.license_derivative_source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "ingredient_id": ingredient_id,
                "ingredient_uuid": ingredient_uuid,
                "image": image,
                "created": created,
                "last_update": last_update,
                "size": size,
                "width": width,
                "height": height,
            }
        )
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_title is not UNSET:
            field_dict["license_title"] = license_title
        if license_object_url is not UNSET:
            field_dict["license_object_url"] = license_object_url
        if license_author is not UNSET:
            field_dict["license_author"] = license_author
        if license_author_url is not UNSET:
            field_dict["license_author_url"] = license_author_url
        if license_derivative_source_url is not UNSET:
            field_dict["license_derivative_source_url"] = license_derivative_source_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        def _parse_ingredient_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ingredient_id = _parse_ingredient_id(d.pop("ingredient_id"))

        ingredient_uuid = d.pop("ingredient_uuid")

        image = d.pop("image")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        last_update = datetime.datetime.fromisoformat(d.pop("last_update"))

        size = d.pop("size")

        width = d.pop("width")

        height = d.pop("height")

        license_ = d.pop("license", UNSET)

        license_title = d.pop("license_title", UNSET)

        def _parse_license_object_url(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        license_object_url = _parse_license_object_url(
            d.pop("license_object_url", UNSET)
        )

        license_author = d.pop("license_author", UNSET)

        def _parse_license_author_url(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        license_author_url = _parse_license_author_url(
            d.pop("license_author_url", UNSET)
        )

        def _parse_license_derivative_source_url(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        license_derivative_source_url = _parse_license_derivative_source_url(
            d.pop("license_derivative_source_url", UNSET)
        )

        ingredient_image = cls(
            id=id,
            uuid=uuid,
            ingredient_id=ingredient_id,
            ingredient_uuid=ingredient_uuid,
            image=image,
            created=created,
            last_update=last_update,
            size=size,
            width=width,
            height=height,
            license_=license_,
            license_title=license_title,
            license_object_url=license_object_url,
            license_author=license_author,
            license_author_url=license_author_url,
            license_derivative_source_url=license_derivative_source_url,
        )

        ingredient_image.additional_properties = d
        return ingredient_image

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
