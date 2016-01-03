import click
import time
from ..utils import cup_text1, cup_text2, done_text

h1 = '\033[97m'
h2 = '\033[96m'
HEADER = '\033[95m'
OKBLUE = '\033[94m'
WARNING = '\033[93m'
OKGREEN = '\033[92m'
h3 = '\033[91m'
h4 = '\033[90m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def pause(a):
    time.sleep(a)

@click.command()
@click.option('--cool', default=90, help='')
@click.argument('recipe', type=click.Path(exists=True))
@click.option('--fake', is_flag=True, help="process script but don't roast")
@click.version_option()
def cli(recipe, cool, fake):
    click.clear()
    steps = [0.02]*8
    with click.progressbar(length=len(steps), label='Roasting...',
                           bar_template='%(label)s  %(bar)s | %(info)s',
                           fill_char=click.style(u'█', fg='cyan'),
                           empty_char=' ') as bar:
        for item in bar:
            pause(0.4)

    click.echo(done_text)
    click.echo(h4 + cup_text1 + ENDC, nl=False)
    click.echo(h1 + cup_text2 + ENDC)


if __name__ == "__main__":
    cli()
