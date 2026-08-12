from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExerciseTranslation")


@_attrs_define
class ExerciseTranslation:
    """Exercise translation serializer

    Attributes:
        id (int):
        uuid (UUID):
        name (str):
        exercise (int):
        description (str):
        description_source (str):
        created (datetime.datetime):
        language (int):
        license_author (str | Unset): If you are not the author, enter the name or source here.
    """

    id: int
    uuid: UUID
    name: str
    exercise: int
    description: str
    description_source: str
    created: datetime.datetime
    language: int
    license_author: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = str(self.uuid)

        name = self.name

        exercise = self.exercise

        description = self.description

        description_source = self.description_source

        created = self.created.isoformat()

        language = self.language

        license_author = self.license_author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "name": name,
                "exercise": exercise,
                "description": description,
                "description_source": description_source,
                "created": created,
                "language": language,
            }
        )
        if license_author is not UNSET:
            field_dict["license_author"] = license_author

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        exercise = d.pop("exercise")

        description = d.pop("description")

        description_source = d.pop("description_source")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        language = d.pop("language")

        license_author = d.pop("license_author", UNSET)

        exercise_translation = cls(
            id=id,
            uuid=uuid,
            name=name,
            exercise=exercise,
            description=description,
            description_source=description_source,
            created=created,
            language=language,
            license_author=license_author,
        )

        exercise_translation.additional_properties = d
        return exercise_translation

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
