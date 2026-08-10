"""
Smoke test against a running wger instance.

Skipped unless WGER_SMOKE_URL and WGER_SMOKE_TOKEN are set, e.g.:

    WGER_SMOKE_URL=http://localhost:8000 \
    WGER_SMOKE_TOKEN=<api key from /en/user/api-key> \
    uv run pytest tests/test_smoke_live.py
"""

import os

import pytest

URL = os.environ.get("WGER_SMOKE_URL")
TOKEN = os.environ.get("WGER_SMOKE_TOKEN")

pytestmark = pytest.mark.skipif(
    not (URL and TOKEN),
    reason="WGER_SMOKE_URL and WGER_SMOKE_TOKEN are not set",
)


@pytest.fixture
def client():
    from wger_api_client import AuthenticatedClient

    with AuthenticatedClient(base_url=URL, token=TOKEN, prefix="Token") as c:
        yield c


def test_userprofile_parses_as_a_single_object(client):
    from wger_api_client.api.userprofile import userprofile_list
    from wger_api_client.models import Userprofile

    profile = userprofile_list.sync(client=client)
    assert isinstance(profile, Userprofile)


def test_routine_list_parses(client):
    from wger_api_client.api.routine import routine_list

    page = routine_list.sync(client=client)
    assert page is not None
    assert isinstance(page.count, int)


def test_day_routine_filter_is_applied(client):
    from wger_api_client.api.day import day_list
    from wger_api_client.api.routine import routine_list

    routines = routine_list.sync(client=client)
    if not routines.results:
        pytest.skip("the account has no routines")

    routine_id = routines.results[0].id
    days = day_list.sync(client=client, routine=routine_id)
    assert {d.routine for d in days.results} <= {routine_id}
