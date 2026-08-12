from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_type_enum import ModelTypeEnum, check_model_type_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeletionLog")


@_attrs_define
class DeletionLog:
    """Deletion log serializer

    Attributes:
        model_type (ModelTypeEnum): * `base` - base
            * `translation` - translation
            * `image` - image
            * `video` - video
        uuid (UUID):
        replaced_by (None | UUID): UUID of the object replaced by the deleted one. At the moment only available for
            exercises
        timestamp (datetime.datetime):
        comment (str | Unset):
    """

    model_type: ModelTypeEnum
    uuid: UUID
    replaced_by: None | UUID
    timestamp: datetime.datetime
    comment: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_type: str = self.model_type

        uuid = str(self.uuid)

        replaced_by: None | str
        if isinstance(self.replaced_by, UUID):
            replaced_by = str(self.replaced_by)
        else:
            replaced_by = self.replaced_by

        timestamp = self.timestamp.isoformat()

        comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_type": model_type,
                "uuid": uuid,
                "replaced_by": replaced_by,
                "timestamp": timestamp,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        model_type = check_model_type_enum(d.pop("model_type"))

        uuid = UUID(d.pop("uuid"))

        def _parse_replaced_by(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                replaced_by_type_0 = UUID(data)

                return replaced_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        replaced_by = _parse_replaced_by(d.pop("replaced_by"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        comment = d.pop("comment", UNSET)

        deletion_log = cls(
            model_type=model_type,
            uuid=uuid,
            replaced_by=replaced_by,
            timestamp=timestamp,
            comment=comment,
        )

        deletion_log.additional_properties = d
        return deletion_log

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
