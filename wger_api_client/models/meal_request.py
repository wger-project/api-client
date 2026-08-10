from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="MealRequest")


@_attrs_define
class MealRequest:
    """Meal serializer

    Attributes:
        plan (UUID):
        id (UUID | Unset):
        time (None | str | Unset):
        name (str | Unset): Give meals a textual description / name such as "Breakfast" or "after workout"
    """

    plan: UUID
    id: UUID | Unset = UNSET
    time: None | str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = str(self.plan)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if time is not UNSET:
            field_dict["time"] = time
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("plan", (None, str(self.plan), "text/plain")))

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id), "text/plain")))

        if not isinstance(self.time, Unset):
            if isinstance(self.time, str):
                files.append(("time", (None, str(self.time).encode(), "text/plain")))
            else:
                files.append(("time", (None, str(self.time).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        plan = UUID(d.pop("plan"))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        time = _parse_time(d.pop("time", UNSET))

        name = d.pop("name", UNSET)

        meal_request = cls(
            plan=plan,
            id=id,
            time=time,
            name=name,
        )

        meal_request.additional_properties = d
        return meal_request

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
