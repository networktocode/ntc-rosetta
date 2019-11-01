import json
import pathlib
import sys
from typing import Tuple

import click

from ntc_rosetta.yang import get_data_model

from yangify import linter


ERROR_CODE_HELP = "\n".join(
    [f"  - {k}: {v[1]}\n" for k, v, in linter.MessageType.help().items()]
)

LINT_HELP = f"""Lint files/folders with Parsers/Translators:

Errors/Warning message codes:

{ERROR_CODE_HELP}
"""


@click.command("lint", help=LINT_HELP)
@click.option("-i", "--ignore", multiple=True, help="ignore error/warning codes")
@click.option(
    "-m",
    "--model",
    default="openconfig",
    type=click.Choice(["openconfig", "ntc"]),
    help="model to lint",
)
@click.option("-j/-t", "--json/--text", "to_json", default=False, help="output format")
@click.argument("filepaths", nargs=-1)
@click.pass_context
def lint(
    ctx: click.Context,
    filepaths: Tuple[str],
    ignore: Tuple[str],
    to_json: bool,
    model: str,
) -> None:
    failed = False
    if not filepaths:
        filepaths = (".",)
    for filepath in filepaths:
        path = pathlib.Path(f"{filepath}")
        lint = linter.Linter.lint(path, get_data_model(model), ignore=ignore)
        if to_json:
            text = json.dumps(lint.serialize(), indent=4)
        else:
            text = lint.to_text()
        failed = failed or bool(text)
        print(text, end="")
    if failed:
        sys.exit(1)


def add_commands(cli: click.Group) -> None:
    cli.add_command(lint)
