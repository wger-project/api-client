from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.log_data import LogData


T = TypeVar("T", bound="GroupedLogDataWeekly")


@_attrs_define
class GroupedLogDataWeekly:
    """ """

    additional_properties: dict[str, LogData] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.log_data import LogData

        d = dict(src_dict)
        grouped_log_data_weekly = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = LogData.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        grouped_log_data_weekly.additional_properties = additional_properties
        return grouped_log_data_weekly

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> LogData:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: LogData) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
