from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Image")


@_attrs_define
class Image:
    """Exercise serializer

    Attributes:
        id (int):
        date (datetime.date):
        image (str): Only PNG and JPEG formats are supported
        height (int):
        width (int):
        description (str | Unset):
    """

    id: int
    date: datetime.date
    image: str
    height: int
    width: int
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        image = self.image

        height = self.height

        width = self.width

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "image": image,
                "height": height,
                "width": width,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        date = datetime.date.fromisoformat(d.pop("date"))

        image = d.pop("image")

        height = d.pop("height")

        width = d.pop("width")

        description = d.pop("description", UNSET)

        image = cls(
            id=id,
            date=date,
            image=image,
            height=height,
            width=width,
            description=description,
        )

        image.additional_properties = d
        return image

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
