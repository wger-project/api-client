from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.grouped_log_data import GroupedLogData


T = TypeVar("T", bound="LogStatsData")


@_attrs_define
class LogStatsData:
    """Log Stats Data serializer

    Attributes:
        intensity (GroupedLogData): Log Stats Data serializer
        sets (GroupedLogData): Log Stats Data serializer
        volume (GroupedLogData): Log Stats Data serializer
    """

    intensity: GroupedLogData
    sets: GroupedLogData
    volume: GroupedLogData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        intensity = self.intensity.to_dict()

        sets = self.sets.to_dict()

        volume = self.volume.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "intensity": intensity,
                "sets": sets,
                "volume": volume,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grouped_log_data import GroupedLogData

        d = dict(src_dict)
        intensity = GroupedLogData.from_dict(d.pop("intensity"))

        sets = GroupedLogData.from_dict(d.pop("sets"))

        volume = GroupedLogData.from_dict(d.pop("volume"))

        log_stats_data = cls(
            intensity=intensity,
            sets=sets,
            volume=volume,
        )

        log_stats_data.additional_properties = d
        return log_stats_data

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
