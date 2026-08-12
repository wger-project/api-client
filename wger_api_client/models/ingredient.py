from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.nutriscore_enum import NutriscoreEnum, check_nutriscore_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingredient_weight_unit import IngredientWeightUnit


T = TypeVar("T", bound="Ingredient")


@_attrs_define
class Ingredient:
    """Ingredient serializer

    Attributes:
        id (int):
        uuid (UUID):
        name (str):
        created (datetime.datetime):
        last_update (datetime.datetime):
        last_imported (datetime.datetime | None):
        energy (int): In kcal per 100g
        protein (str): In g per 100g of product
        carbohydrates (str): In g per 100g of product
        fat (str): In g per 100g of product
        weight_units (list[IngredientWeightUnit]):
        language (int):
        remote_id (None | str | Unset):
        source_name (None | str | Unset):
        source_url (None | str | Unset): Link to product
        code (None | str | Unset):
        common_name (None | str | Unset):
        brand (None | str | Unset):
        carbohydrates_sugar (None | str | Unset): In g per 100g of product
        fat_saturated (None | str | Unset): In g per 100g of product
        fiber (None | str | Unset): In g per 100g of product
        sodium (None | str | Unset): In g per 100g of product
        is_vegan (bool | None | Unset): Whether the ingredient is suitable for a vegan diet
        is_vegetarian (bool | None | Unset): Whether the ingredient is suitable for a vegetarian diet
        nutriscore (BlankEnum | None | NutriscoreEnum | Unset): Nutri-Score grade from Open Food Facts

            * `a` - A
            * `b` - B
            * `c` - C
            * `d` - D
            * `e` - E
        license_ (int | Unset):
        license_title (str | Unset):
        license_object_url (str | Unset):
        license_author (str | Unset): If you are not the author, enter the name or source here.
        license_author_url (str | Unset):
        license_derivative_source_url (str | Unset): Note that a derivative work is one which is not only based on a
            previous work, but which also contains sufficient new, creative content to entitle it to its own copyright.
    """

    id: int
    uuid: UUID
    name: str
    created: datetime.datetime
    last_update: datetime.datetime
    last_imported: datetime.datetime | None
    energy: int
    protein: str
    carbohydrates: str
    fat: str
    weight_units: list[IngredientWeightUnit]
    language: int
    remote_id: None | str | Unset = UNSET
    source_name: None | str | Unset = UNSET
    source_url: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    common_name: None | str | Unset = UNSET
    brand: None | str | Unset = UNSET
    carbohydrates_sugar: None | str | Unset = UNSET
    fat_saturated: None | str | Unset = UNSET
    fiber: None | str | Unset = UNSET
    sodium: None | str | Unset = UNSET
    is_vegan: bool | None | Unset = UNSET
    is_vegetarian: bool | None | Unset = UNSET
    nutriscore: BlankEnum | None | NutriscoreEnum | Unset = UNSET
    license_: int | Unset = UNSET
    license_title: str | Unset = UNSET
    license_object_url: str | Unset = UNSET
    license_author: str | Unset = UNSET
    license_author_url: str | Unset = UNSET
    license_derivative_source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = str(self.uuid)

        name = self.name

        created = self.created.isoformat()

        last_update = self.last_update.isoformat()

        last_imported: None | str
        if isinstance(self.last_imported, datetime.datetime):
            last_imported = self.last_imported.isoformat()
        else:
            last_imported = self.last_imported

        energy = self.energy

        protein = self.protein

        carbohydrates = self.carbohydrates

        fat = self.fat

        weight_units = []
        for weight_units_item_data in self.weight_units:
            weight_units_item = weight_units_item_data.to_dict()
            weight_units.append(weight_units_item)

        language = self.language

        remote_id: None | str | Unset
        if isinstance(self.remote_id, Unset):
            remote_id = UNSET
        else:
            remote_id = self.remote_id

        source_name: None | str | Unset
        if isinstance(self.source_name, Unset):
            source_name = UNSET
        else:
            source_name = self.source_name

        source_url: None | str | Unset
        if isinstance(self.source_url, Unset):
            source_url = UNSET
        else:
            source_url = self.source_url

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        common_name: None | str | Unset
        if isinstance(self.common_name, Unset):
            common_name = UNSET
        else:
            common_name = self.common_name

        brand: None | str | Unset
        if isinstance(self.brand, Unset):
            brand = UNSET
        else:
            brand = self.brand

        carbohydrates_sugar: None | str | Unset
        if isinstance(self.carbohydrates_sugar, Unset):
            carbohydrates_sugar = UNSET
        else:
            carbohydrates_sugar = self.carbohydrates_sugar

        fat_saturated: None | str | Unset
        if isinstance(self.fat_saturated, Unset):
            fat_saturated = UNSET
        else:
            fat_saturated = self.fat_saturated

        fiber: None | str | Unset
        if isinstance(self.fiber, Unset):
            fiber = UNSET
        else:
            fiber = self.fiber

        sodium: None | str | Unset
        if isinstance(self.sodium, Unset):
            sodium = UNSET
        else:
            sodium = self.sodium

        is_vegan: bool | None | Unset
        if isinstance(self.is_vegan, Unset):
            is_vegan = UNSET
        else:
            is_vegan = self.is_vegan

        is_vegetarian: bool | None | Unset
        if isinstance(self.is_vegetarian, Unset):
            is_vegetarian = UNSET
        else:
            is_vegetarian = self.is_vegetarian

        nutriscore: None | str | Unset
        if isinstance(self.nutriscore, Unset):
            nutriscore = UNSET
        elif isinstance(self.nutriscore, str) or isinstance(self.nutriscore, str):
            nutriscore = self.nutriscore
        else:
            nutriscore = self.nutriscore

        license_ = self.license_

        license_title = self.license_title

        license_object_url: str | Unset
        if isinstance(self.license_object_url, Unset):
            license_object_url = UNSET
        else:
            license_object_url = self.license_object_url

        license_author = self.license_author

        license_author_url: str | Unset
        if isinstance(self.license_author_url, Unset):
            license_author_url = UNSET
        else:
            license_author_url = self.license_author_url

        license_derivative_source_url: str | Unset
        if isinstance(self.license_derivative_source_url, Unset):
            license_derivative_source_url = UNSET
        else:
            license_derivative_source_url = self.license_derivative_source_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "name": name,
                "created": created,
                "last_update": last_update,
                "last_imported": last_imported,
                "energy": energy,
                "protein": protein,
                "carbohydrates": carbohydrates,
                "fat": fat,
                "weight_units": weight_units,
                "language": language,
            }
        )
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if source_name is not UNSET:
            field_dict["source_name"] = source_name
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if code is not UNSET:
            field_dict["code"] = code
        if common_name is not UNSET:
            field_dict["common_name"] = common_name
        if brand is not UNSET:
            field_dict["brand"] = brand
        if carbohydrates_sugar is not UNSET:
            field_dict["carbohydrates_sugar"] = carbohydrates_sugar
        if fat_saturated is not UNSET:
            field_dict["fat_saturated"] = fat_saturated
        if fiber is not UNSET:
            field_dict["fiber"] = fiber
        if sodium is not UNSET:
            field_dict["sodium"] = sodium
        if is_vegan is not UNSET:
            field_dict["is_vegan"] = is_vegan
        if is_vegetarian is not UNSET:
            field_dict["is_vegetarian"] = is_vegetarian
        if nutriscore is not UNSET:
            field_dict["nutriscore"] = nutriscore
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_title is not UNSET:
            field_dict["license_title"] = license_title
        if license_object_url is not UNSET:
            field_dict["license_object_url"] = license_object_url
        if license_author is not UNSET:
            field_dict["license_author"] = license_author
        if license_author_url is not UNSET:
            field_dict["license_author_url"] = license_author_url
        if license_derivative_source_url is not UNSET:
            field_dict["license_derivative_source_url"] = license_derivative_source_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ingredient_weight_unit import IngredientWeightUnit

        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        name = d.pop("name")

        created = datetime.datetime.fromisoformat(d.pop("created"))

        last_update = datetime.datetime.fromisoformat(d.pop("last_update"))

        def _parse_last_imported(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_imported_type_0 = datetime.datetime.fromisoformat(data)

                return last_imported_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_imported = _parse_last_imported(d.pop("last_imported"))

        energy = d.pop("energy")

        protein = d.pop("protein")

        carbohydrates = d.pop("carbohydrates")

        fat = d.pop("fat")

        weight_units = []
        _weight_units = d.pop("weight_units")
        for weight_units_item_data in _weight_units:
            weight_units_item = IngredientWeightUnit.from_dict(weight_units_item_data)

            weight_units.append(weight_units_item)

        language = d.pop("language")

        def _parse_remote_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remote_id = _parse_remote_id(d.pop("remote_id", UNSET))

        def _parse_source_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_name = _parse_source_name(d.pop("source_name", UNSET))

        def _parse_source_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_url = _parse_source_url(d.pop("source_url", UNSET))

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_common_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        common_name = _parse_common_name(d.pop("common_name", UNSET))

        def _parse_brand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brand = _parse_brand(d.pop("brand", UNSET))

        def _parse_carbohydrates_sugar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carbohydrates_sugar = _parse_carbohydrates_sugar(
            d.pop("carbohydrates_sugar", UNSET)
        )

        def _parse_fat_saturated(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fat_saturated = _parse_fat_saturated(d.pop("fat_saturated", UNSET))

        def _parse_fiber(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fiber = _parse_fiber(d.pop("fiber", UNSET))

        def _parse_sodium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sodium = _parse_sodium(d.pop("sodium", UNSET))

        def _parse_is_vegan(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_vegan = _parse_is_vegan(d.pop("is_vegan", UNSET))

        def _parse_is_vegetarian(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_vegetarian = _parse_is_vegetarian(d.pop("is_vegetarian", UNSET))

        def _parse_nutriscore(
            data: object,
        ) -> BlankEnum | None | NutriscoreEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                nutriscore_type_0 = check_nutriscore_enum(data)

                return nutriscore_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                nutriscore_type_1 = check_blank_enum(data)

                return nutriscore_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | NutriscoreEnum | Unset, data)

        nutriscore = _parse_nutriscore(d.pop("nutriscore", UNSET))

        license_ = d.pop("license", UNSET)

        license_title = d.pop("license_title", UNSET)

        def _parse_license_object_url(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        license_object_url = _parse_license_object_url(
            d.pop("license_object_url", UNSET)
        )

        license_author = d.pop("license_author", UNSET)

        def _parse_license_author_url(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        license_author_url = _parse_license_author_url(
            d.pop("license_author_url", UNSET)
        )

        def _parse_license_derivative_source_url(data: object) -> str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(str | Unset, data)

        license_derivative_source_url = _parse_license_derivative_source_url(
            d.pop("license_derivative_source_url", UNSET)
        )

        ingredient = cls(
            id=id,
            uuid=uuid,
            name=name,
            created=created,
            last_update=last_update,
            last_imported=last_imported,
            energy=energy,
            protein=protein,
            carbohydrates=carbohydrates,
            fat=fat,
            weight_units=weight_units,
            language=language,
            remote_id=remote_id,
            source_name=source_name,
            source_url=source_url,
            code=code,
            common_name=common_name,
            brand=brand,
            carbohydrates_sugar=carbohydrates_sugar,
            fat_saturated=fat_saturated,
            fiber=fiber,
            sodium=sodium,
            is_vegan=is_vegan,
            is_vegetarian=is_vegetarian,
            nutriscore=nutriscore,
            license_=license_,
            license_title=license_title,
            license_object_url=license_object_url,
            license_author=license_author,
            license_author_url=license_author_url,
            license_derivative_source_url=license_derivative_source_url,
        )

        ingredient.additional_properties = d
        return ingredient

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
