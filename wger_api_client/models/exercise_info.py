from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.equipment import Equipment
    from ..models.exercise_category import ExerciseCategory
    from ..models.exercise_image import ExerciseImage
    from ..models.exercise_translation_info import ExerciseTranslationInfo
    from ..models.exercise_video_info import ExerciseVideoInfo
    from ..models.license_ import License
    from ..models.muscle import Muscle


T = TypeVar("T", bound="ExerciseInfo")


@_attrs_define
class ExerciseInfo:
    """Exercise info serializer

    Attributes:
        id (int):
        uuid (UUID):
        created (datetime.datetime):
        last_update (datetime.datetime):
        last_update_global (datetime.datetime):
        category (ExerciseCategory): ExerciseCategory serializer
        muscles (list[Muscle]):
        muscles_secondary (list[Muscle]):
        equipment (list[Equipment]):
        license_ (License): License serializer
        images (list[ExerciseImage]):
        translations (list[ExerciseTranslationInfo]):
        videos (list[ExerciseVideoInfo]):
        author_history (list[str]):
        total_authors_history (list[str]):
        license_author (str | Unset): If you are not the author, enter the name or source here.
        variation_group (None | Unset | UUID):
    """

    id: int
    uuid: UUID
    created: datetime.datetime
    last_update: datetime.datetime
    last_update_global: datetime.datetime
    category: ExerciseCategory
    muscles: list[Muscle]
    muscles_secondary: list[Muscle]
    equipment: list[Equipment]
    license_: License
    images: list[ExerciseImage]
    translations: list[ExerciseTranslationInfo]
    videos: list[ExerciseVideoInfo]
    author_history: list[str]
    total_authors_history: list[str]
    license_author: str | Unset = UNSET
    variation_group: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = str(self.uuid)

        created = self.created.isoformat()

        last_update = self.last_update.isoformat()

        last_update_global = self.last_update_global.isoformat()

        category = self.category.to_dict()

        muscles = []
        for muscles_item_data in self.muscles:
            muscles_item = muscles_item_data.to_dict()
            muscles.append(muscles_item)

        muscles_secondary = []
        for muscles_secondary_item_data in self.muscles_secondary:
            muscles_secondary_item = muscles_secondary_item_data.to_dict()
            muscles_secondary.append(muscles_secondary_item)

        equipment = []
        for equipment_item_data in self.equipment:
            equipment_item = equipment_item_data.to_dict()
            equipment.append(equipment_item)

        license_ = self.license_.to_dict()

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        author_history = self.author_history

        total_authors_history = self.total_authors_history

        license_author = self.license_author

        variation_group: None | str | Unset
        if isinstance(self.variation_group, Unset):
            variation_group = UNSET
        elif isinstance(self.variation_group, UUID):
            variation_group = str(self.variation_group)
        else:
            variation_group = self.variation_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "created": created,
                "last_update": last_update,
                "last_update_global": last_update_global,
                "category": category,
                "muscles": muscles,
                "muscles_secondary": muscles_secondary,
                "equipment": equipment,
                "license": license_,
                "images": images,
                "translations": translations,
                "videos": videos,
                "author_history": author_history,
                "total_authors_history": total_authors_history,
            }
        )
        if license_author is not UNSET:
            field_dict["license_author"] = license_author
        if variation_group is not UNSET:
            field_dict["variation_group"] = variation_group

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.equipment import Equipment
        from ..models.exercise_category import ExerciseCategory
        from ..models.exercise_image import ExerciseImage
        from ..models.exercise_translation_info import ExerciseTranslationInfo
        from ..models.exercise_video_info import ExerciseVideoInfo
        from ..models.license_ import License
        from ..models.muscle import Muscle

        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        created = datetime.datetime.fromisoformat(d.pop("created"))

        last_update = datetime.datetime.fromisoformat(d.pop("last_update"))

        last_update_global = datetime.datetime.fromisoformat(
            d.pop("last_update_global")
        )

        category = ExerciseCategory.from_dict(d.pop("category"))

        muscles = []
        _muscles = d.pop("muscles")
        for muscles_item_data in _muscles:
            muscles_item = Muscle.from_dict(muscles_item_data)

            muscles.append(muscles_item)

        muscles_secondary = []
        _muscles_secondary = d.pop("muscles_secondary")
        for muscles_secondary_item_data in _muscles_secondary:
            muscles_secondary_item = Muscle.from_dict(muscles_secondary_item_data)

            muscles_secondary.append(muscles_secondary_item)

        equipment = []
        _equipment = d.pop("equipment")
        for equipment_item_data in _equipment:
            equipment_item = Equipment.from_dict(equipment_item_data)

            equipment.append(equipment_item)

        license_ = License.from_dict(d.pop("license"))

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = ExerciseImage.from_dict(images_item_data)

            images.append(images_item)

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = ExerciseTranslationInfo.from_dict(
                translations_item_data
            )

            translations.append(translations_item)

        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = ExerciseVideoInfo.from_dict(videos_item_data)

            videos.append(videos_item)

        author_history = cast(list[str], d.pop("author_history"))

        total_authors_history = cast(list[str], d.pop("total_authors_history"))

        license_author = d.pop("license_author", UNSET)

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

        exercise_info = cls(
            id=id,
            uuid=uuid,
            created=created,
            last_update=last_update,
            last_update_global=last_update_global,
            category=category,
            muscles=muscles,
            muscles_secondary=muscles_secondary,
            equipment=equipment,
            license_=license_,
            images=images,
            translations=translations,
            videos=videos,
            author_history=author_history,
            total_authors_history=total_authors_history,
            license_author=license_author,
            variation_group=variation_group,
        )

        exercise_info.additional_properties = d
        return exercise_info

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
