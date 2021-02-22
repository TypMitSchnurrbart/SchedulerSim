"""
Modul for a Counter thread showing the Current "Clock Time" of the "virtual" CPU
"""

# Library Imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Module Imports
from src.processor import Processor
from src.const import FCFS, SJF, PROCESS_LIST, HELPER, SRTF, RR
from src.process import Process
from src.decision import first_come_first_serve, smallest_job_first 
from src.decision import shortest_remaining_time_first, round_robin


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

        # Necessarities
        single_core = Processor()

        # Create User Output
        HELPER[0].schedule_start_message(self, self.schedule_mode)

        # Scheduling - loop
        while len(PROCESS_LIST) > 0:

            # Determine which Scheduler an get the decision accordingly
            if self.schedule_mode == FCFS:
                process_found, active_index, finish = first_come_first_serve(single_core)

            elif self.schedule_mode == SJF:
                process_found, active_index, finish = smallest_job_first(single_core)

            elif self.schedule_mode == SRTF:
                process_found, active_index, finish = shortest_remaining_time_first(single_core)

            elif self.schedule_mode == RR:
                process_found, active_index, finish = round_robin(single_core)

            else:
                self.window.display_text("Error Occured! Please try again!")
                return


            # CPU got to wait, no Process arrived yet
            if not process_found:
                self.window.display_text(f"No Process in Queue. Running Empty...")
                self.window.display_text(f"System-Clock: {single_core.get_clock_time_step()}")
                single_core.work()
                    
            else:

                # Put the CPU to work according to the decisions made
                single_core.work_process(self, active_index, self.schedule_mode, single_core, finish)


        # Finish Message
        self.window.display_text(f"Finished all Processes!")
        self.window.display_text(f"Average Waiting Time: {single_core.get_average_waiting()}")

        return

                           
