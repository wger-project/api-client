from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingredient_info import IngredientInfo


T = TypeVar("T", bound="CursorPaginatedIngredientInfoList")


@_attrs_define
class CursorPaginatedIngredientInfoList:
    """
    Attributes:
        results (list[IngredientInfo]):
        next_ (None | str | Unset):  Example: http://api.example.org/accounts/?cursor=cD00ODY%3D".
        previous (None | str | Unset):  Example: http://api.example.org/accounts/?cursor=cj0xJnA9NDg3.
    """

    results: list[IngredientInfo]
    next_: None | str | Unset = UNSET
    previous: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        next_: None | str | Unset
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        previous: None | str | Unset
        if isinstance(self.previous, Unset):
            previous = UNSET
        else:
            previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ingredient_info import IngredientInfo

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = IngredientInfo.from_dict(results_item_data)

            results.append(results_item)

        def _parse_next_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_ = _parse_next_(d.pop("next", UNSET))

        def _parse_previous(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        previous = _parse_previous(d.pop("previous", UNSET))

        cursor_paginated_ingredient_info_list = cls(
            results=results,
            next_=next_,
            previous=previous,
        )

        cursor_paginated_ingredient_info_list.additional_properties = d
        return cursor_paginated_ingredient_info_list

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
