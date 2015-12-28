import click

@click.command()
def cli():
    click.echo("hello world!")


if __name__ == "__main__":
    cli()
