from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DynamicType")


@_attrs_define
class DynamicType:
    """One calculated category type of the registry. Read-only: the registry is
    code, there is nothing to write back.

        Attributes:
            value (str):
            label (str):
            params_schema (Any):
    """

    value: str
    label: str
    params_schema: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        label = self.label

        params_schema = self.params_schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "label": label,
                "params_schema": params_schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value")

        label = d.pop("label")

        params_schema = d.pop("params_schema")

        dynamic_type = cls(
            value=value,
            label=label,
            params_schema=params_schema,
        )

        dynamic_type.additional_properties = d
        return dynamic_type

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
