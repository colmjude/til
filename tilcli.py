import click

from bin.create_til import create_note


@click.group()
def cli():
    pass


@cli.command(name="new")
@click.option("--name", prompt="Note name", help="The name to use.")
@click.option("--folder", help="The name to use.")
def new(name, folder):
    print(f"Attempting to create note: {name}")
    create_note(name, folder)


if __name__ == "__main__":
    cli()
