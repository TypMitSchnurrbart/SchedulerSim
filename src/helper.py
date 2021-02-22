"""
Helper class to call from everywhere
"""

# System Imports
from datetime import datetime

# Modul imports
from src.process import Process
from src.const import SJF, FCFS, SRTF, PROCESS_LIST, RR, RR_QUANTUM, LAST_RR_INDEX


class Helper():
    """
    Offering different needed functions. Class just to stay object orientated
    And makes it nicer to call it
    """

    def __init__(self):
        print("Created Helper...")


    @staticmethod
    def get_current_time():
        """
        Get current system time formated the way needed
        """
        return datetime.now().strftime("[%H:%M:%S]\t")

    @staticmethod
    def schedule_start_message(scheduler_thread, scheduler):
        """
        param - {obj} - scheduler_thread - QRunnable which is scheduling
        param - {int} - scheduler
        """

        # Create User Output
        scheduler_thread.window.display_text("<br><br>")
        scheduler_thread.window.display_text("------------------------------------------------------------")

        if scheduler == FCFS:
            scheduler_thread.window.display_text("Starting First Come - First Serve Algorithm!")
        elif scheduler == SJF:
            scheduler_thread.window.display_text("Shortest Job First Algorithm!")
        elif scheduler == SRTF:
            scheduler_thread.window.display_text("Shortest Remaining Time First!")
        elif scheduler == RR:
            scheduler_thread.window.display_text("Round Robin!")

        scheduler_thread.window.display_text(f"Found {Process.number_of_processes} Processes to schedule...")
        scheduler_thread.window.display_text("------------------------------------------------------------")
        scheduler_thread.window.display_text("<br><br>")

        return

    @staticmethod
    def check_context_switch(scheduler, single_core, active_process, iterator):

        # Check Context Switch Condition for SRFT
        if scheduler == SRTF:

            # Context Switch has to be made if process is arriving that is shorter than current remaining burst time
            for i in range(0, len(PROCESS_LIST)):
                if PROCESS_LIST[i].get_arrival_time() == single_core.get_clock_time() + 1:
                    if PROCESS_LIST[i].get_burst_time() < active_process.get_burst_time():
                        return True

        # Check Context Switch for RR
        if scheduler == RR:
            if (iterator + 1) == RR_QUANTUM[0]:
                
                for index in range(0, len(PROCESS_LIST)):
                    if PROCESS_LIST[index].get_pid() == active_process.get_pid():
                        LAST_RR_INDEX[0] = index
                        return True
            
            