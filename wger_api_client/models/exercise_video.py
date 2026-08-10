from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExerciseVideo")


@_attrs_define
class ExerciseVideo:
    """ExerciseVideo serializer

    Attributes:
        id (int):
        uuid (UUID):
        exercise (int):
        exercise_uuid (UUID):
        video (str):
        size (int):
        duration (str):
        width (int):
        height (int):
        codec (str):
        codec_long (str):
        author_history (list[str]):
        is_main (bool | Unset):
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
    exercise: int
    exercise_uuid: UUID
    video: str
    size: int
    duration: str
    width: int
    height: int
    codec: str
    codec_long: str
    author_history: list[str]
    is_main: bool | Unset = UNSET
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

        exercise = self.exercise

        exercise_uuid = str(self.exercise_uuid)

        video = self.video

        size = self.size

        duration = self.duration

        width = self.width

        height = self.height

        codec = self.codec

        codec_long = self.codec_long

        author_history = self.author_history

        is_main = self.is_main

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
                "exercise": exercise,
                "exercise_uuid": exercise_uuid,
                "video": video,
                "size": size,
                "duration": duration,
                "width": width,
                "height": height,
                "codec": codec,
                "codec_long": codec_long,
                "author_history": author_history,
            }
        )
        if is_main is not UNSET:
            field_dict["is_main"] = is_main
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
        d = dict(src_dict)
        id = d.pop("id")

        uuid = UUID(d.pop("uuid"))

        exercise = d.pop("exercise")

        exercise_uuid = UUID(d.pop("exercise_uuid"))

        video = d.pop("video")

        size = d.pop("size")

        duration = d.pop("duration")

        width = d.pop("width")

        height = d.pop("height")

        codec = d.pop("codec")

        codec_long = d.pop("codec_long")

        author_history = cast(list[str], d.pop("author_history"))

        is_main = d.pop("is_main", UNSET)

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

        exercise_video = cls(
            id=id,
            uuid=uuid,
            exercise=exercise,
            exercise_uuid=exercise_uuid,
            video=video,
            size=size,
            duration=duration,
            width=width,
            height=height,
            codec=codec,
            codec_long=codec_long,
            author_history=author_history,
            is_main=is_main,
            license_=license_,
            license_title=license_title,
            license_object_url=license_object_url,
            license_author=license_author,
            license_author_url=license_author_url,
            license_derivative_source_url=license_derivative_source_url,
        )

        exercise_video.additional_properties = d
        return exercise_video

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
