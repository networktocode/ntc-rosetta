import click

from ntc_rosetta.cli import linter, print_model, print_processor


@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    pass


def run() -> None:
    cli(obj={})


linter.add_commands(cli)
print_model.add_commands(cli)
print_processor.add_commands(cli)


if __name__ == "__main__":
    run()
