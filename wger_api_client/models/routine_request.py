from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutineRequest")


@_attrs_define
class RoutineRequest:
    """Routine serializer

    Attributes:
        start (datetime.date):
        end (datetime.date):
        name (str | Unset):
        description (str | Unset):
        fit_in_week (bool | Unset):
        is_template (bool | Unset): Marking a workout as a template will freeze it and allow you to make copies of it
        is_public (bool | Unset): A public template is available to other users
    """

    start: datetime.date
    end: datetime.date
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    fit_in_week: bool | Unset = UNSET
    is_template: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start.isoformat()

        end = self.end.isoformat()

        name = self.name

        description = self.description

        fit_in_week = self.fit_in_week

        is_template = self.is_template

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if fit_in_week is not UNSET:
            field_dict["fit_in_week"] = fit_in_week
        if is_template is not UNSET:
            field_dict["is_template"] = is_template
        if is_public is not UNSET:
            field_dict["is_public"] = is_public

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("start", (None, self.start.isoformat().encode(), "text/plain")))

        files.append(("end", (None, self.end.isoformat().encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            files.append(
                ("description", (None, str(self.description).encode(), "text/plain"))
            )

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
        start = datetime.date.fromisoformat(d.pop("start"))

        end = datetime.date.fromisoformat(d.pop("end"))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        fit_in_week = d.pop("fit_in_week", UNSET)

        is_template = d.pop("is_template", UNSET)

        is_public = d.pop("is_public", UNSET)

        routine_request = cls(
            start=start,
            end=end,
            name=name,
            description=description,
            fit_in_week=fit_in_week,
            is_template=is_template,
            is_public=is_public,
        )

        routine_request.additional_properties = d
        return routine_request

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
