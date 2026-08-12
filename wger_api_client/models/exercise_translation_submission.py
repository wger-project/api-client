from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise_submission_alias import ExerciseSubmissionAlias
    from ..models.exercise_submission_comment import ExerciseSubmissionComment


T = TypeVar("T", bound="ExerciseTranslationSubmission")


@_attrs_define
class ExerciseTranslationSubmission:
    """Translation serializer used as a nested child of ``ExerciseSubmissionSerializer``.

    Differs from the regular serializer only because:
    - the ``exercise`` FK isn't known until the parent creates it (passed via ``create()`` kwargs);
    - the payload also accepts nested ``aliases`` and ``comments`` lists,
      which the regular CRUD endpoint doesn't;
    - those take their ``translation`` from the parent, so they don't accept one.

        Attributes:
            name (str):
            description_source (str):
            language (int):
            aliases (list[ExerciseSubmissionAlias] | Unset):
            comments (list[ExerciseSubmissionComment] | Unset):
            license_author (str | Unset): If you are not the author, enter the name or source here.
    """

    name: str
    description_source: str
    language: int
    aliases: list[ExerciseSubmissionAlias] | Unset = UNSET
    comments: list[ExerciseSubmissionComment] | Unset = UNSET
    license_author: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description_source = self.description_source

        language = self.language

        aliases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = []
            for aliases_item_data in self.aliases:
                aliases_item = aliases_item_data.to_dict()
                aliases.append(aliases_item)

        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)

        license_author = self.license_author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description_source": description_source,
                "language": language,
            }
        )
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if comments is not UNSET:
            field_dict["comments"] = comments
        if license_author is not UNSET:
            field_dict["license_author"] = license_author

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.exercise_submission_alias import ExerciseSubmissionAlias
        from ..models.exercise_submission_comment import ExerciseSubmissionComment

        d = dict(src_dict)
        name = d.pop("name")

        description_source = d.pop("description_source")

        language = d.pop("language")

        _aliases = d.pop("aliases", UNSET)
        aliases: list[ExerciseSubmissionAlias] | Unset = UNSET
        if _aliases is not UNSET:
            aliases = []
            for aliases_item_data in _aliases:
                aliases_item = ExerciseSubmissionAlias.from_dict(aliases_item_data)

                aliases.append(aliases_item)

        _comments = d.pop("comments", UNSET)
        comments: list[ExerciseSubmissionComment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = ExerciseSubmissionComment.from_dict(comments_item_data)

                comments.append(comments_item)

        license_author = d.pop("license_author", UNSET)

        exercise_translation_submission = cls(
            name=name,
            description_source=description_source,
            language=language,
            aliases=aliases,
            comments=comments,
            license_author=license_author,
        )

        exercise_translation_submission.additional_properties = d
        return exercise_translation_submission

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
