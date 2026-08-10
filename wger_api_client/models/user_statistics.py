from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="UserStatistics")


@_attrs_define
class UserStatistics:
    """Serializer for UserStatistics model.

    Shows user's trophy-related statistics.

        Attributes:
            id (int):
            total_weight_lifted (str): Cumulative weight lifted in kg
            total_workouts (int): Total number of workout sessions completed
            current_streak (int): Current consecutive days with workouts
            longest_streak (int): Longest consecutive days with workouts
            last_workout_date (datetime.date | None): Date of the most recent workout
            earliest_workout_time (None | str): Earliest time a workout was started
            latest_workout_time (None | str): Latest time a workout was started
            weekend_workout_streak (int): Consecutive weekends with workouts on both Saturday and Sunday
            last_complete_weekend_date (datetime.date | None): Date of the last Saturday where both Sat and Sun had workouts
            worked_out_jan_1 (bool): Whether user has ever worked out on January 1st
            last_updated (datetime.datetime):
    """

    id: int
    total_weight_lifted: str
    total_workouts: int
    current_streak: int
    longest_streak: int
    last_workout_date: datetime.date | None
    earliest_workout_time: None | str
    latest_workout_time: None | str
    weekend_workout_streak: int
    last_complete_weekend_date: datetime.date | None
    worked_out_jan_1: bool
    last_updated: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        total_weight_lifted = self.total_weight_lifted

        total_workouts = self.total_workouts

        current_streak = self.current_streak

        longest_streak = self.longest_streak

        last_workout_date: None | str
        if isinstance(self.last_workout_date, datetime.date):
            last_workout_date = self.last_workout_date.isoformat()
        else:
            last_workout_date = self.last_workout_date

        earliest_workout_time: None | str
        earliest_workout_time = self.earliest_workout_time

        latest_workout_time: None | str
        latest_workout_time = self.latest_workout_time

        weekend_workout_streak = self.weekend_workout_streak

        last_complete_weekend_date: None | str
        if isinstance(self.last_complete_weekend_date, datetime.date):
            last_complete_weekend_date = self.last_complete_weekend_date.isoformat()
        else:
            last_complete_weekend_date = self.last_complete_weekend_date

        worked_out_jan_1 = self.worked_out_jan_1

        last_updated = self.last_updated.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "total_weight_lifted": total_weight_lifted,
                "total_workouts": total_workouts,
                "current_streak": current_streak,
                "longest_streak": longest_streak,
                "last_workout_date": last_workout_date,
                "earliest_workout_time": earliest_workout_time,
                "latest_workout_time": latest_workout_time,
                "weekend_workout_streak": weekend_workout_streak,
                "last_complete_weekend_date": last_complete_weekend_date,
                "worked_out_jan_1": worked_out_jan_1,
                "last_updated": last_updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        total_weight_lifted = d.pop("total_weight_lifted")

        total_workouts = d.pop("total_workouts")

        current_streak = d.pop("current_streak")

        longest_streak = d.pop("longest_streak")

        def _parse_last_workout_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_workout_date_type_0 = datetime.date.fromisoformat(data)

                return last_workout_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        last_workout_date = _parse_last_workout_date(d.pop("last_workout_date"))

        def _parse_earliest_workout_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        earliest_workout_time = _parse_earliest_workout_time(
            d.pop("earliest_workout_time")
        )

        def _parse_latest_workout_time(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latest_workout_time = _parse_latest_workout_time(d.pop("latest_workout_time"))

        weekend_workout_streak = d.pop("weekend_workout_streak")

        def _parse_last_complete_weekend_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_complete_weekend_date_type_0 = datetime.date.fromisoformat(data)

                return last_complete_weekend_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        last_complete_weekend_date = _parse_last_complete_weekend_date(
            d.pop("last_complete_weekend_date")
        )

        worked_out_jan_1 = d.pop("worked_out_jan_1")

        last_updated = datetime.datetime.fromisoformat(d.pop("last_updated"))

        user_statistics = cls(
            id=id,
            total_weight_lifted=total_weight_lifted,
            total_workouts=total_workouts,
            current_streak=current_streak,
            longest_streak=longest_streak,
            last_workout_date=last_workout_date,
            earliest_workout_time=earliest_workout_time,
            latest_workout_time=latest_workout_time,
            weekend_workout_streak=weekend_workout_streak,
            last_complete_weekend_date=last_complete_weekend_date,
            worked_out_jan_1=worked_out_jan_1,
            last_updated=last_updated,
        )

        user_statistics.additional_properties = d
        return user_statistics

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
