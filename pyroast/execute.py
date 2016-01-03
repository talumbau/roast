# -*- coding: utf-8 -*-

import time
import freshroastsr700
from .roaster import Roaster

def roast_recipe(recipe):

    # Create a roaster object.
    r = Roaster(steps=recipe['steps'])

    # Set variables.
    r.initialize()
    #r.roaster.target_temp = 320
    #r.roaster.fan_speed = 9
    #r.roaster.time_remaining = 120

    print("just before starting the roast ...")
    # Begin roasting.
    print("just before starting ", time.time())
    r.roast()

    print("got to after the roast...")
    # This ensures the example script does not end before the roast.
    print("got to after the roast ", time.time())
    time.sleep(r.recipe_time + 20)
    print("got to after sleep", time.time())

    # Disconnect from the roaster.
    r.roaster.disconnect()
