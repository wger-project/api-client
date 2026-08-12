from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.exercise_type_enum import ExerciseTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.max_ri_r_config import MaxRiRConfig
    from ..models.max_set_nr_config import MaxSetNrConfig
    from ..models.repetitions_config import RepetitionsConfig
    from ..models.rest_config import RestConfig
    from ..models.ri_r_config import RiRConfig
    from ..models.set_nr_config import SetNrConfig
    from ..models.weight_config import WeightConfig


T = TypeVar("T", bound="SlotEntryStructure")


@_attrs_define
class SlotEntryStructure:
    """Slot entry

    Attributes:
        id (int):
        slot (int):
        exercise (int):
        repetitions_configs (list[RepetitionsConfig]):
        max_repetitions_configs (list[RepetitionsConfig]):
        weight_configs (list[WeightConfig]):
        max_weight_configs (list[WeightConfig]):
        set_nr_configs (list[SetNrConfig]):
        max_set_nr_configs (list[MaxSetNrConfig]):
        rir_configs (list[RiRConfig]):
        max_rir_configs (list[MaxRiRConfig]):
        rest_configs (list[RestConfig]):
        max_rest_configs (list[RestConfig]):
        order (int | Unset):
        comment (str | Unset):
        type_ (ExerciseTypeEnum | Unset): * `normal` - Normal
            * `warmup` - Warmup
            * `dropset` - Dropset
            * `myo` - Myo
            * `partial` - Partial
            * `forced` - Forced
            * `tut` - Tut
            * `iso` - Iso Hold
            * `jump` - Jump
        class_name (None | str | Unset):
        config (Any | Unset):
        repetition_unit (int | None | Unset):
        repetition_rounding (None | str | Unset):
        weight_unit (int | None | Unset):
        weight_rounding (None | str | Unset):
    """

    id: int
    slot: int
    exercise: int
    repetitions_configs: list[RepetitionsConfig]
    max_repetitions_configs: list[RepetitionsConfig]
    weight_configs: list[WeightConfig]
    max_weight_configs: list[WeightConfig]
    set_nr_configs: list[SetNrConfig]
    max_set_nr_configs: list[MaxSetNrConfig]
    rir_configs: list[RiRConfig]
    max_rir_configs: list[MaxRiRConfig]
    rest_configs: list[RestConfig]
    max_rest_configs: list[RestConfig]
    order: int | Unset = UNSET
    comment: str | Unset = UNSET
    type_: ExerciseTypeEnum | Unset = UNSET
    class_name: None | str | Unset = UNSET
    config: Any | Unset = UNSET
    repetition_unit: int | None | Unset = UNSET
    repetition_rounding: None | str | Unset = UNSET
    weight_unit: int | None | Unset = UNSET
    weight_rounding: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slot = self.slot

        exercise = self.exercise

        repetitions_configs = []
        for repetitions_configs_item_data in self.repetitions_configs:
            repetitions_configs_item = repetitions_configs_item_data.to_dict()
            repetitions_configs.append(repetitions_configs_item)

        max_repetitions_configs = []
        for max_repetitions_configs_item_data in self.max_repetitions_configs:
            max_repetitions_configs_item = max_repetitions_configs_item_data.to_dict()
            max_repetitions_configs.append(max_repetitions_configs_item)

        weight_configs = []
        for weight_configs_item_data in self.weight_configs:
            weight_configs_item = weight_configs_item_data.to_dict()
            weight_configs.append(weight_configs_item)

        max_weight_configs = []
        for max_weight_configs_item_data in self.max_weight_configs:
            max_weight_configs_item = max_weight_configs_item_data.to_dict()
            max_weight_configs.append(max_weight_configs_item)

        set_nr_configs = []
        for set_nr_configs_item_data in self.set_nr_configs:
            set_nr_configs_item = set_nr_configs_item_data.to_dict()
            set_nr_configs.append(set_nr_configs_item)

        max_set_nr_configs = []
        for max_set_nr_configs_item_data in self.max_set_nr_configs:
            max_set_nr_configs_item = max_set_nr_configs_item_data.to_dict()
            max_set_nr_configs.append(max_set_nr_configs_item)

        rir_configs = []
        for rir_configs_item_data in self.rir_configs:
            rir_configs_item = rir_configs_item_data.to_dict()
            rir_configs.append(rir_configs_item)

        max_rir_configs = []
        for max_rir_configs_item_data in self.max_rir_configs:
            max_rir_configs_item = max_rir_configs_item_data.to_dict()
            max_rir_configs.append(max_rir_configs_item)

        rest_configs = []
        for rest_configs_item_data in self.rest_configs:
            rest_configs_item = rest_configs_item_data.to_dict()
            rest_configs.append(rest_configs_item)

        max_rest_configs = []
        for max_rest_configs_item_data in self.max_rest_configs:
            max_rest_configs_item = max_rest_configs_item_data.to_dict()
            max_rest_configs.append(max_rest_configs_item)

        order = self.order

        comment = self.comment

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        class_name: None | str | Unset
        if isinstance(self.class_name, Unset):
            class_name = UNSET
        else:
            class_name = self.class_name

        config = self.config

        repetition_unit: int | None | Unset
        if isinstance(self.repetition_unit, Unset):
            repetition_unit = UNSET
        else:
            repetition_unit = self.repetition_unit

        repetition_rounding: None | str | Unset
        if isinstance(self.repetition_rounding, Unset):
            repetition_rounding = UNSET
        else:
            repetition_rounding = self.repetition_rounding

        weight_unit: int | None | Unset
        if isinstance(self.weight_unit, Unset):
            weight_unit = UNSET
        else:
            weight_unit = self.weight_unit

        weight_rounding: None | str | Unset
        if isinstance(self.weight_rounding, Unset):
            weight_rounding = UNSET
        else:
            weight_rounding = self.weight_rounding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slot": slot,
                "exercise": exercise,
                "repetitions_configs": repetitions_configs,
                "max_repetitions_configs": max_repetitions_configs,
                "weight_configs": weight_configs,
                "max_weight_configs": max_weight_configs,
                "set_nr_configs": set_nr_configs,
                "max_set_nr_configs": max_set_nr_configs,
                "rir_configs": rir_configs,
                "max_rir_configs": max_rir_configs,
                "rest_configs": rest_configs,
                "max_rest_configs": max_rest_configs,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order
        if comment is not UNSET:
            field_dict["comment"] = comment
        if type_ is not UNSET:
            field_dict["type"] = type_
        if class_name is not UNSET:
            field_dict["class_name"] = class_name
        if config is not UNSET:
            field_dict["config"] = config
        if repetition_unit is not UNSET:
            field_dict["repetition_unit"] = repetition_unit
        if repetition_rounding is not UNSET:
            field_dict["repetition_rounding"] = repetition_rounding
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if weight_rounding is not UNSET:
            field_dict["weight_rounding"] = weight_rounding

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.max_ri_r_config import MaxRiRConfig
        from ..models.max_set_nr_config import MaxSetNrConfig
        from ..models.repetitions_config import RepetitionsConfig
        from ..models.rest_config import RestConfig
        from ..models.ri_r_config import RiRConfig
        from ..models.set_nr_config import SetNrConfig
        from ..models.weight_config import WeightConfig

        d = dict(src_dict)
        id = d.pop("id")

        slot = d.pop("slot")

        exercise = d.pop("exercise")

        repetitions_configs = []
        _repetitions_configs = d.pop("repetitions_configs")
        for repetitions_configs_item_data in _repetitions_configs:
            repetitions_configs_item = RepetitionsConfig.from_dict(
                repetitions_configs_item_data
            )

            repetitions_configs.append(repetitions_configs_item)

        max_repetitions_configs = []
        _max_repetitions_configs = d.pop("max_repetitions_configs")
        for max_repetitions_configs_item_data in _max_repetitions_configs:
            max_repetitions_configs_item = RepetitionsConfig.from_dict(
                max_repetitions_configs_item_data
            )

            max_repetitions_configs.append(max_repetitions_configs_item)

        weight_configs = []
        _weight_configs = d.pop("weight_configs")
        for weight_configs_item_data in _weight_configs:
            weight_configs_item = WeightConfig.from_dict(weight_configs_item_data)

            weight_configs.append(weight_configs_item)

        max_weight_configs = []
        _max_weight_configs = d.pop("max_weight_configs")
        for max_weight_configs_item_data in _max_weight_configs:
            max_weight_configs_item = WeightConfig.from_dict(
                max_weight_configs_item_data
            )

            max_weight_configs.append(max_weight_configs_item)

        set_nr_configs = []
        _set_nr_configs = d.pop("set_nr_configs")
        for set_nr_configs_item_data in _set_nr_configs:
            set_nr_configs_item = SetNrConfig.from_dict(set_nr_configs_item_data)

            set_nr_configs.append(set_nr_configs_item)

        max_set_nr_configs = []
        _max_set_nr_configs = d.pop("max_set_nr_configs")
        for max_set_nr_configs_item_data in _max_set_nr_configs:
            max_set_nr_configs_item = MaxSetNrConfig.from_dict(
                max_set_nr_configs_item_data
            )

            max_set_nr_configs.append(max_set_nr_configs_item)

        rir_configs = []
        _rir_configs = d.pop("rir_configs")
        for rir_configs_item_data in _rir_configs:
            rir_configs_item = RiRConfig.from_dict(rir_configs_item_data)

            rir_configs.append(rir_configs_item)

        max_rir_configs = []
        _max_rir_configs = d.pop("max_rir_configs")
        for max_rir_configs_item_data in _max_rir_configs:
            max_rir_configs_item = MaxRiRConfig.from_dict(max_rir_configs_item_data)

            max_rir_configs.append(max_rir_configs_item)

        rest_configs = []
        _rest_configs = d.pop("rest_configs")
        for rest_configs_item_data in _rest_configs:
            rest_configs_item = RestConfig.from_dict(rest_configs_item_data)

            rest_configs.append(rest_configs_item)

        max_rest_configs = []
        _max_rest_configs = d.pop("max_rest_configs")
        for max_rest_configs_item_data in _max_rest_configs:
            max_rest_configs_item = RestConfig.from_dict(max_rest_configs_item_data)

            max_rest_configs.append(max_rest_configs_item)

        order = d.pop("order", UNSET)

        comment = d.pop("comment", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ExerciseTypeEnum | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ExerciseTypeEnum(_type_)

        def _parse_class_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_name = _parse_class_name(d.pop("class_name", UNSET))

        config = d.pop("config", UNSET)

        def _parse_repetition_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        repetition_unit = _parse_repetition_unit(d.pop("repetition_unit", UNSET))

        def _parse_repetition_rounding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repetition_rounding = _parse_repetition_rounding(
            d.pop("repetition_rounding", UNSET)
        )

        def _parse_weight_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        weight_unit = _parse_weight_unit(d.pop("weight_unit", UNSET))

        def _parse_weight_rounding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weight_rounding = _parse_weight_rounding(d.pop("weight_rounding", UNSET))

        slot_entry_structure = cls(
            id=id,
            slot=slot,
            exercise=exercise,
            repetitions_configs=repetitions_configs,
            max_repetitions_configs=max_repetitions_configs,
            weight_configs=weight_configs,
            max_weight_configs=max_weight_configs,
            set_nr_configs=set_nr_configs,
            max_set_nr_configs=max_set_nr_configs,
            rir_configs=rir_configs,
            max_rir_configs=max_rir_configs,
            rest_configs=rest_configs,
            max_rest_configs=max_rest_configs,
            order=order,
            comment=comment,
            type_=type_,
            class_name=class_name,
            config=config,
            repetition_unit=repetition_unit,
            repetition_rounding=repetition_rounding,
            weight_unit=weight_unit,
            weight_rounding=weight_rounding,
        )

        slot_entry_structure.additional_properties = d
        return slot_entry_structure

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
