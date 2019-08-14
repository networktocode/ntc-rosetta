import json

import click

from ntc_rosetta import get_driver
from ntc_rosetta.yang import get_data_model

from yangify import linter


@click.command("print-parser")
@click.option("-j/-t", "--json/--text", "to_json", default=False, help="output format")
@click.argument("driver")
@click.option(
    "-m",
    "--model",
    default="openconfig",
    type=click.Choice(["openconfig", "ntc"]),
    help="model to lint",
)
@click.pass_context
def print_parser(ctx: click.Context, driver: str, model: str, to_json: bool) -> None:
    """
    Prints a tree representation of a parser/translator.

    Parser/Translator needs to be properly linted for this to work
    """
    d = get_driver(driver, model)
    dm = get_data_model(model)
    lint = linter.Linter.lint(d.parser, dm, recursive=True)
    if to_json:
        text = json.dumps(lint.to_dict(), indent=4)
    else:
        text = lint.to_ascii_tree("")
    print(text)


def add_commands(cli: click.Group) -> None:
    cli.add_command(print_parser)
