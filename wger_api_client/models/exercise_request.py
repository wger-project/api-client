from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExerciseRequest")


@_attrs_define
class ExerciseRequest:
    """Exercise serializer

    Attributes:
        category (int):
        muscles (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        equipment (list[int] | Unset):
        variation_group (None | Unset | UUID):
        license_author (str | Unset): If you are not the author, enter the name or source here.
    """

    category: int
    muscles: list[int] | Unset = UNSET
    muscles_secondary: list[int] | Unset = UNSET
    equipment: list[int] | Unset = UNSET
    variation_group: None | Unset | UUID = UNSET
    license_author: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        muscles: list[int] | Unset = UNSET
        if not isinstance(self.muscles, Unset):
            muscles = self.muscles

        muscles_secondary: list[int] | Unset = UNSET
        if not isinstance(self.muscles_secondary, Unset):
            muscles_secondary = self.muscles_secondary

        equipment: list[int] | Unset = UNSET
        if not isinstance(self.equipment, Unset):
            equipment = self.equipment

        variation_group: None | str | Unset
        if isinstance(self.variation_group, Unset):
            variation_group = UNSET
        elif isinstance(self.variation_group, UUID):
            variation_group = str(self.variation_group)
        else:
            variation_group = self.variation_group

        license_author = self.license_author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
            }
        )
        if muscles is not UNSET:
            field_dict["muscles"] = muscles
        if muscles_secondary is not UNSET:
            field_dict["muscles_secondary"] = muscles_secondary
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if variation_group is not UNSET:
            field_dict["variation_group"] = variation_group
        if license_author is not UNSET:
            field_dict["license_author"] = license_author

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("category", (None, str(self.category).encode(), "text/plain")))

        if not isinstance(self.muscles, Unset):
            for muscles_item_element in self.muscles:
                files.append(
                    (
                        "muscles",
                        (None, str(muscles_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.muscles_secondary, Unset):
            for muscles_secondary_item_element in self.muscles_secondary:
                files.append(
                    (
                        "muscles_secondary",
                        (
                            None,
                            str(muscles_secondary_item_element).encode(),
                            "text/plain",
                        ),
                    )
                )

        if not isinstance(self.equipment, Unset):
            for equipment_item_element in self.equipment:
                files.append(
                    (
                        "equipment",
                        (None, str(equipment_item_element).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.variation_group, Unset):
            if isinstance(self.variation_group, UUID):
                files.append(
                    ("variation_group", (None, str(self.variation_group), "text/plain"))
                )
            else:
                files.append(
                    (
                        "variation_group",
                        (None, str(self.variation_group).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.license_author, Unset):
            files.append(
                (
                    "license_author",
                    (None, str(self.license_author).encode(), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = d.pop("category")

        muscles = cast(list[int], d.pop("muscles", UNSET))

        muscles_secondary = cast(list[int], d.pop("muscles_secondary", UNSET))

        equipment = cast(list[int], d.pop("equipment", UNSET))

        def _parse_variation_group(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                variation_group_type_0 = UUID(data)

                return variation_group_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        variation_group = _parse_variation_group(d.pop("variation_group", UNSET))

        license_author = d.pop("license_author", UNSET)

        exercise_request = cls(
            category=category,
            muscles=muscles,
            muscles_secondary=muscles_secondary,
            equipment=equipment,
            variation_group=variation_group,
            license_author=license_author,
        )

        exercise_request.additional_properties = d
        return exercise_request

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
