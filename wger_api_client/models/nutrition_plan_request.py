from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NutritionPlanRequest")


@_attrs_define
class NutritionPlanRequest:
    """Nutritional plan serializer

    Attributes:
        id (UUID | Unset):
        start (datetime.date | Unset):
        end (datetime.date | None | Unset):
        description (str | Unset): A description of the goal of the plan, e.g. "Gain mass" or "Prepare for summer"
        only_logging (bool | Unset):
        goal_energy (int | None | Unset):
        goal_protein (int | None | Unset):
        goal_carbohydrates (int | None | Unset):
        goal_fat (int | None | Unset):
        goal_fiber (int | None | Unset):
    """

    id: UUID | Unset = UNSET
    start: datetime.date | Unset = UNSET
    end: datetime.date | None | Unset = UNSET
    description: str | Unset = UNSET
    only_logging: bool | Unset = UNSET
    goal_energy: int | None | Unset = UNSET
    goal_protein: int | None | Unset = UNSET
    goal_carbohydrates: int | None | Unset = UNSET
    goal_fat: int | None | Unset = UNSET
    goal_fiber: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        end: None | str | Unset
        if isinstance(self.end, Unset):
            end = UNSET
        elif isinstance(self.end, datetime.date):
            end = self.end.isoformat()
        else:
            end = self.end

        description = self.description

        only_logging = self.only_logging

        goal_energy: int | None | Unset
        if isinstance(self.goal_energy, Unset):
            goal_energy = UNSET
        else:
            goal_energy = self.goal_energy

        goal_protein: int | None | Unset
        if isinstance(self.goal_protein, Unset):
            goal_protein = UNSET
        else:
            goal_protein = self.goal_protein

        goal_carbohydrates: int | None | Unset
        if isinstance(self.goal_carbohydrates, Unset):
            goal_carbohydrates = UNSET
        else:
            goal_carbohydrates = self.goal_carbohydrates

        goal_fat: int | None | Unset
        if isinstance(self.goal_fat, Unset):
            goal_fat = UNSET
        else:
            goal_fat = self.goal_fat

        goal_fiber: int | None | Unset
        if isinstance(self.goal_fiber, Unset):
            goal_fiber = UNSET
        else:
            goal_fiber = self.goal_fiber

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if description is not UNSET:
            field_dict["description"] = description
        if only_logging is not UNSET:
            field_dict["only_logging"] = only_logging
        if goal_energy is not UNSET:
            field_dict["goal_energy"] = goal_energy
        if goal_protein is not UNSET:
            field_dict["goal_protein"] = goal_protein
        if goal_carbohydrates is not UNSET:
            field_dict["goal_carbohydrates"] = goal_carbohydrates
        if goal_fat is not UNSET:
            field_dict["goal_fat"] = goal_fat
        if goal_fiber is not UNSET:
            field_dict["goal_fiber"] = goal_fiber

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _start = d.pop("start", UNSET)
        start: datetime.date | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = datetime.date.fromisoformat(_start)

        def _parse_end(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_0 = datetime.date.fromisoformat(data)

                return end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end = _parse_end(d.pop("end", UNSET))

        description = d.pop("description", UNSET)

        only_logging = d.pop("only_logging", UNSET)

        def _parse_goal_energy(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        goal_energy = _parse_goal_energy(d.pop("goal_energy", UNSET))

        def _parse_goal_protein(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        goal_protein = _parse_goal_protein(d.pop("goal_protein", UNSET))

        def _parse_goal_carbohydrates(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        goal_carbohydrates = _parse_goal_carbohydrates(
            d.pop("goal_carbohydrates", UNSET)
        )

        def _parse_goal_fat(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        goal_fat = _parse_goal_fat(d.pop("goal_fat", UNSET))

        def _parse_goal_fiber(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        goal_fiber = _parse_goal_fiber(d.pop("goal_fiber", UNSET))

        nutrition_plan_request = cls(
            id=id,
            start=start,
            end=end,
            description=description,
            only_logging=only_logging,
            goal_energy=goal_energy,
            goal_protein=goal_protein,
            goal_carbohydrates=goal_carbohydrates,
            goal_fat=goal_fat,
            goal_fiber=goal_fiber,
        )

        nutrition_plan_request.additional_properties = d
        return nutrition_plan_request

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
