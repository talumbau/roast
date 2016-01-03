import pytest
import tempfile
import os
from pyroast import read_recipe

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

def test_read_recipe(recipefile):
    r = read_recipe(recipefile.name)
    assert len(r['steps']) == 2
 
