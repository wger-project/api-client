from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPowersyncUploadRequest")


@_attrs_define
class PatchedPowersyncUploadRequest:
    """
    Attributes:
        table (str | Unset):
        data (Any | Unset):
    """

    table: str | Unset = UNSET
    data: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table

        data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table is not UNSET:
            field_dict["table"] = table
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.table, Unset):
            files.append(("table", (None, str(self.table).encode(), "text/plain")))

        if not isinstance(self.data, Unset):
            files.append(("data", (None, str(self.data).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        table = d.pop("table", UNSET)

        data = d.pop("data", UNSET)

        patched_powersync_upload_request = cls(
            table=table,
            data=data,
        )

        patched_powersync_upload_request.additional_properties = d
        return patched_powersync_upload_request

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
