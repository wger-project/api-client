from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.trophy import Trophy


T = TypeVar("T", bound="TrophyProgress")


@_attrs_define
class TrophyProgress:
    """Serializer for trophy progress information.

    Used for showing progress on all trophies (earned and unearned).
    This is not a ModelSerializer as it aggregates data from multiple sources.

        Attributes:
            trophy (Trophy): Serializer for Trophy model.

                Shows trophy information for listing active trophies.
            is_earned (bool):
            earned_at (datetime.datetime | None):
            progress (float):
            current_value (None | str):
            target_value (None | str):
            progress_display (None | str):
    """

    trophy: Trophy
    is_earned: bool
    earned_at: datetime.datetime | None
    progress: float
    current_value: None | str
    target_value: None | str
    progress_display: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trophy = self.trophy.to_dict()

        is_earned = self.is_earned

        earned_at: None | str
        if isinstance(self.earned_at, datetime.datetime):
            earned_at = self.earned_at.isoformat()
        else:
            earned_at = self.earned_at

        progress = self.progress

        current_value: None | str
        current_value = self.current_value

        target_value: None | str
        target_value = self.target_value

        progress_display: None | str
        progress_display = self.progress_display

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trophy": trophy,
                "is_earned": is_earned,
                "earned_at": earned_at,
                "progress": progress,
                "current_value": current_value,
                "target_value": target_value,
                "progress_display": progress_display,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.trophy import Trophy

        d = dict(src_dict)
        trophy = Trophy.from_dict(d.pop("trophy"))

        is_earned = d.pop("is_earned")

        def _parse_earned_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                earned_at_type_0 = datetime.datetime.fromisoformat(data)

                return earned_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        earned_at = _parse_earned_at(d.pop("earned_at"))

        progress = d.pop("progress")

        def _parse_current_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        current_value = _parse_current_value(d.pop("current_value"))

        def _parse_target_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_value = _parse_target_value(d.pop("target_value"))

        def _parse_progress_display(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        progress_display = _parse_progress_display(d.pop("progress_display"))

        trophy_progress = cls(
            trophy=trophy,
            is_earned=is_earned,
            earned_at=earned_at,
            progress=progress,
            current_value=current_value,
            target_value=target_value,
            progress_display=progress_display,
        )

        trophy_progress.additional_properties = d
        return trophy_progress

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
