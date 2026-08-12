from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExerciseTranslationRequest")


@_attrs_define
class ExerciseTranslationRequest:
    """Exercise translation serializer

    Attributes:
        name (str):
        exercise (int):
        description_source (str):
        language (int):
        license_author (str | Unset): If you are not the author, enter the name or source here.
    """

    name: str
    exercise: int
    description_source: str
    language: int
    license_author: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        exercise = self.exercise

        description_source = self.description_source

        language = self.language

        license_author = self.license_author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "exercise": exercise,
                "description_source": description_source,
                "language": language,
            }
        )
        if license_author is not UNSET:
            field_dict["license_author"] = license_author

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        exercise = d.pop("exercise")

        description_source = d.pop("description_source")

        language = d.pop("language")

        license_author = d.pop("license_author", UNSET)

        exercise_translation_request = cls(
            name=name,
            exercise=exercise,
            description_source=description_source,
            language=language,
            license_author=license_author,
        )

        exercise_translation_request.additional_properties = d
        return exercise_translation_request

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
