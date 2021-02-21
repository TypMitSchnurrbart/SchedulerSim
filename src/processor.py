"""
Creating a Class represeting the function of the processor
"""

import time

from src.const import SLEEPER, PROCESS_LIST, HELPER

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
        return round(self.waited_time / self.computed_amount, 2)


    def work_process(self, scheduler_runnable, index, scheduler, single_core, finish = True):
        """
        Function to finish a process completly and behave accordingly
        param - {obj} - scheduler_runnable - QRunnable of the Scheduler in the window
        param - {int} - index - of process to work with in the Process list
        param - {int} - scheduler - const to remember which scheduler is running
        param - {obj} - single_core - instance of processor
        param - {bool} - finsih - to differ if a context_switch is possible
        """

        # Translate process with newest arrival time
        active_process = PROCESS_LIST[index]

        # "Process" the smallest process
        scheduler_runnable.window.display_text("<br>")
        scheduler_runnable.window.display_text(f"Starting to process {active_process.get_pid()} with Burst Time: {active_process.get_burst_time()}!=======================")

        # Declaring some needed variables
        init_burst_time = active_process.get_burst_time()
        active_pid = active_process.get_pid()
        context_switch = False

        for iterator in range(0, init_burst_time):

            if not finish:
                context_switch = HELPER[0].check_context_switch(scheduler, single_core, active_process)

            scheduler_runnable.window.display_text(f"System-Clock: {self.get_clock_time_step()}")

            active_process.set_burst_time(init_burst_time - (iterator + 1))
            scheduler_runnable.window.display_text(f"\tActive PID: {active_pid} \tRemaining Burst Time: {active_process.get_burst_time()}")
        
            # Sleep a Second for Sim Reasons, utterly important
            self.work()

            # If the context switch hits break at this point
            if context_switch:
                # Now increment waiting time of all remaining processes by the just done burst time
                for i in range(0, len(PROCESS_LIST)):
                    if PROCESS_LIST[i].get_arrival_time() <= self.get_clock_time():
                        PROCESS_LIST[i].set_waiting_time(iterator + 1)

                scheduler_runnable.window.display_text("<br><br>")
                scheduler_runnable.window.display_text("Better Process found! Performing a Context Switch...")
                scheduler_runnable.window.display_text("<br><br>")
                return

        scheduler_runnable.window.display_text(f"Finished Processing: {active_pid}! =================================")
        scheduler_runnable.window.display_text("<br><br>")

        # Store time the process had to wait in its live and remeber that the core finished a process
        self.set_waited_time(active_process.get_waiting_time())
        self.set_computed_amount()

        # Finished processing; deleting Process
        del PROCESS_LIST[index]

        # Now increment waiting time of all remaining processes by the just done burst time
        for i in range(0, len(PROCESS_LIST)):
            if PROCESS_LIST[i].get_arrival_time() <= self.get_clock_time():
                PROCESS_LIST[i].set_waiting_time(init_burst_time)

        return

    @staticmethod
    def work():
        time.sleep(SLEEPER)
        return