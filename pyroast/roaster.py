# -*- coding: utf-8 -*-

import time
import freshroastsr700

class Roaster(object):
    def __init__(self, steps=[]):
        """Creates a freshroastsr700 object passing in methods included in this
        class."""
        self.roaster = freshroastsr700.freshroastsr700(
            self.update_data, self.next_state, thermostat=True)
        self._steps = steps
        self._iter = iter(self._steps)

    def __del__(self):
        self.roaster.disconnect()
        pass

    def initialize(self):
        """
        Connect to the roaster and set the intial temps
        """
        # Conenct to the roaster.
        self.roaster.auto_connect()

        # Wait for the roaster to be connected.
        while(self.roaster.connected is False):
            print("Please connect your roaster...")
            time.sleep(1)

        # Set the first temp, fan speed, and time
        self.next_state()

    def roast(self):
        """
        Start roasting!
        """
        self.roaster.roast()

    def update_data(self):
        """This is a method that will be called every time a packet is opened
        from the roaster."""
        print("Current Temperature:", self.roaster.current_temp)

    @property
    def recipe_time(self):
        return sum((s['sectionTime'] for s in self._steps))

    def states(self):
        """This is a generator method that will generate all the states given
        to this Roaster object
        """
        print(time.time())
        for step in self._steps:
            yield step

    def update_state(self, state):
        self.roaster.time_remaining = state['sectionTime']
        self.roaster.fan_speed = state['fanSpeed']
        self.roaster.target_temp = state['targetTemp']


    def next_state(self):
        return self.update_state(next(self._iter))
