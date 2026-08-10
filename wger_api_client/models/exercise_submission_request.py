from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise_translation_submission_request import (
        ExerciseTranslationSubmissionRequest,
    )


T = TypeVar("T", bound="ExerciseSubmissionRequest")


@_attrs_define
class ExerciseSubmissionRequest:
    """Exercise submission serializer

    Attributes:
        category (int):
        translations (list[ExerciseTranslationSubmissionRequest]):
        muscles (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        equipment (list[int] | Unset):
        variation_group (None | Unset | UUID):
        variations_connect_to (int | None | Unset): If provided, the created exercise will be added to the selected
            variation set.
        license_ (int | Unset):
        license_author (str | Unset): If you are not the author, enter the name or source here.
    """

    category: int
    translations: list[ExerciseTranslationSubmissionRequest]
    muscles: list[int] | Unset = UNSET
    muscles_secondary: list[int] | Unset = UNSET
    equipment: list[int] | Unset = UNSET
    variation_group: None | Unset | UUID = UNSET
    variations_connect_to: int | None | Unset = UNSET
    license_: int | Unset = UNSET
    license_author: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

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

        variations_connect_to: int | None | Unset
        if isinstance(self.variations_connect_to, Unset):
            variations_connect_to = UNSET
        else:
            variations_connect_to = self.variations_connect_to

        license_ = self.license_

        license_author = self.license_author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "translations": translations,
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
        if variations_connect_to is not UNSET:
            field_dict["variations_connect_to"] = variations_connect_to
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_author is not UNSET:
            field_dict["license_author"] = license_author

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("category", (None, str(self.category).encode(), "text/plain")))

        for translations_item_element in self.translations:
            files.append(
                (
                    "translations",
                    (
                        None,
                        json.dumps(translations_item_element.to_dict()).encode(),
                        "application/json",
                    ),
                )
            )

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

        if not isinstance(self.variations_connect_to, Unset):
            if isinstance(self.variations_connect_to, int):
                files.append(
                    (
                        "variations_connect_to",
                        (None, str(self.variations_connect_to).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "variations_connect_to",
                        (None, str(self.variations_connect_to).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.license_, Unset):
            files.append(("license", (None, str(self.license_).encode(), "text/plain")))

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
        from ..models.exercise_translation_submission_request import (
            ExerciseTranslationSubmissionRequest,
        )

        d = dict(src_dict)
        category = d.pop("category")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = ExerciseTranslationSubmissionRequest.from_dict(
                translations_item_data
            )

            translations.append(translations_item)

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

        def _parse_variations_connect_to(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        variations_connect_to = _parse_variations_connect_to(
            d.pop("variations_connect_to", UNSET)
        )

        license_ = d.pop("license", UNSET)

        license_author = d.pop("license_author", UNSET)

        exercise_submission_request = cls(
            category=category,
            translations=translations,
            muscles=muscles,
            muscles_secondary=muscles_secondary,
            equipment=equipment,
            variation_group=variation_group,
            variations_connect_to=variations_connect_to,
            license_=license_,
            license_author=license_author,
        )

        exercise_submission_request.additional_properties = d
        return exercise_submission_request

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
