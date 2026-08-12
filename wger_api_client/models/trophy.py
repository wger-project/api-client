from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trophy_type_enum import TrophyTypeEnum, check_trophy_type_enum

T = TypeVar("T", bound="Trophy")


@_attrs_define
class Trophy:
    """Serializer for Trophy model.

    Shows trophy information for listing active trophies.

        Attributes:
            id (int):
            uuid (UUID):
            name (str): Translate the trophy name
            description (str): Translate the trophy description
            image (None | str): Build absolute URL to trophy image, if possible.
            trophy_type (TrophyTypeEnum): * `time` - Time-based
                * `volume` - Volume-based
                * `count` - Count-based
                * `sequence` - Sequence-based
                * `date` - Date-based
                * `pr` - Personal Record
                * `other` - Other
            is_hidden (bool): If true, this trophy is hidden until earned
            is_progressive (bool): If true, this trophy shows progress towards completion
            is_repeatable (bool): If true, this trophy can be earned multiple times
            order (int): Display order of the trophy
    """

    id: int
    uuid: UUID
    name: str
    description: str
    image: None | str
    trophy_type: TrophyTypeEnum
    is_hidden: bool
    is_progressive: bool
    is_repeatable: bool
    order: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = str(self.uuid)

        name = self.name

        description = self.description

        image: None | str
        image = self.image

        trophy_type: str = self.trophy_type

        is_hidden = self.is_hidden

        is_progressive = self.is_progressive

        is_repeatable = self.is_repeatable

        order = self.order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "name": name,
                "description": description,
                "image": image,
                "trophy_type": trophy_type,
                "is_hidden": is_hidden,
                "is_progressive": is_progressive,
                "is_repeatable": is_repeatable,
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        description = d.pop("description")

        def _parse_image(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        image = _parse_image(d.pop("image"))

        trophy_type = check_trophy_type_enum(d.pop("trophy_type"))

        is_hidden = d.pop("is_hidden")

        is_progressive = d.pop("is_progressive")

        is_repeatable = d.pop("is_repeatable")

        order = d.pop("order")

        trophy = cls(
            id=id,
            uuid=uuid,
            name=name,
            description=description,
            image=image,
            trophy_type=trophy_type,
            is_hidden=is_hidden,
            is_progressive=is_progressive,
            is_repeatable=is_repeatable,
            order=order,
        )

        trophy.additional_properties = d
        return trophy

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
