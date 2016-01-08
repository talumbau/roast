import pytest
import tempfile
import os
import mock
from pyroast import read_recipe, Roaster

test_recipe = """
{
    "creator": "John Smith",
    "roastName": "French Roast",
    "steps": [
        {
            "targetTemp": 250,
            "fanSpeed": 9,
            "sectionTime": 30
        },
        {
            "cooling": true,
            "fanSpeed": 9,
            "sectionTime": 180
        }
    ],
    "bean": {
        "region": "N/A",
        "source": {
            "reseller": "Sweet Maria's",
            "link": ""
        },
        "country": "N/A"
    },
    "totalTime": 210,
    "roastDescription": {
        "roastType": "the type of roast",
        "description": "a description"
    }
}
"""

@pytest.yield_fixture
def recipefile():

    f = tempfile.NamedTemporaryFile(mode="a", delete=False)
    f.write(test_recipe + "\n")
    f.close()
    # Must close and then yield for Windows platform
    yield f
    os.remove(f.name)


@mock.patch('pyroast.roaster.freshroastsr700.freshroastsr700')
def test_make_Roaster(mock_fr, recipefile):
    mock_fr.connected.return_value = True
    recipe = read_recipe(recipefile.name)
    len(recipe['steps']) == 2
    r = Roaster(recipe['steps'])
    r.initialize()
    assert r


@mock.patch('pyroast.roaster.freshroastsr700.freshroastsr700')
def test_Roaster_recipe_time(mock_fr, recipefile):
    mock_fr.connected.return_value = True
    recipe = read_recipe(recipefile.name)
    r = Roaster(recipe['steps'])
    assert r.recipe_time == 215


@mock.patch('pyroast.roaster.freshroastsr700.freshroastsr700')
def test_Roaster_roast(mock_fr, recipefile):
    mock_fr.connected.return_value = True
    recipe = read_recipe(recipefile.name)
    r = Roaster(recipe['steps'])
    r.initialize()
    r._roaster.roast.side_effect = r.next_state
    r.roast()
    assert r



