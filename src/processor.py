"""
Creating a Class represeting the function of the processor
"""

import time

from src.const import SLEEPER

class Processor():
    """
    Class "simulating" a Process but only the clock timing
    This is a class to support possibility for multi-core sims
    """

    def __init__(self, clock_time = 0, waited_time = 0, computed_amount = 0):
        self.clock_time = clock_time
        self.waited_time = waited_time
        self.computed_amount = computed_amount

    def get_clock_time(self):
        return self.clock_time

    def get_clock_time_step(self):
        self.clock_time += 1
        return self.clock_time
    
    def reset_clock_time(self):
        self.clock_time = 0
        return self.clock_time

    def get_waited_time(self):
        return self.waited_time

    def set_waited_time(self, waited_time):
        self.waited_time += waited_time

    def set_computed_amount(self):
        self.computed_amount += 1
        return

    def get_average_waiting(self):
        return self.waited_time / self.computed_amount

    @staticmethod
    def work():
        time.sleep(SLEEPER)
        return