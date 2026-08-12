from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExerciseSubmissionAliasRequest")


@_attrs_define
class ExerciseSubmissionAliasRequest:
    """Alias serializer without ``translation``, for use inside a submission.

    A subclass rather than a modified instance of the parent: both would be named
    ExerciseAlias in the schema, and the narrower one would win for the alias
    endpoint too.

        Attributes:
            alias (str):
    """

    alias: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alias": alias,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        alias = d.pop("alias")

        exercise_submission_alias_request = cls(
            alias=alias,
        )

        exercise_submission_alias_request.additional_properties = d
        return exercise_submission_alias_request

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
