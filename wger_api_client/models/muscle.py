from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Muscle")


@_attrs_define
class Muscle:
    """Muscle serializer

    Attributes:
        id (int):
        name (str): In latin, e.g. "Pectoralis major"
        image_url_main (None | str): Absolute URL to the main muscle image
        image_url_secondary (None | str): Absolute URL to the secondary muscle image
        name_en (str | Unset): A more basic name for the muscle
        is_front (bool | Unset):
    """

    id: int
    name: str
    image_url_main: None | str
    image_url_secondary: None | str
    name_en: str | Unset = UNSET
    is_front: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        image_url_main: None | str
        image_url_main = self.image_url_main

        image_url_secondary: None | str
        image_url_secondary = self.image_url_secondary

        name_en = self.name_en

        is_front = self.is_front

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "image_url_main": image_url_main,
                "image_url_secondary": image_url_secondary,
            }
        )
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if is_front is not UNSET:
            field_dict["is_front"] = is_front

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_image_url_main(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url_main = _parse_image_url_main(d.pop("image_url_main"))

        def _parse_image_url_secondary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image_url_secondary = _parse_image_url_secondary(d.pop("image_url_secondary"))

        name_en = d.pop("name_en", UNSET)

        is_front = d.pop("is_front", UNSET)

        muscle = cls(
            id=id,
            name=name,
            image_url_main=image_url_main,
            image_url_secondary=image_url_secondary,
            name_en=name_en,
            is_front=is_front,
        )

        muscle.additional_properties = d
        return muscle

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
