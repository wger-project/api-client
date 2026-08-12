from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workout_log import WorkoutLog
    from ..models.workout_session import WorkoutSession


T = TypeVar("T", bound="LogDisplay")


@_attrs_define
class LogDisplay:
    """Log Display Data serializer

    Attributes:
        session (WorkoutSession): Workout session serializer
        logs (list[WorkoutLog]):
    """

    session: WorkoutSession
    logs: list[WorkoutLog]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session = self.session.to_dict()

        logs = []
        for logs_item_data in self.logs:
            logs_item = logs_item_data.to_dict()
            logs.append(logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "session": session,
                "logs": logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workout_log import WorkoutLog
        from ..models.workout_session import WorkoutSession

        d = dict(src_dict)
        session = WorkoutSession.from_dict(d.pop("session"))

        logs = []
        _logs = d.pop("logs")
        for logs_item_data in _logs:
            logs_item = WorkoutLog.from_dict(logs_item_data)

            logs.append(logs_item)

        log_display = cls(
            session=session,
            logs=logs,
        )

        log_display.additional_properties = d
        return log_display

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
