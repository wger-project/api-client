# wger-api-client

Typed Python client for the [wger](https://github.com/wger-project/wger) workout
manager REST API, generated from the server's OpenAPI schema with
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
Built on `httpx`, with a sync and an async call for every endpoint.

Note that this is still new, if you encounter any problems, please contact us.

## Install

```bash
pip install wger-api-client
```

### Versioning

The major and minor version indicate which wger release this client targets, so
`2.6.x` is meant for a 2.6 server.

Since we try to keep the API as compatible as possible, an older client generally
keeps working against a newer server, specially for endpoints such as the exercises.
However, it is recommended that you use the version that exactly matches the server
you want to connect to.

## Usage

Every endpoint has its own module under `wger_api_client.api.<tag>`, and each of
those exposes four functions:

| Function | Returns |
|---|---|
| `sync` | the parsed body, or `None` |
| `sync_detailed` | a `Response` with status code, headers and the parsed body |
| `asyncio` | as `sync`, awaitable |
| `asyncio_detailed` | as `sync_detailed`, awaitable |

With an API key from `/en/user/api-key`:

```python
from wger_api_client import AuthenticatedClient
from wger_api_client.api.routine import routine_list

with AuthenticatedClient(
    base_url="https://wger.de", token="<api key>", prefix="Token"
) as client:
    page = routine_list.sync(client=client)
    for routine in page.results:
        print(routine.id, routine.name)
```

With a JWT access token, which is the same call with a different prefix:

```python
client = AuthenticatedClient(
    base_url="https://wger.de", token="<access token>", prefix="Bearer"
)
```

Unauthenticated endpoints, such as the exercise database, work with the plain
`Client`:

```python
from wger_api_client import Client
from wger_api_client.api.exercise import exercise_list

with Client(base_url="https://wger.de") as client:
    page = exercise_list.sync(client=client)
```

By default a non-2xx response returns `None` from `sync`. Pass
`raise_on_unexpected_status=True` to the client to get an
`errors.UnexpectedStatus` exception instead.

## Development

The generated package under `wger_api_client/` is checked in, so that a schema
change shows up as a reviewable diff. Do not edit it by hand.

Updating the client after the server's API changed is two steps, refresh the
schema and regenerate from it. The schema is read from a running wger instance,
by default the upstream one at https://wger.de:

```bash
# 1. refresh schema/wger-openapi.yaml
uv run scripts/sync_schema.py [--base-url https://my.server]

# 2. regenerate the client from the refreshed schema
./scripts/generate.sh

uv run pytest
```

To pick up API changes that are not released yet, point it at a local instance
(`./manage.py runserver` in the server checkout) with `--base-url` or
`$WGER_BASE_URL`:

```bash
uv run scripts/sync_schema.py --base-url http://localhost:8000
```

Then commit both diffs together. A schema that moved without a regenerated
client is exactly what CI rejects.

Two things to keep in mind when refreshing:

The instance must be backed by **PostgreSQL**, the way real deployments are.
Django derives the bounds of its integer fields from the database backend, so
the schema is backend-dependent. The default instance already satisfies this,
so it only matters when syncing from a local checkout configured for SQLite.

Also note that the schema endpoint does not report the warnings that
`./manage.py spectacular` prints on the server side. Those warnings mean the schema
might be misdescribing the  API somewhere, and the mistake gets baked into the
client, so check them in the server checkout whenever its serializers changed.

To verify without changing anything:

```bash
# does the committed client still match the committed schema?
./scripts/generate.sh --check

# has the server's schema moved since the snapshot was taken?
uv run scripts/sync_schema.py --check
```

`tests/test_contract.py` pins the parts of the contract that are easy to get
wrong when the calls are written by hand: which endpoints are read-only, which
methods each URL allows, the valid enum values and the writable field sets.

`tests/test_smoke_live.py` runs against a real instance and is skipped unless
`WGER_SMOKE_URL` and `WGER_SMOKE_TOKEN` are set.

## License

Apache-2.0, see [LICENSE.txt](LICENSE.txt) and [NOTICE](NOTICE).

The wger server itself is AGPL-3.0-or-later. This client is licensed
permissively so that it can be used as an ordinary dependency. The endpoint and
field descriptions carried in the generated docstrings come from the server's
source code and are attributed in the NOTICE file.
