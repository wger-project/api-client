from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedExerciseTranslationRequest")


@_attrs_define
class PatchedExerciseTranslationRequest:
    """Exercise translation serializer

    Attributes:
        name (str | Unset):
        exercise (int | Unset):
        description_source (str | Unset):
        language (int | Unset):
        license_author (str | Unset): If you are not the author, enter the name or source here.
    """

    name: str | Unset = UNSET
    exercise: int | Unset = UNSET
    description_source: str | Unset = UNSET
    language: int | Unset = UNSET
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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if exercise is not UNSET:
            field_dict["exercise"] = exercise
        if description_source is not UNSET:
            field_dict["description_source"] = description_source
        if language is not UNSET:
            field_dict["language"] = language
        if license_author is not UNSET:
            field_dict["license_author"] = license_author

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.exercise, Unset):
            files.append(
                ("exercise", (None, str(self.exercise).encode(), "text/plain"))
            )

        if not isinstance(self.description_source, Unset):
            files.append(
                (
                    "description_source",
                    (None, str(self.description_source).encode(), "text/plain"),
                )
            )

        if not isinstance(self.language, Unset):
            files.append(
                ("language", (None, str(self.language).encode(), "text/plain"))
            )

        if not isinstance(self.license_author, Unset):
            files.append(
                (
                    "license_author",
                    (None, str(self.license_author).encode(), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        exercise = d.pop("exercise", UNSET)

        description_source = d.pop("description_source", UNSET)

        language = d.pop("language", UNSET)

        license_author = d.pop("license_author", UNSET)

        patched_exercise_translation_request = cls(
            name=name,
            exercise=exercise,
            description_source=description_source,
            language=language,
            license_author=license_author,
        )

        patched_exercise_translation_request.additional_properties = d
        return patched_exercise_translation_request

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
