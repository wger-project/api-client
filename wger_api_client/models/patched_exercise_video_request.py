from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PatchedExerciseVideoRequest")


@_attrs_define
class PatchedExerciseVideoRequest:
    """ExerciseVideo serializer

    Attributes:
        exercise (int | Unset):
        video (File | Unset):
        is_main (bool | Unset):
        license_ (int | Unset):
        license_title (str | Unset):
        license_object_url (str | Unset):
        license_author (str | Unset): If you are not the author, enter the name or source here.
        license_author_url (str | Unset):
        license_derivative_source_url (str | Unset): Note that a derivative work is one which is not only based on a
            previous work, but which also contains sufficient new, creative content to entitle it to its own copyright.
    """

    exercise: int | Unset = UNSET
    video: File | Unset = UNSET
    is_main: bool | Unset = UNSET
    license_: int | Unset = UNSET
    license_title: str | Unset = UNSET
    license_object_url: str | Unset = UNSET
    license_author: str | Unset = UNSET
    license_author_url: str | Unset = UNSET
    license_derivative_source_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exercise = self.exercise

        video: FileTypes | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_tuple()

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
        field_dict.update({})
        if exercise is not UNSET:
            field_dict["exercise"] = exercise
        if video is not UNSET:
            field_dict["video"] = video
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.exercise, Unset):
            files.append(
                ("exercise", (None, str(self.exercise).encode(), "text/plain"))
            )

        if not isinstance(self.video, Unset):
            files.append(("video", self.video.to_tuple()))

        if not isinstance(self.is_main, Unset):
            files.append(("is_main", (None, str(self.is_main).encode(), "text/plain")))

        if not isinstance(self.license_, Unset):
            files.append(("license", (None, str(self.license_).encode(), "text/plain")))

        if not isinstance(self.license_title, Unset):
            files.append(
                (
                    "license_title",
                    (None, str(self.license_title).encode(), "text/plain"),
                )
            )

        if not isinstance(self.license_object_url, Unset):
            if isinstance(self.license_object_url, str):
                files.append(
                    (
                        "license_object_url",
                        (None, str(self.license_object_url).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.license_author, Unset):
            files.append(
                (
                    "license_author",
                    (None, str(self.license_author).encode(), "text/plain"),
                )
            )

        if not isinstance(self.license_author_url, Unset):
            if isinstance(self.license_author_url, str):
                files.append(
                    (
                        "license_author_url",
                        (None, str(self.license_author_url).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.license_derivative_source_url, Unset):
            if isinstance(self.license_derivative_source_url, str):
                files.append(
                    (
                        "license_derivative_source_url",
                        (
                            None,
                            str(self.license_derivative_source_url).encode(),
                            "text/plain",
                        ),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exercise = d.pop("exercise", UNSET)

        _video = d.pop("video", UNSET)
        video: File | Unset
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = File(payload=BytesIO(_video))

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

        patched_exercise_video_request = cls(
            exercise=exercise,
            video=video,
            is_main=is_main,
            license_=license_,
            license_title=license_title,
            license_object_url=license_object_url,
            license_author=license_author,
            license_author_url=license_author_url,
            license_derivative_source_url=license_derivative_source_url,
        )

        patched_exercise_video_request.additional_properties = d
        return patched_exercise_video_request

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
