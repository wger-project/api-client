from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.log_data_exercises import LogDataExercises
    from ..models.log_data_muscle import LogDataMuscle


T = TypeVar("T", bound="LogData")


@_attrs_define
class LogData:
    """Log Stats Data serializer

    Attributes:
        exercises (LogDataExercises):
        muscle (LogDataMuscle):
        upper_body (str):
        lower_body (str):
        total (str):
    """

    exercises: LogDataExercises
    muscle: LogDataMuscle
    upper_body: str
    lower_body: str
    total: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercises = self.exercises.to_dict()

        muscle = self.muscle.to_dict()

        upper_body = self.upper_body

        lower_body = self.lower_body

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exercises": exercises,
                "muscle": muscle,
                "upper_body": upper_body,
                "lower_body": lower_body,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.log_data_exercises import LogDataExercises
        from ..models.log_data_muscle import LogDataMuscle

        d = dict(src_dict)
        exercises = LogDataExercises.from_dict(d.pop("exercises"))

        muscle = LogDataMuscle.from_dict(d.pop("muscle"))

        upper_body = d.pop("upper_body")

        lower_body = d.pop("lower_body")

        total = d.pop("total")

        log_data = cls(
            exercises=exercises,
            muscle=muscle,
            upper_body=upper_body,
            lower_body=lower_body,
            total=total,
        )

        log_data.additional_properties = d
        return log_data

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
