import click

@click.command()
def hello():
    click.echo("hello world!")


if __name__ == "__main__":
    hello()
