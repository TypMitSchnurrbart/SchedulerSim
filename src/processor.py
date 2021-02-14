"""
Creating a Class represeting the function of the processor
"""

class Processor():
    """
    Class "simulating" a Process but only the clock timing
    This is a class to support possibility for multi-core sims
    """
    def __init__(self, clock_time = 0):
        self.clock_time = clock_time

    def get_clock_time(self):
        return self.clock_time

    def get_clock_time_step(self):
        self.clock_time += 1
        return self.clock_time
    
    def reset_clock_time(self):
        self.clock_time = 0
        return self.clock_time