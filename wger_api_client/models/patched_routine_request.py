from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRoutineRequest")


@_attrs_define
class PatchedRoutineRequest:
    """Routine serializer

    Attributes:
        name (str | Unset):
        description (str | Unset):
        start (datetime.date | Unset):
        end (datetime.date | Unset):
        fit_in_week (bool | Unset):
        is_template (bool | Unset): Marking a workout as a template will freeze it and allow you to make copies of it
        is_public (bool | Unset): A public template is available to other users
    """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    start: datetime.date | Unset = UNSET
    end: datetime.date | Unset = UNSET
    fit_in_week: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        fit_in_week = self.fit_in_week

        is_template = self.is_template

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if fit_in_week is not UNSET:
            field_dict["fit_in_week"] = fit_in_week
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if is_public is not UNSET:
            field_dict["is_public"] = is_public

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(
                ("description", (None, str(self.description).encode(), "text/plain"))
            )

        if not isinstance(self.start, Unset):
            files.append(
                ("start", (None, self.start.isoformat().encode(), "text/plain"))
            )

        if not isinstance(self.end, Unset):
            files.append(("end", (None, self.end.isoformat().encode(), "text/plain")))

        if not isinstance(self.fit_in_week, Unset):
            files.append(
                ("fit_in_week", (None, str(self.fit_in_week).encode(), "text/plain"))
            )

        if not isinstance(self.is_template, Unset):
            files.append(
                ("is_template", (None, str(self.is_template).encode(), "text/plain"))
            )

        if not isinstance(self.is_public, Unset):
            files.append(
                ("is_public", (None, str(self.is_public).encode(), "text/plain"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.date | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = datetime.date.fromisoformat(_start)

        _end = d.pop("end", UNSET)
        end: datetime.date | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = datetime.date.fromisoformat(_end)

        fit_in_week = d.pop("fit_in_week", UNSET)

        is_template = d.pop("is_template", UNSET)

        is_public = d.pop("is_public", UNSET)

        patched_routine_request = cls(
            name=name,
            description=description,
            start=start,
            end=end,
            fit_in_week=fit_in_week,
            is_template=is_template,
            is_public=is_public,
        )

        patched_routine_request.additional_properties = d
        return patched_routine_request

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
