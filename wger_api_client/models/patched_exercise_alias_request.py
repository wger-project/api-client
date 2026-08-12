from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedExerciseAliasRequest")


@_attrs_define
class PatchedExerciseAliasRequest:
    """ExerciseAlias serializer

    Attributes:
        translation (int | Unset):
        alias (str | Unset):
    """

    translation: int | Unset = UNSET
    alias: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        translation = self.translation

        alias = self.alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if translation is not UNSET:
            field_dict["translation"] = translation
        if alias is not UNSET:
            field_dict["alias"] = alias

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        translation = d.pop("translation", UNSET)

        alias = d.pop("alias", UNSET)

        patched_exercise_alias_request = cls(
            translation=translation,
            alias=alias,
        )

        patched_exercise_alias_request.additional_properties = d
        return patched_exercise_alias_request

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
