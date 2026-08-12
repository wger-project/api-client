#!/usr/bin/env bash
#
# Regenerate the client from schema/wger-openapi.yaml.
#
# The generated package is checked in, so run this after refreshing the schema
# and commit the diff. CI runs it with --check to catch a schema that was
# updated without regenerating.
#
# Usage:
#   scripts/generate.sh            regenerate in place
#   scripts/generate.sh --check    fail if the result differs from what is committed

set -euo pipefail

cd "$(dirname "$0")/.."

PACKAGE=wger_api_client
SCHEMA=schema/wger-openapi.yaml

if ! command -v uv >/dev/null 2>&1; then
    echo 'uv not found. Install it: https://docs.astral.sh/uv/' >&2
    exit 1
fi

generate() {
    local target=$1
    # The generator comes from the dev dependency group, so uv.lock fixes its
    # version and the version of the ruff it formats the output with. Running it
    # with uvx instead would resolve both freshly every time, and the generated
    # code would change whenever either released.
    #
    # --meta none emits only the package directory, leaving the hand-written
    # pyproject.toml, README and tests alone.
    uv run --quiet openapi-python-client generate \
        --path "$SCHEMA" \
        --config openapi-config.yml \
        --meta none \
        --output-path "$target" \
        --overwrite
    # --meta none skips py.typed, but consumers need it to see the annotations
    touch "$target/py.typed"
    # the generator formats with ruff and leaves its cache behind
    rm -rf "$target/.ruff_cache"
}

if [[ ${1:-} == --check ]]; then
    tmp=$(mktemp -d)
    trap 'rm -rf "$tmp"' EXIT
    # the generator reads requires-python from the nearest pyproject.toml to choose
    # between typing.Self and typing_extensions.Self, so the temporary tree needs
    # the same one or every model differs
    cp pyproject.toml "$tmp/"
    generate "$tmp/$PACKAGE"
    # __pycache__ is a gitignored working-tree artifact, not part of the client
    if ! diff -r -q -x '__pycache__' -x '*.pyc' "$PACKAGE" "$tmp/$PACKAGE"; then
        echo >&2
        echo "The committed client does not match $SCHEMA." >&2
        echo "Run scripts/generate.sh and commit the result." >&2
        exit 1
    fi
    echo "Client is in sync with $SCHEMA."
else
    rm -rf "$PACKAGE"
    generate "$PACKAGE"
    echo "Regenerated $PACKAGE from $SCHEMA."
fi
