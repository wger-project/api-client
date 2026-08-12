from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.day_type_enum import DayTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Day")


@_attrs_define
class Day:
    """Day serializer

    Attributes:
        id (int):
        routine (int):
        order (int | Unset):
        name (str | Unset):
        description (str | Unset):
        is_rest (bool | Unset):
        need_logs_to_advance (bool | Unset):
        type_ (DayTypeEnum | Unset): * `custom` - Custom
            * `enom` - Enom
            * `amrap` - Amrap
            * `hiit` - Hiit
            * `tabata` - Tabata
            * `edt` - Edt
            * `rft` - Rft
            * `afap` - Afap
        config (Any | Unset):
    """

    id: int
    routine: int
    order: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    is_rest: bool | Unset = UNSET
    need_logs_to_advance: bool | Unset = UNSET
    type_: DayTypeEnum | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        routine = self.routine

        order = self.order

        name = self.name

        description = self.description

        is_rest = self.is_rest

        need_logs_to_advance = self.need_logs_to_advance

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "routine": routine,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_rest is not UNSET:
            field_dict["is_rest"] = is_rest
        if need_logs_to_advance is not UNSET:
            field_dict["need_logs_to_advance"] = need_logs_to_advance
        if type_ is not UNSET:
            field_dict["type"] = type_
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        routine = d.pop("routine")

        order = d.pop("order", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_rest = d.pop("is_rest", UNSET)

        need_logs_to_advance = d.pop("need_logs_to_advance", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: DayTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DayTypeEnum(_type_)

        config = d.pop("config", UNSET)

        day = cls(
            id=id,
            routine=routine,
            order=order,
            name=name,
            description=description,
            is_rest=is_rest,
            need_logs_to_advance=need_logs_to_advance,
            type_=type_,
            config=config,
        )

        day.additional_properties = d
        return day

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
