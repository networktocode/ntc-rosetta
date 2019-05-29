import click

from ntc_rosetta.yang import get_data_model


@click.command("print-model")
@click.pass_context
def print_model(ctx: click.Context) -> None:
    """
    Prints the model as an ASCII tree
    """
    print(get_data_model().ascii_tree())


def add_commands(cli: click.Group) -> None:
    cli.add_command(print_model)
