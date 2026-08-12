from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_enum import OperationEnum
from ..models.step_enum import StepEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRepetitionsConfigRequest")


@_attrs_define
class PatchedRepetitionsConfigRequest:
    """Repetition Config serializer

    Attributes:
        slot_entry (int | Unset):
        iteration (int | Unset):
        value (str | Unset):
        operation (OperationEnum | Unset): * `+` - Plus
            * `-` - Minus
            * `r` - Replace
        step (StepEnum | Unset): * `na` - Not Applicable
            * `abs` - Absolute
            * `percent` - Percent
        repeat (bool | Unset):
        requirements (Any | Unset):
    """

    slot_entry: int | Unset = UNSET
    iteration: int | Unset = UNSET
    value: str | Unset = UNSET
    operation: OperationEnum | Unset = UNSET
    step: StepEnum | Unset = UNSET
    repeat: bool | Unset = UNSET
    requirements: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slot_entry = self.slot_entry

        iteration = self.iteration

        value = self.value

        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        step: str | Unset = UNSET
        if not isinstance(self.step, Unset):
            step = self.step.value

        repeat = self.repeat

        requirements = self.requirements

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slot_entry is not UNSET:
            field_dict["slot_entry"] = slot_entry
        if iteration is not UNSET:
            field_dict["iteration"] = iteration
        if value is not UNSET:
            field_dict["value"] = value
        if operation is not UNSET:
            field_dict["operation"] = operation
        if step is not UNSET:
            field_dict["step"] = step
        if repeat is not UNSET:
            field_dict["repeat"] = repeat
        if requirements is not UNSET:
            field_dict["requirements"] = requirements

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        slot_entry = d.pop("slot_entry", UNSET)

        iteration = d.pop("iteration", UNSET)

        value = d.pop("value", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: OperationEnum | Unset
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = OperationEnum(_operation)

        _step = d.pop("step", UNSET)
        step: StepEnum | Unset
        if isinstance(_step, Unset):
            step = UNSET
        else:
            step = StepEnum(_step)

        repeat = d.pop("repeat", UNSET)

        requirements = d.pop("requirements", UNSET)

        patched_repetitions_config_request = cls(
            slot_entry=slot_entry,
            iteration=iteration,
            value=value,
            operation=operation,
            step=step,
            repeat=repeat,
            requirements=requirements,
        )

        patched_repetitions_config_request.additional_properties = d
        return patched_repetitions_config_request

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
