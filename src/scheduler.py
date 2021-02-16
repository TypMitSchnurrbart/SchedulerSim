"""
Modul for a Counter thread showing the Current "Clock Time" of the "virtual" CPU
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.processor import Processor
from src.const import FCFS, SJF, PROCESS_LIST, HELPER
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

        else:
            self.window.display_error()
            return

    def first_come_first_serve(self, single_core):
        """
        First Come First Serve Scheduler Implementation
        param - {obj} - single_core - Object of Class Processor, inheriting a system clock
        return - {int} - default Zero
        """

        # Create User Output
        self.window.display_text("<br><br>")
        self.window.display_text("------------------------------------------------------------")
        self.window.display_text("Starting First Come - First Serve Algorithm!")
        self.window.display_text(f"Found {Process.number_of_processes} Processes to schedule...")
        self.window.display_text("------------------------------------------------------------")
        self.window.display_text("<br><br>")

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
                # Translate process with newest arrival time
                active_process = PROCESS_LIST[smallest]

                # "Process" the smallest process
                self.window.display_text("<br>")
                self.window.display_text(f"Starting to process {active_process.get_pid()} with Burst Time: {active_process.get_burst_time()}!=======================")

                init_burst_time = active_process.get_burst_time()
                active_pid = active_process.get_pid()
                for iterator in range(0, init_burst_time + 1):

                    # Differ for first case
                    if iterator == 0:
                        self.window.display_text(f"System-Clock: {single_core.get_clock_time()}")
                    else:
                        self.window.display_text(f"System-Clock: {single_core.get_clock_time_step()}")

                    self.window.display_text(f"\tActive PID: {active_pid} \tRemaining Burst Time: {init_burst_time - iterator}")

                    # Sleep a Second for Sim Reasons
                    single_core.work()

                self.window.display_text(f"Finished Processing: {active_pid}! =================================")
                self.window.display_text("<br><br>")

                # Store time the process had to wait in its live and remeber that you the core finished a process
                single_core.set_waited_time(active_process.get_waiting_time())
                single_core.set_computed_amount()

                # Finished processing; deleting Process
                del PROCESS_LIST[smallest]

                # Now increment waiting time of all remaining processes by the just done burst time
                for i in range(0, len(PROCESS_LIST)):
                    if PROCESS_LIST[i].get_arrival_time() <= single_core.get_clock_time():
                        PROCESS_LIST[i].set_waiting_time(init_burst_time)


        # Finish Message
        self.window.display_text(f"Finished all Processes with First Come - First Serve!")
        self.window.display_text(f"Average Waiting Time: {single_core.get_average_waiting()}")

        return

    def smallest_job_first(self, single_core):
        """
        Choose by smallest burst_time; no context_switching
        param - {obj} - single_core - Object of Processor for the System Clock
        return - {int} - default Zero
        """

        pass
