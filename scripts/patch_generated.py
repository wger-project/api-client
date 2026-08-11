#!/usr/bin/env python3
"""Add the ``Unset`` import that the generator leaves out.

For an operation whose request body is *required*, openapi-python-client
annotates the body as ``X | Unset`` but does not import ``Unset``. The module
then raises ``NameError`` on import under Python 3.10 to 3.13, which evaluate
annotations eagerly. Python 3.14 evaluates them lazily and hides the problem

Not a formatting or ruff issue. Generating with ``post_hooks: []`` produces the
same missing import, so the generator itself never emits it.

Delete this script and its call in generate.sh once the issue upstream is fixed.
https://github.com/openapi-generators/openapi-python-client/issues/1451

Usage:
    scripts/patch_generated.py <package directory>
"""

import re
import sys
from pathlib import Path

TYPES_IMPORT = re.compile(r"^from (\.+)types import (.+)$", re.MULTILINE)


def patch(path: Path) -> bool:
    """Add Unset to the types import of one module, if it is used but missing"""
    src = path.read_text()
    match = TYPES_IMPORT.search(src)
    if not match:
        return False

    names = [n.strip() for n in match.group(2).split(",")]
    if "Unset" in names:
        return False

    # Look outside the import line itself, so the name in it does not count
    if not re.search(r"\bUnset\b", TYPES_IMPORT.sub("", src)):
        return False

    # isort's order_by_type: constants first, then classes alphabetically. The
    # modules that do import Unset show the same order, so the result matches
    # what the generator emits elsewhere.
    constants = [n for n in names if n.isupper()]
    classes = sorted([n for n in names if not n.isupper()] + ["Unset"])
    replacement = f"from {match.group(1)}types import {', '.join(constants + classes)}"

    path.write_text(src[: match.start()] + replacement + src[match.end() :])
    return True


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)

    package = Path(sys.argv[1])
    if not package.is_dir():
        sys.exit(f"not a directory: {package}")

    patched = [p for p in sorted(package.rglob("*.py")) if patch(p)]
    print(f"added the missing Unset import to {len(patched)} modules")


if __name__ == "__main__":
    main()
