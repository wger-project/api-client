"""
Checks that the generated client encodes the parts of the API contract that are
easy to get wrong when the REST calls are hand-written: read-only endpoints,
allowed methods per URL, valid enum values and the set of writable fields.
"""

import dataclasses
import importlib
import inspect
from pathlib import Path

import pytest

PACKAGE = Path(__file__).parent.parent / "wger_api_client"


def operations(tag: str) -> set[str]:
    """Names of the generated operation modules for one API tag"""
    return {
        p.stem for p in (PACKAGE / "api" / tag).glob("*.py") if p.stem != "__init__"
    }


def fields(model) -> set[str]:
    if dataclasses.is_dataclass(model):
        return {f.name for f in dataclasses.fields(model)}
    return {a.name for a in model.__attrs_attrs__}


def test_equipment_is_read_only():
    assert operations("equipment") == {"equipment_list", "equipment_retrieve"}


def test_workout_endpoint_does_not_exist():
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("wger_api_client.api.workout")


def test_userprofile_list_url_has_no_patch():
    """Profile updates go through POST on the list URL, not PATCH"""
    ops = operations("userprofile")
    assert "userprofile_create" in ops
    assert "userprofile_patch" not in ops


def test_userprofile_list_returns_a_single_object():
    from wger_api_client.api.userprofile import userprofile_list
    from wger_api_client.models import Userprofile

    annotation = inspect.signature(userprofile_list.sync).return_annotation
    assert Userprofile.__name__ in str(annotation)
    assert "Paginated" not in str(annotation)


def test_day_type_rejects_invalid_choices():
    from wger_api_client.models import DayTypeEnum

    assert {e.value for e in DayTypeEnum} == {
        "custom",
        "enom",
        "amrap",
        "hiit",
        "tabata",
        "edt",
        "rft",
        "afap",
    }
    with pytest.raises(ValueError):
        DayTypeEnum("standard")


def test_day_can_be_filtered_by_routine():
    from wger_api_client.api.day import day_list

    assert "routine" in inspect.signature(day_list.sync).parameters


def test_slot_has_no_sets_or_rest_fields():
    """Sets and rest live on the config endpoints, not on the slot itself"""
    from wger_api_client.models import SlotRequest

    assert not {"sets", "rest"} & fields(SlotRequest)


def test_routine_actions_have_their_own_response_types():
    from wger_api_client.api.routine import (
        routine_logs_list,
        routine_stats_retrieve,
        routine_structure_retrieve,
    )

    expected = {
        routine_structure_retrieve: "RoutineStructure",
        routine_logs_list: "LogDisplay",
        routine_stats_retrieve: "LogStatsData",
    }
    for module, model in expected.items():
        annotation = str(inspect.signature(module.sync).return_annotation)
        assert model in annotation, f"{module.__name__} returns {annotation}"
