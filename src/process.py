"""
Class of Processes containing the Processes parameters
"""

# Module imports
from src.const import START_ID, ID_OFFSET

class Process():
    """
    Class to implement a Process with all its variables
    """

    number_of_processes = 0
    process_id_generator = START_ID

    def __init__(self, arrival_time, burst_time, niceness = 0, deadline = 0, waiting_time = 0):
        """
        Constructor of a Process
        param - {int} - arrival_time - Clock when the process enters waiting queue
        param - {int} - burst_time - Clock Ticks the process needs to be processed
        param - {int} - waiting_time - Time the process needed to wait; init as Zero
        param - {int} - niceness - Prority value, dont need for every scheduler algorithm
        param - {int} - deadline - Clock value when the process needs to be finished; dont need for every scheduler algorithm
        """
        Process.number_of_processes += 1
        Process.process_id_generator += ID_OFFSET

        self.pid = Process.process_id_generator
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = waiting_time
        self.niceness = niceness
        self.deadline = deadline

    def get_arrival_time(self):
        """
        Getter for the arrival_time set at creation
        return - {int} - arrival_time of calling object
        """
        return self.arrival_time

    def get_burst_time(self):
        """
        Getter for current burst_time
        return - {int} - burst_time of calling object
        """
        return self.burst_time

    def set_burst_time(self, remaining_time):
        """
        Possibility to change the burst_time until it hits zero 
        param - {int} - remaining_time - new burst_time value subtrated by the time the process got already processed
        return - {int} - burst_time
        """
        self.burst_time = remaining_time
        return self.burst_time

    def get_waiting_time(self):
        """
        Setter / Getter for Waiting Time
        return - {int} - waiting_time of calling object
        """
        return self.waiting_time

    def set_waiting_time(self, waited_time):
        """
        Setter for the waiting_time
        param - {int} - waited_time - Value of time already waited, doesnt have to be final  
        """
        self.waiting_time += waited_time
        return 

    def get_pid(self):
        """
        Setter for PID
        return - {int} - process id of calling object
        """
        return self.pid

    def get_niceness(self):
        """
        Getter for niceness
        return - {int} - Priority level of calling object
        """
        return self.niceness

    def get_deadline(self):
        """
        Getter for the deadline
        return - {int} - deadline of calling object
        """
        return self.deadline

    #TODO Finished Process Method decrementing pid counter __del__?