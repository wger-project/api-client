from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.chart_type_enum import ChartTypeEnum, check_chart_type_enum
from ..models.dynamic_type_enum import DynamicTypeEnum, check_dynamic_type_enum
from ..models.metric_type_enum import MetricTypeEnum, check_metric_type_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedCategoryRequest")


@_attrs_define
class PatchedCategoryRequest:
    """Measurement category serializer

    Attributes:
        id (UUID | Unset):
        name (str | Unset):
        unit (str | Unset):
        metric_type (MetricTypeEnum | Unset): * `custom` - Custom
            * `body_weight` - Body Weight
            * `body_fat` - Body Fat
            * `lean_body_mass` - Lean Body Mass
            * `height` - Height
            * `blood_pressure` - Blood Pressure
            * `blood_pressure_systolic` - Blood Pressure Systolic
            * `blood_pressure_diastolic` - Blood Pressure Diastolic
            * `heart_rate` - Heart Rate
            * `resting_heart_rate` - Resting Heart Rate
            * `blood_oxygen` - Blood Oxygen
            * `steps` - Steps
            * `distance` - Distance
            * `energy` - Energy
            * `sleep` - Sleep
            * `sleep_total` - Total sleep
            * `sleep_light` - Light sleep
            * `sleep_deep` - Deep sleep
            * `sleep_rem` - REM sleep
            * `sleep_awake` - Awake
        chart_type (BlankEnum | ChartTypeEnum | None | Unset):
        chart_config (Any | Unset):
        parent (None | Unset | UUID):
        order (int | Unset):
        dynamic_type (DynamicTypeEnum | Unset): * `NONE` - None
            * `BMI` - BMI
            * `WHTR` - Waist-to-height ratio
            * `ONE_REP_MAX` - 1RM
            * `ONE_RM_TOTAL` - 1RM total
        dynamic_params (Any | Unset): Configuration parameters for dynamic calculations
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    unit: str | Unset = UNSET
    metric_type: MetricTypeEnum | Unset = UNSET
    chart_type: BlankEnum | ChartTypeEnum | None | Unset = UNSET
    chart_config: Any | Unset = UNSET
    parent: None | Unset | UUID = UNSET
    order: int | Unset = UNSET
    dynamic_type: DynamicTypeEnum | Unset = UNSET
    dynamic_params: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        unit = self.unit

        metric_type: str | Unset = UNSET
        if not isinstance(self.metric_type, Unset):
            metric_type = self.metric_type

        chart_type: None | str | Unset
        if isinstance(self.chart_type, Unset):
            chart_type = UNSET
        elif isinstance(self.chart_type, str) or isinstance(self.chart_type, str):
            chart_type = self.chart_type
        else:
            chart_type = self.chart_type

        chart_config = self.chart_config

        parent: None | str | Unset
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, UUID):
            parent = str(self.parent)
        else:
            parent = self.parent

        order = self.order

        dynamic_type: str | Unset = UNSET
        if not isinstance(self.dynamic_type, Unset):
            dynamic_type = self.dynamic_type

        dynamic_params = self.dynamic_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if unit is not UNSET:
            field_dict["unit"] = unit
        if metric_type is not UNSET:
            field_dict["metric_type"] = metric_type
        if chart_type is not UNSET:
            field_dict["chart_type"] = chart_type
        if chart_config is not UNSET:
            field_dict["chart_config"] = chart_config
        if parent is not UNSET:
            field_dict["parent"] = parent
        if order is not UNSET:
            field_dict["order"] = order
        if dynamic_type is not UNSET:
            field_dict["dynamic_type"] = dynamic_type
        if dynamic_params is not UNSET:
            field_dict["dynamic_params"] = dynamic_params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        unit = d.pop("unit", UNSET)

        _metric_type = d.pop("metric_type", UNSET)
        metric_type: MetricTypeEnum | Unset
        if isinstance(_metric_type, Unset):
            metric_type = UNSET
        else:
            metric_type = check_metric_type_enum(_metric_type)

        def _parse_chart_type(data: object) -> BlankEnum | ChartTypeEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chart_type_type_0 = check_chart_type_enum(data)

                return chart_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                chart_type_type_1 = check_blank_enum(data)

                return chart_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | ChartTypeEnum | None | Unset, data)

        chart_type = _parse_chart_type(d.pop("chart_type", UNSET))

        chart_config = d.pop("chart_config", UNSET)

        def _parse_parent(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_type_0 = UUID(data)

                return parent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent = _parse_parent(d.pop("parent", UNSET))

        order = d.pop("order", UNSET)

        _dynamic_type = d.pop("dynamic_type", UNSET)
        dynamic_type: DynamicTypeEnum | Unset
        if isinstance(_dynamic_type, Unset):
            dynamic_type = UNSET
        else:
            dynamic_type = check_dynamic_type_enum(_dynamic_type)

        dynamic_params = d.pop("dynamic_params", UNSET)

        patched_category_request = cls(
            id=id,
            name=name,
            unit=unit,
            metric_type=metric_type,
            chart_type=chart_type,
            chart_config=chart_config,
            parent=parent,
            order=order,
            dynamic_type=dynamic_type,
            dynamic_params=dynamic_params,
        )

        patched_category_request.additional_properties = d
        return patched_category_request

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
