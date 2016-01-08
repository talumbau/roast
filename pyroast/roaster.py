# -*- coding: utf-8 -*-

import time
import freshroastsr700

class Roaster(object):
    def __init__(self, steps=[]):
        """Creates a freshroastsr700 object passing in methods included in this
        class."""
        #update_func = self.next_state
        self._roaster = freshroastsr700.freshroastsr700(
            self.update_data, self.next_state, thermostat=True)
        #self._update_func = update_func
        steps.append({"idle": True, "sectionTime": 5})
        self._steps = steps
        self.current_step = -1
        self._iter = iter(self._steps)
        self._verbose = True

    def done(self):
        self._roaster.disconnect()

    def initialize(self):
        """
        Connect to the roaster and set the intial temps
        """
        # Conenct to the roaster.
        self._roaster.auto_connect()

        # Wait for the roaster to be connected.
        while(self._roaster.connected is False):
            print("Please connect your roaster...")
            time.sleep(1)

        # Set the first temp, fan speed, and time
        self.next_state()

    def roast(self):
        """
        Start roasting!
        """
        print("starting to roast")
        self._roaster.roast()

    def update_data(self):
        """This is a method that will be called every time a packet is opened
        from the roaster."""
        print("Current Temperature:", self._roaster.current_temp)

    @property
    def recipe_time(self):
        return sum((s['sectionTime'] for s in self._steps))

    def states(self):
        """This is a generator method that will generate all the states given
        to this Roaster object
        """
        for step in self._steps:
            yield step

    def update_state(self, state):
        if 'targetTemp' in state:

            msg = ("Next Section Time: {st} Fan Speed: {fs}, "
                   "Target Temp: {tt}")
            args = {'st': state['sectionTime'],
                    'fs': state['fanSpeed'],
                    'tt': state['targetTemp']
                   }
            self._roaster.time_remaining = state['sectionTime']
            self._roaster.fan_speed = state['fanSpeed']
            self._roaster.target_temp = state['targetTemp']
            msg = msg.format(**args)

        elif 'cooling' in state:
            assert state['cooling']

            msg = ("Next Section Time: {st} Fan Speed: {fs}, "
                    "Cooling: True")
            args = {'st': state['sectionTime'],
                    'fs': state['fanSpeed'],
                   }
            self._roaster.time_remaining = state['sectionTime']
            self._roaster.fan_speed = state['fanSpeed']
            self._roaster.cool()
            msg = msg.format(**args)

        elif 'idle' in state:
            msg = ("Next Section Idle: True")
            self._roaster.idle()
            self._roaster.time_remaining = 5
            self.current_step += 1

        elif self._roaster.get_roaster_state() == 'idle':
            msg = "Time to quit"
        else:
            raise ValueError("This state is incorrect")

        if self._verbose:
            print(msg)
        self.current_step += 1


    def next_state(self):
        return self.update_state(next(self._iter))
