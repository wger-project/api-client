#!/usr/bin/env python3
"""Sync the wger OpenAPI snapshot.

The snapshot at ``schema/wger-openapi.yaml`` is the contract this client is
generated from. Refresh it when wger's serializers change, then run
``scripts/generate.sh`` and commit both diffs together.

Usage:
    # Default: fetch from $WGER_BASE_URL (or localhost) and overwrite the snapshot.
    uv run python scripts/sync_schema.py

    # CI mode: fetch and compare; exit 1 (with a diff) on mismatch.
    uv run python scripts/sync_schema.py --check
"""

import argparse
import difflib
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

SNAPSHOT = Path(__file__).parent.parent / "schema" / "wger-openapi.yaml"
DEFAULT_BASE = "https://wger.de"
MAX_DIFF_LINES = 200


def fetch(base_url: str) -> bytes:
    url = f"{base_url.rstrip('/')}/api/v2/schema"
    req = urllib.request.Request(
        url, headers={"User-Agent": "wger-api-client-sync/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read()
    except urllib.error.URLError as e:
        sys.exit(f"failed to fetch {url}: {e}")


def main() -> None:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--check",
        action="store_true",
        help="Compare against the snapshot and exit non-zero on mismatch.",
    )
    p.add_argument(
        "--base-url",
        default=os.environ.get("WGER_BASE_URL", DEFAULT_BASE),
        help="wger base URL (default: $WGER_BASE_URL or %(default)s).",
    )
    args = p.parse_args()

    source = f"{args.base_url}/api/v2/schema"
    fresh = fetch(args.base_url)

    if args.check:
        if not SNAPSHOT.exists():
            sys.exit(f"snapshot missing: {SNAPSHOT}, run without --check first.")
        current = SNAPSHOT.read_bytes()
        if fresh == current:
            print(f"OK, snapshot matches {source} ({len(fresh):,} bytes)")
            return
        diff = list(
            difflib.unified_diff(
                current.decode().splitlines(keepends=True),
                fresh.decode().splitlines(keepends=True),
                fromfile=SNAPSHOT.name,
                tofile=source,
                n=3,
            )
        )
        sys.stdout.write("".join(diff[:MAX_DIFF_LINES]))
        if len(diff) > MAX_DIFF_LINES:
            print(f"\n... and {len(diff) - MAX_DIFF_LINES} more lines.")
        sys.exit(f"\nsnapshot drift detected ({len(diff)} diff lines)")

    SNAPSHOT.write_bytes(fresh)
    print(f"wrote {len(fresh):,} bytes -> {SNAPSHOT}")


if __name__ == "__main__":
    main()
