from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.trophy import Trophy


T = TypeVar("T", bound="UserTrophy")


@_attrs_define
class UserTrophy:
    """Serializer for UserTrophy model.

    Shows user's earned trophies with trophy details.

        Attributes:
            id (int):
            trophy (Trophy): Serializer for Trophy model.

                Shows trophy information for listing active trophies.
            earned_at (datetime.datetime): When the trophy was earned
            progress (float): Progress towards earning the trophy (0-100)
            is_notified (bool): Whether the user has been notified about earning this trophy
            context_data (Any): Additional information concerning this trophy
    """

    id: int
    trophy: Trophy
    earned_at: datetime.datetime
    progress: float
    is_notified: bool
    context_data: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        trophy = self.trophy.to_dict()

        earned_at = self.earned_at.isoformat()

        progress = self.progress

        is_notified = self.is_notified

        context_data = self.context_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "trophy": trophy,
                "earned_at": earned_at,
                "progress": progress,
                "is_notified": is_notified,
                "context_data": context_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.trophy import Trophy

        d = dict(src_dict)
        id = d.pop("id")

        trophy = Trophy.from_dict(d.pop("trophy"))

        earned_at = datetime.datetime.fromisoformat(d.pop("earned_at"))

        progress = d.pop("progress")

        is_notified = d.pop("is_notified")

        context_data = d.pop("context_data")

        user_trophy = cls(
            id=id,
            trophy=trophy,
            earned_at=earned_at,
            progress=progress,
            is_notified=is_notified,
            context_data=context_data,
        )

        user_trophy.additional_properties = d
        return user_trophy

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
