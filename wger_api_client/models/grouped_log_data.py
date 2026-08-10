from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.grouped_log_data_daily import GroupedLogDataDaily
    from ..models.grouped_log_data_iteration import GroupedLogDataIteration
    from ..models.grouped_log_data_weekly import GroupedLogDataWeekly
    from ..models.log_data import LogData


T = TypeVar("T", bound="GroupedLogData")


@_attrs_define
class GroupedLogData:
    """Log Stats Data serializer

    Attributes:
        iteration (GroupedLogDataIteration):
        weekly (GroupedLogDataWeekly):
        daily (GroupedLogDataDaily):
        mesocycle (LogData): Log Stats Data serializer
    """

    iteration: GroupedLogDataIteration
    weekly: GroupedLogDataWeekly
    daily: GroupedLogDataDaily
    mesocycle: LogData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iteration = self.iteration.to_dict()

        weekly = self.weekly.to_dict()

        daily = self.daily.to_dict()

        mesocycle = self.mesocycle.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iteration": iteration,
                "weekly": weekly,
                "daily": daily,
                "mesocycle": mesocycle,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grouped_log_data_daily import GroupedLogDataDaily
        from ..models.grouped_log_data_iteration import GroupedLogDataIteration
        from ..models.grouped_log_data_weekly import GroupedLogDataWeekly
        from ..models.log_data import LogData

        d = dict(src_dict)
        iteration = GroupedLogDataIteration.from_dict(d.pop("iteration"))

        weekly = GroupedLogDataWeekly.from_dict(d.pop("weekly"))

        daily = GroupedLogDataDaily.from_dict(d.pop("daily"))

        mesocycle = LogData.from_dict(d.pop("mesocycle"))

        grouped_log_data = cls(
            iteration=iteration,
            weekly=weekly,
            daily=daily,
            mesocycle=mesocycle,
        )

        grouped_log_data.additional_properties = d
        return grouped_log_data

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
