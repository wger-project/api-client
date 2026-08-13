#!/usr/bin/env python3
"""Join ``explode: false`` array query parameters with commas.

openapi-python-client ignores a parameter's ``explode`` attribute and always
hands the list to httpx, which repeats the parameter. wger declares its
``*__in`` filters as ``style: form, explode: false``, and Django's
``QueryDict.get`` keeps only the last repetition, so ``id__in=[9, 12, 13]``
filters on 13 alone. No error, just the wrong result set.

The schema decides which parameters are affected, not the ``__in`` suffix: they
are exactly the ones declared ``explode: false``.

Delete this script and its call in generate.sh once the generator handles
explode. https://github.com/openapi-generators/openapi-python-client/pull/1296

Usage:
    scripts/patch_generated.py <schema> <package directory>
"""

import re
import sys
from pathlib import Path

from ruamel.yaml import YAML

# What the generator emits for an array parameter, anchored on the parameter
# name so a module with several of them is rewritten one at a time.

# Items that already serialize themselves: the list is passed through
PASSED_THROUGH = (
    r"    json_(?P<var>\w+): list\[\w+\] \| Unset = UNSET\n"
    r"    if not isinstance\((?P=var), Unset\):\n"
    r"        json_(?P=var) = (?P=var)\n"
    r"\n"
    r'    params\["{name}"\] = json_(?P=var)\n'
)

# Items that do not, UUIDs for instance: a converted copy is built. Only str()
# counts, so joining the originals gives the same string. Another conversion,
# say .isoformat(), does not match and the count check below reports it.
CONVERTED = (
    r"    json_(?P<var>\w+): list\[\w+\] \| Unset = UNSET\n"
    r"    if not isinstance\((?P=var), Unset\):\n"
    r"        json_(?P=var) = \[\]\n"
    r"        for (?P=var)_item_data in (?P=var):\n"
    r"            (?P=var)_item = str\((?P=var)_item_data\)\n"
    r"            json_(?P=var)\.append\((?P=var)_item\)\n"
    r"\n"
    r'    params\["{name}"\] = json_(?P=var)\n'
)

JOINED = """    json_{var}: str | Unset = UNSET
    if not isinstance({var}, Unset):
        json_{var} = ",".join(str(v) for v in {var})

    params["{name}"] = json_{var}
"""


def non_exploded(schema: Path) -> list[tuple[str, str]]:
    """(operation id, parameter name) of every array query parameter to join"""
    doc = YAML(typ="safe").load(schema)
    return [
        (operation["operationId"], param["name"])
        for operations in doc["paths"].values()
        for operation in operations.values()
        if isinstance(operation, dict)
        for param in operation.get("parameters", [])
        if param.get("in") == "query"
        and param.get("schema", {}).get("type") == "array"
        # style: form defaults to explode: true, so only an explicit false counts
        and param.get("explode") is False
    ]


def patch(module: Path, name: str) -> bool:
    """Rewrite one parameter of one generated module"""
    src = module.read_text()
    for block in (PASSED_THROUGH, CONVERTED):
        match = re.search(block.format(name=re.escape(name)), src)
        if match:
            break
    else:
        return False

    module.write_text(
        src[: match.start()]
        + JOINED.format(var=match.group("var"), name=name)
        + src[match.end() :]
    )
    return True


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)

    schema, package = Path(sys.argv[1]), Path(sys.argv[2])
    if not schema.is_file():
        sys.exit(f"not a file: {schema}")
    if not package.is_dir():
        sys.exit(f"not a directory: {package}")

    joined = non_exploded(schema)
    patched = 0
    for operation, name in joined:
        modules = list(package.rglob(f"{operation}.py"))
        if len(modules) != 1:
            sys.exit(f"expected one module for {operation}, found {modules}")
        patched += patch(modules[0], name)

    if patched != len(joined):
        sys.exit(
            f"joined {patched} of {len(joined)} parameters. Either the generator "
            f"changed the shape of the code this rewrites, or it handles explode "
            f"itself now and the script can go."
        )
    print(f"comma-joined {patched} non-exploded query parameters")


if __name__ == "__main__":
    main()
