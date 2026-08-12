from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanguageCheckRequest")


@_attrs_define
class LanguageCheckRequest:
    """Serializer for language check

    Attributes:
        input_ (str):
        language (int | Unset):
        language_code (str | Unset):
    """

    input_: str
    language: int | Unset = UNSET
    language_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_

        language = self.language

        language_code = self.language_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if language_code is not UNSET:
            field_dict["language_code"] = language_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        input_ = d.pop("input")

        language = d.pop("language", UNSET)

        language_code = d.pop("language_code", UNSET)

        language_check_request = cls(
            input_=input_,
            language=language,
            language_code=language_code,
        )

        language_check_request.additional_properties = d
        return language_check_request

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
