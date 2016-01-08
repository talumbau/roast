import click
import time
from ..utils import cup_text1, cup_text2, done_text
import mock
from ..reader import read_recipe
from ..roaster import Roaster
import mock

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


def count_steps(roaster, step_num):
    while True:
        time.sleep(1.0)
        if roaster.current_step > step_num:
            return


def create_roaster(steps, fake=True):
    r = Roaster(steps=steps)
    r.initialize()
    #r._roaster.roast.side_effect = r.next_state
    if fake:
        r._roaster.roast.side_effect = r.next_state
    return r


@click.command()
@click.option('--cool', default=90, help='')
@click.argument('recipe', type=click.Path(exists=True))
@click.option('--fake', is_flag=True, help="process script but don't roast")
@click.version_option()
def cli(recipe, cool, fake):

    fake=False
    click.clear()
    steps = 1

    if recipe:
        recipe = read_recipe(recipe)
        steps = recipe['steps']
        if fake:
            #Mock the freshroastsr700 object
            with mock.patch('pyroast.roaster.freshroastsr700.freshroastsr700') as mock_fr:
                r = create_roaster(steps, fake)
        else:
            r = create_roaster(steps, False)

    r.roast()

    with click.progressbar(length=len(steps), label='Roasting...',
                           bar_template='%(label)s  %(bar)s | %(info)s',
                           fill_char=click.style(u'█', fg='cyan'),
                           empty_char=' ') as bar:
        for count, item in enumerate(bar):
            #print("counting now", len(steps), count)
            count_steps(r, count)

    time.sleep(2)

    click.clear()
    click.echo(OKGREEN + done_text + ENDC)
    click.echo(h4 + cup_text1 + ENDC, nl=False)
    click.echo(h1 + cup_text2 + ENDC)
    r.done()


if __name__ == "__main__":
    cli()
