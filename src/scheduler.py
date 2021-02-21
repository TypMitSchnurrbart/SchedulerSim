"""
Modul for a Counter thread showing the Current "Clock Time" of the "virtual" CPU
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.processor import Processor
from src.const import FCFS, SJF, PROCESS_LIST, HELPER, SRTF
from src.process import Process

class Scheduler(QRunnable):
    """
    Class to create a thread in our GUI Process in order to have a Widget updating
    itself without the window freezing
    """

    def __init__(self, window_to_work, chosen_scheduler):
        """
        Constructor of Counter_Worker
        param   {obj}   window_to_work - Is the Object aof the class Window in which this widget shall be working
        """
        super(Scheduler, self).__init__()
        self.window = window_to_work
        self.schedule_mode = chosen_scheduler


    def run(self):

        single_core = Processor()


        if self.schedule_mode == FCFS:
            self.first_come_first_serve(single_core)
            return

        elif self.schedule_mode == SJF:
            self.smallest_job_first(single_core)
            return

        elif self.schedule_mode == SRTF:
            self.shortest_remaining_time_first(single_core)

        else:
            self.window.display_error()
            return

#----------------------------------------------------------------------------------------------------------
# First Come - First Serve
#----------------------------------------------------------------------------------------------------------
    def first_come_first_serve(self, single_core):
        """
        First Come First Serve Scheduler Implementation
        param - {obj} - single_core - Object of Class Processor, inheriting a system clock
        return - {int} - default Zero
        """

        # Create User Output
        HELPER[0].schedule_start_message(self, FCFS)

        # scheduling - loop
        while len(PROCESS_LIST) > 0:

            process_found = False
            first_call = True

            # Search smallest arrival time
            for index in range(0, len(PROCESS_LIST)):
                
                # Initial Case but needs to be arrived yet
                if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():
                
                    # Store Index that fulfills requirement of being lesser than compared arrival_time and greater or equal to system clock
                    if not first_call:
                        if PROCESS_LIST[smallest].get_arrival_time() > PROCESS_LIST[index].get_arrival_time():
                            smallest = index
                            process_found = True

                    else:
                        smallest = index
                        process_found = True
                        first_call = False
        
            # CPU got to wait, no Process arrived yet
            if not process_found:
                self.window.display_text(f"No Process in Queue. Running Empty...")
                self.window.display_text(f"System-Clock: {single_core.get_clock_time_step()}")
                single_core.work()
                    
            else:

                # Finish the process because this algo has no context switching
                single_core.work_process(self, smallest, FCFS, single_core)

        # Finish Message
        self.window.display_text(f"Finished all Processes with First Come - First Serve!")
        self.window.display_text(f"Average Waiting Time: {single_core.get_average_waiting()}")

        return

#----------------------------------------------------------------------------------------------------------
# Smallest Job First
#----------------------------------------------------------------------------------------------------------

    def smallest_job_first(self, single_core):
        """
        Choose by smallest burst_time; no context_switching
        param - {obj} - single_core - Object of Processor for the System Clock
        return - {int} - default Zero
        """

        # Create User Output
        HELPER[0].schedule_start_message(self, SJF)

        # Scheduling - loop
        while len(PROCESS_LIST) > 0:

                # Determine Process with shortest burst time, and if there are even processes waiting

                found_process = False
                first_call = True

                # Check every Process in line
                for index in range(0, len(PROCESS_LIST)):

                    # Check if the process is even arrived yet
                    if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():

                        # Differ from first call to even have something to compare
                        if not first_call:

                            # Check burst time, if smaller this process becomes the new to beat
                            if PROCESS_LIST[index].get_burst_time() < fastest_burst_time:
                                    fastest_index = index
                                    fastest_burst_time = PROCESS_LIST[index].get_burst_time()

                        else:
                            fastest_index = index
                            fastest_burst_time = PROCESS_LIST[index].get_burst_time()
                            first_call = False
                            found_process = True


                if not found_process:
                    self.window.display_text(f"No Process in Queue. Running Empty...")
                    self.window.display_text(f"System-Clock: {single_core.get_clock_time_step()}")
                    single_core.work()
                    
                else:
                    # Finish the process because there is no context switching in SJF
                    single_core.work_process(self, fastest_index, SJF, single_core)

        # Finish Message
        self.window.display_text(f"Finished all Processes with Smallest Job First!")
        self.window.display_text(f"Average Waiting Time: {single_core.get_average_waiting()}")

        return

#----------------------------------------------------------------------------------------------------------
# Shortest Remaining Time First
#----------------------------------------------------------------------------------------------------------
    def shortest_remaining_time_first(self, single_core):
        """
        Implemtation of the SRTF Algorithm, now we start context switching!
        param - {obj} - single_core - instance of processor
        """

        while len(PROCESS_LIST) > 0:
            
            
            # Determine Process with shortest burst time, and if there are even processes waiting

            found_process = False
            first_call = True

            # Check every Process in line
            for index in range(0, len(PROCESS_LIST)):

                # Check if the process is even arrived yet
                if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():

                    # Differ from first call to even have something to compare
                    if not first_call:

                        # Check burst time, if smaller this process becomes the new to beat
                        if PROCESS_LIST[index].get_burst_time() < fastest_burst_time:
                                fastest_index = index
                                fastest_burst_time = PROCESS_LIST[index].get_burst_time()

                    else:
                        fastest_index = index
                        fastest_burst_time = PROCESS_LIST[index].get_burst_time()
                        first_call = False
                        found_process = True


            if not found_process:
                self.window.display_text(f"No Process in Queue. Running Empty...")
                self.window.display_text(f"System-Clock: {single_core.get_clock_time_step()}")
                single_core.work()
                    
            else:
                # Work the process until a new one arrives
                single_core.work_process(self, fastest_index, SRTF, single_core, False)


        # Finish Message
        self.window.display_text(f"Finished all Processes with Shortest Remaining Time First")
        self.window.display_text(f"Average Waiting Time: {single_core.get_average_waiting()}")

        return

                        
