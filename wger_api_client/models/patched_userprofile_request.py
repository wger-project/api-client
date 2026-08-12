from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gender_enum import GenderEnum, check_gender_enum
from ..models.intensity_enum import IntensityEnum, check_intensity_enum
from ..models.weight_unit_enum import WeightUnitEnum, check_weight_unit_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUserprofileRequest")


@_attrs_define
class PatchedUserprofileRequest:
    """Workout session serializer

    Attributes:
        weight_rounding (None | str | Unset):
        repetitions_rounding (None | str | Unset):
        workout_reminder_active (bool | Unset): Check to activate automatic reminders for workouts. You need to provide
            a valid email for this to work.
        workout_reminder (int | Unset): The number of days you want to be reminded before a workout expires.
        workout_duration (int | Unset): Default duration in weeks of workouts not in a schedule. Used for email workout
            reminders.
        notification_language (int | Unset): Language to use when sending you email notifications, e.g. email reminders
            for workouts. This does not affect the language used on the website.
        age (int | None | Unset):
        birthdate (datetime.date | None | Unset):
        height (int | None | Unset):
        gender (GenderEnum | None | Unset):
        sleep_hours (int | None | Unset): The average hours of sleep per day
        work_hours (int | None | Unset): Average hours per day
        work_intensity (IntensityEnum | None | Unset): Approximately

            * `1` - Low
            * `2` - Medium
            * `3` - High
        sport_hours (int | None | Unset): Average hours per week
        sport_intensity (IntensityEnum | None | Unset): Approximately

            * `1` - Low
            * `2` - Medium
            * `3` - High
        freetime_hours (int | None | Unset): Average hours per day
        freetime_intensity (IntensityEnum | None | Unset): Approximately

            * `1` - Low
            * `2` - Medium
            * `3` - High
        calories (int | None | Unset): Total caloric intake, including e.g. any surplus
        weight_unit (WeightUnitEnum | Unset): * `kg` - Metric (kilogram)
            * `lb` - Imperial (pound)
        num_days_weight_reminder (int | Unset): Number of days after the last weight entry (enter 0 to deactivate)
    """

    weight_rounding: None | str | Unset = UNSET
    repetitions_rounding: None | str | Unset = UNSET
    workout_reminder_active: bool | Unset = UNSET
    workout_reminder: int | Unset = UNSET
    workout_duration: int | Unset = UNSET
    notification_language: int | Unset = UNSET
    age: int | None | Unset = UNSET
    birthdate: datetime.date | None | Unset = UNSET
    height: int | None | Unset = UNSET
    gender: GenderEnum | None | Unset = UNSET
    sleep_hours: int | None | Unset = UNSET
    work_hours: int | None | Unset = UNSET
    work_intensity: IntensityEnum | None | Unset = UNSET
    sport_hours: int | None | Unset = UNSET
    sport_intensity: IntensityEnum | None | Unset = UNSET
    freetime_hours: int | None | Unset = UNSET
    freetime_intensity: IntensityEnum | None | Unset = UNSET
    calories: int | None | Unset = UNSET
    weight_unit: WeightUnitEnum | Unset = UNSET
    num_days_weight_reminder: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight_rounding: None | str | Unset
        if isinstance(self.weight_rounding, Unset):
            weight_rounding = UNSET
        else:
            weight_rounding = self.weight_rounding

        repetitions_rounding: None | str | Unset
        if isinstance(self.repetitions_rounding, Unset):
            repetitions_rounding = UNSET
        else:
            repetitions_rounding = self.repetitions_rounding

        workout_reminder_active = self.workout_reminder_active

        workout_reminder = self.workout_reminder

        workout_duration = self.workout_duration

        notification_language = self.notification_language

        age: int | None | Unset
        if isinstance(self.age, Unset):
            age = UNSET
        else:
            age = self.age

        birthdate: None | str | Unset
        if isinstance(self.birthdate, Unset):
            birthdate = UNSET
        elif isinstance(self.birthdate, datetime.date):
            birthdate = self.birthdate.isoformat()
        else:
            birthdate = self.birthdate

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        elif isinstance(self.gender, str):
            gender = self.gender
        else:
            gender = self.gender

        sleep_hours: int | None | Unset
        if isinstance(self.sleep_hours, Unset):
            sleep_hours = UNSET
        else:
            sleep_hours = self.sleep_hours

        work_hours: int | None | Unset
        if isinstance(self.work_hours, Unset):
            work_hours = UNSET
        else:
            work_hours = self.work_hours

        work_intensity: None | str | Unset
        if isinstance(self.work_intensity, Unset):
            work_intensity = UNSET
        elif isinstance(self.work_intensity, str):
            work_intensity = self.work_intensity
        else:
            work_intensity = self.work_intensity

        sport_hours: int | None | Unset
        if isinstance(self.sport_hours, Unset):
            sport_hours = UNSET
        else:
            sport_hours = self.sport_hours

        sport_intensity: None | str | Unset
        if isinstance(self.sport_intensity, Unset):
            sport_intensity = UNSET
        elif isinstance(self.sport_intensity, str):
            sport_intensity = self.sport_intensity
        else:
            sport_intensity = self.sport_intensity

        freetime_hours: int | None | Unset
        if isinstance(self.freetime_hours, Unset):
            freetime_hours = UNSET
        else:
            freetime_hours = self.freetime_hours

        freetime_intensity: None | str | Unset
        if isinstance(self.freetime_intensity, Unset):
            freetime_intensity = UNSET
        elif isinstance(self.freetime_intensity, str):
            freetime_intensity = self.freetime_intensity
        else:
            freetime_intensity = self.freetime_intensity

        calories: int | None | Unset
        if isinstance(self.calories, Unset):
            calories = UNSET
        else:
            calories = self.calories

        weight_unit: str | Unset = UNSET
        if not isinstance(self.weight_unit, Unset):
            weight_unit = self.weight_unit

        num_days_weight_reminder = self.num_days_weight_reminder

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight_rounding is not UNSET:
            field_dict["weight_rounding"] = weight_rounding
        if repetitions_rounding is not UNSET:
            field_dict["repetitions_rounding"] = repetitions_rounding
        if workout_reminder_active is not UNSET:
            field_dict["workout_reminder_active"] = workout_reminder_active
        if workout_reminder is not UNSET:
            field_dict["workout_reminder"] = workout_reminder
        if workout_duration is not UNSET:
            field_dict["workout_duration"] = workout_duration
        if notification_language is not UNSET:
            field_dict["notification_language"] = notification_language
        if age is not UNSET:
            field_dict["age"] = age
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if height is not UNSET:
            field_dict["height"] = height
        if gender is not UNSET:
            field_dict["gender"] = gender
        if sleep_hours is not UNSET:
            field_dict["sleep_hours"] = sleep_hours
        if work_hours is not UNSET:
            field_dict["work_hours"] = work_hours
        if work_intensity is not UNSET:
            field_dict["work_intensity"] = work_intensity
        if sport_hours is not UNSET:
            field_dict["sport_hours"] = sport_hours
        if sport_intensity is not UNSET:
            field_dict["sport_intensity"] = sport_intensity
        if freetime_hours is not UNSET:
            field_dict["freetime_hours"] = freetime_hours
        if freetime_intensity is not UNSET:
            field_dict["freetime_intensity"] = freetime_intensity
        if calories is not UNSET:
            field_dict["calories"] = calories
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if num_days_weight_reminder is not UNSET:
            field_dict["num_days_weight_reminder"] = num_days_weight_reminder

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_weight_rounding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weight_rounding = _parse_weight_rounding(d.pop("weight_rounding", UNSET))

        def _parse_repetitions_rounding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repetitions_rounding = _parse_repetitions_rounding(
            d.pop("repetitions_rounding", UNSET)
        )

        workout_reminder_active = d.pop("workout_reminder_active", UNSET)

        workout_reminder = d.pop("workout_reminder", UNSET)

        workout_duration = d.pop("workout_duration", UNSET)

        notification_language = d.pop("notification_language", UNSET)

        def _parse_age(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        age = _parse_age(d.pop("age", UNSET))

        def _parse_birthdate(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birthdate_type_0 = datetime.date.fromisoformat(data)

                return birthdate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        birthdate = _parse_birthdate(d.pop("birthdate", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_gender(data: object) -> GenderEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gender_type_0 = check_gender_enum(data)

                return gender_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenderEnum | None | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_sleep_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sleep_hours = _parse_sleep_hours(d.pop("sleep_hours", UNSET))

        def _parse_work_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        work_hours = _parse_work_hours(d.pop("work_hours", UNSET))

        def _parse_work_intensity(data: object) -> IntensityEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                work_intensity_type_0 = check_intensity_enum(data)

                return work_intensity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IntensityEnum | None | Unset, data)

        work_intensity = _parse_work_intensity(d.pop("work_intensity", UNSET))

        def _parse_sport_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sport_hours = _parse_sport_hours(d.pop("sport_hours", UNSET))

        def _parse_sport_intensity(data: object) -> IntensityEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sport_intensity_type_0 = check_intensity_enum(data)

                return sport_intensity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IntensityEnum | None | Unset, data)

        sport_intensity = _parse_sport_intensity(d.pop("sport_intensity", UNSET))

        def _parse_freetime_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        freetime_hours = _parse_freetime_hours(d.pop("freetime_hours", UNSET))

        def _parse_freetime_intensity(data: object) -> IntensityEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                freetime_intensity_type_0 = check_intensity_enum(data)

                return freetime_intensity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IntensityEnum | None | Unset, data)

        freetime_intensity = _parse_freetime_intensity(
            d.pop("freetime_intensity", UNSET)
        )

        def _parse_calories(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        calories = _parse_calories(d.pop("calories", UNSET))

        _weight_unit = d.pop("weight_unit", UNSET)
        weight_unit: WeightUnitEnum | Unset
        if isinstance(_weight_unit, Unset):
            weight_unit = UNSET
        else:
            weight_unit = check_weight_unit_enum(_weight_unit)

        num_days_weight_reminder = d.pop("num_days_weight_reminder", UNSET)

        patched_userprofile_request = cls(
            weight_rounding=weight_rounding,
            repetitions_rounding=repetitions_rounding,
            workout_reminder_active=workout_reminder_active,
            workout_reminder=workout_reminder,
            workout_duration=workout_duration,
            notification_language=notification_language,
            age=age,
            birthdate=birthdate,
            height=height,
            gender=gender,
            sleep_hours=sleep_hours,
            work_hours=work_hours,
            work_intensity=work_intensity,
            sport_hours=sport_hours,
            sport_intensity=sport_intensity,
            freetime_hours=freetime_hours,
            freetime_intensity=freetime_intensity,
            calories=calories,
            weight_unit=weight_unit,
            num_days_weight_reminder=num_days_weight_reminder,
        )

        patched_userprofile_request.additional_properties = d
        return patched_userprofile_request

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
