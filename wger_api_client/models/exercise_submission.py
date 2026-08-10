from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise_translation_submission import ExerciseTranslationSubmission


T = TypeVar("T", bound="ExerciseSubmission")


@_attrs_define
class ExerciseSubmission:
    """Exercise submission serializer

    Attributes:
        id (int):
        category (int):
        translations (list[ExerciseTranslationSubmission]):
        muscles (list[int] | Unset):
        muscles_secondary (list[int] | Unset):
        equipment (list[int] | Unset):
        variation_group (None | Unset | UUID):
        license_ (int | Unset):
        license_author (str | Unset): If you are not the author, enter the name or source here.
    """

    id: int
    category: int
    translations: list[ExerciseTranslationSubmission]
    muscles: list[int] | Unset = UNSET
    muscles_secondary: list[int] | Unset = UNSET
    equipment: list[int] | Unset = UNSET
    variation_group: None | Unset | UUID = UNSET
    license_: int | Unset = UNSET
    license_author: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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

        license_ = self.license_

        license_author = self.license_author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
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
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_author is not UNSET:
            field_dict["license_author"] = license_author

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.exercise_translation_submission import (
            ExerciseTranslationSubmission,
        )

        d = dict(src_dict)
        id = d.pop("id")

        category = d.pop("category")

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = ExerciseTranslationSubmission.from_dict(
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

        license_ = d.pop("license", UNSET)

        license_author = d.pop("license_author", UNSET)

        exercise_submission = cls(
            id=id,
            category=category,
            translations=translations,
            muscles=muscles,
            muscles_secondary=muscles_secondary,
            equipment=equipment,
            variation_group=variation_group,
            license_=license_,
            license_author=license_author,
        )

        exercise_submission.additional_properties = d
        return exercise_submission

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
