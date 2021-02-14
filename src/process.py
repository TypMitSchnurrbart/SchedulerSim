"""
Class of Processes containing the Processes parameters
"""

from src.const import START_ID, ID_OFFSET

class Process():

    number_of_processes = START_ID

    def __init__(self, arrvial_time, burst_time, waiting_time = 0):

        Process.number_of_processes += ID_OFFSET

        self.pid = Process.number_of_processes
        self.arrvial_time = arrvial_time
        self.burst_time = burst_time
        self.waiting_time = waiting_time

    # Setter / Getter for Arrival Time 
    def get_arrival_time(self):
        return self.arrvial_time

    # Setter / Getter for Burst Time 
    def get_burst_time(self):
        return self.burst_time

    def set_burst_time(self, remaining_time):
        self.burst_time = remaining_time
        return 0

    # Setter / Getter for Waiting Time
    def get_waiting_time(self):
        return self.waiting_time

    def set_waiting_time(self, waited_time):
        self.waiting_time = waited_time
        return 0

    # Setter for PID
    def get_pid(self):
        return self.pid

    #TODO Finished Process Method decrementing pid counter