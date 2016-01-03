# -*- coding: utf-8 -*-

import time
import freshroastsr700

class Roaster(object):
    def __init__(self, steps=[])
        """Creates a freshroastsr700 object passing in methods included in this
        class."""
        self.roaster = freshroastsr700.freshroastsr700(
            self.update_data, self.next_state, thermostat=True)
        self._steps = steps
        self._iter = iter(self.states)


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

        self.roaster.target_temp = 320
        selfr.roaster.fan_speed = 9
        selfr.roaster.time_remaining = 120

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
    def recipe_time(self)
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


    def next_state():
        return update_state(next(self._iter))

        for step in self._steps():
            self._update_state(step)
            yield


        elif(self.roaster.get_roaster_state() == 'cooling'):
            print("we're switching from cooling to idle", time.time())
            self.roaster.idle()
        else:
            print("the state is ", time.time())
            print("the state is {}".format(self.roaster.get_roaster_state()))


transitions = [240, 240, 360]
fan_transitions = [9, 5, 7]

# Create a roaster object.
r = Roaster(transitions=transitions, fan_transitions=fan_transitions)

# Conenct to the roaster.
r.roaster.auto_connect()

# Wait for the roaster to be connected.
while(r.roaster.connected is False):
    print("Please connect your roaster...")
    time.sleep(1)

# Set variables.
r.roaster.target_temp = 320
r.roaster.fan_speed = 9
r.roaster.time_remaining = 120

print("just before starting the roast ...")
# Begin roasting.
print("just before starting ", time.time())
r.roaster.roast()

print("got to after the roast...")
# This ensures the example script does not end before the roast.
print("got to after the roast ", time.time())
time.sleep(600)
print("got to after sleep", time.time())

# Disconnect from the roaster.
r.roaster.disconnect()
