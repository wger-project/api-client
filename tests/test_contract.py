"""
Checks that the generated client encodes the parts of the API contract that are
easy to get wrong when the REST calls are hand-written: read-only endpoints,
allowed methods per URL, valid enum values, the set of writable fields and how
list filters end up in the query string.
"""

import dataclasses
import importlib
import inspect
import pkgutil
from pathlib import Path

import httpx
import pytest
from ruamel.yaml import YAML

PACKAGE = Path(__file__).parent.parent / "wger_api_client"
SCHEMA = Path(__file__).parent.parent / "schema" / "wger-openapi.yaml"


def operations(tag: str) -> set[str]:
    """Names of the generated operation modules for one API tag"""
    return {
        p.stem for p in (PACKAGE / "api" / tag).glob("*.py") if p.stem != "__init__"
    }


def fields(model) -> set[str]:
    if dataclasses.is_dataclass(model):
        return {f.name for f in dataclasses.fields(model)}
    return {a.name for a in model.__attrs_attrs__}


def test_every_module_imports():
    """
    Importing part of the package is not enough to catch a missing import in an
    annotation: Python 3.14 evaluates annotations lazily, so a broken module only
    fails on 3.11 to 3.13, and only once it is actually imported.
    """
    import wger_api_client

    failed = {}
    for module in pkgutil.walk_packages(wger_api_client.__path__, "wger_api_client."):
        try:
            importlib.import_module(module.name)
        except Exception as e:  # noqa: BLE001 - any import failure counts
            failed[module.name] = f"{type(e).__name__}: {e}"

    assert not failed, (
        f"{len(failed)} modules fail to import: {sorted(failed.items())[:3]}"
    )


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
    from wger_api_client.models.day_type_enum import (
        DAY_TYPE_ENUM_VALUES,
        check_day_type_enum,
    )

    assert DAY_TYPE_ENUM_VALUES == {
        "custom",
        "enom",
        "amrap",
        "hiit",
        "tabata",
        "edt",
        "rft",
        "afap",
    }
    with pytest.raises(TypeError):
        check_day_type_enum("standard")


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


def query(operation: str, **kwargs) -> httpx.QueryParams:
    """The query string one operation builds, decoded"""
    module = importlib.import_module(f"wger_api_client.api.{operation}")
    request = module._get_kwargs(**kwargs)
    return httpx.Request(
        request["method"],
        "http://wger.local" + request["url"],
        params=request["params"],
    ).url.params


def array_parameters() -> list[tuple[str, str, bool]]:
    """(operation id, parameter name, joined) for every array query parameter"""
    doc = YAML(typ="safe").load(SCHEMA)
    return [
        (operation["operationId"], param["name"], param.get("explode") is False)
        for operations in doc["paths"].values()
        for operation in operations.values()
        if isinstance(operation, dict)
        for param in operation.get("parameters", [])
        if param.get("in") == "query" and param.get("schema", {}).get("type") == "array"
    ]


ARRAY_PARAMETERS = array_parameters()


def test_in_filter_is_sent_as_one_comma_separated_value():
    assert query("ingredient.ingredient_list", id_in=[9, 12, 13]).get_list(
        "id__in"
    ) == ["9,12,13"]


def test_multiple_choice_filter_is_sent_repeated():
    assert query("exercise.exercise_list", equipment=[1, 3]).get_list("equipment") == [
        "1",
        "3",
    ]


@pytest.mark.parametrize(
    "operation,name,joined",
    ARRAY_PARAMETERS,
    ids=[f"{o}-{n}" for o, n, _ in ARRAY_PARAMETERS],
)
def test_array_parameter_matches_the_serialization_in_the_schema(
    operation, name, joined
):
    tag = next(p.parent.name for p in PACKAGE.rglob(f"{operation}.py"))
    values = query(f"{tag}.{operation}", **{name.replace("__", "_"): [1, 2]}).get_list(
        name
    )
    assert values == (["1,2"] if joined else ["1", "2"])
