"""
Module holing all the decision rules for the different scheduler
"""

# Module Imports
from src.const import PROCESS_LIST, LAST_RR_INDEX

#----------------------------------------------------------------------------------------------------------
# First Come - First Serve
#----------------------------------------------------------------------------------------------------------
def first_come_first_serve(single_core):
    """
    First Come First Serve Scheduler Implementation of the decision
    param - {obj} - single_core - Object of Class Processor, inheriting a system clock
    return - {int} - default Zero
    """

    # Needed variables
    active_index = None
    process_found = False
    first_call = True
    finish = True

    # Search smallest arrival time
    for index in range(0, len(PROCESS_LIST)):
        
        # Initial Case but needs to be arrived yet
        if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():
        
            # Store Index that fulfills requirement of being lesser than compared arrival_time and greater or equal to system clock
            if not first_call:
                if PROCESS_LIST[active_index].get_arrival_time() > PROCESS_LIST[index].get_arrival_time():
                    active_index = index
                    process_found = True

            else:
                active_index = index
                process_found = True
                first_call = False

    return process_found, active_index, finish


#----------------------------------------------------------------------------------------------------------
# Smallest Job First
#----------------------------------------------------------------------------------------------------------
def smallest_job_first(single_core):
    """
    Choose by smallest burst_time; no context_switching
    param - {obj} - single_core - Object of Processor for the System Clock
    return - {int} - default Zero
    """

    # Needeed Variables
    active_index = None
    process_found = False
    first_call = True
    finish = True

    # Check every Process in line
    for index in range(0, len(PROCESS_LIST)):

        # Check if the process is even arrived yet
        if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():

            # Differ from first call to even have something to compare
            if not first_call:

                # Check burst time, if smaller this process becomes the new to beat
                if PROCESS_LIST[index].get_burst_time() < fastest_burst_time:
                        active_index = index
                        fastest_burst_time = PROCESS_LIST[index].get_burst_time()

            else:
                active_index = index
                fastest_burst_time = PROCESS_LIST[index].get_burst_time()
                first_call = False
                process_found = True

    return process_found, active_index, finish


#----------------------------------------------------------------------------------------------------------
# Shortest Remaining Time First
#----------------------------------------------------------------------------------------------------------
def shortest_remaining_time_first(single_core):
    """
    Implemtation of the SRTF Algorithm, now we start context switching!
    param - {obj} - single_core - instance of processor
    """ 
        
    # Needed variables
    active_index = None
    found_process = False
    first_call = True
    finish = False

    # Check every Process in line
    for index in range(0, len(PROCESS_LIST)):

        # Check if the process is even arrived yet
        if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():

            # Differ from first call to even have something to compare
            if not first_call:

                # Check burst time, if smaller this process becomes the new to beat
                if PROCESS_LIST[index].get_burst_time() < fastest_burst_time:
                        active_index = index
                        fastest_burst_time = PROCESS_LIST[index].get_burst_time()

            else:
                active_index = index
                fastest_burst_time = PROCESS_LIST[index].get_burst_time()
                first_call = False
                found_process = True

    return found_process, active_index, finish


#----------------------------------------------------------------------------------------------------------
# Round Robin
#----------------------------------------------------------------------------------------------------------
def round_robin(single_core):
    """
    Implemtation of the RR Scheduler
    param - {obj} - single_core - instance of processor
    """
            
    # Needed variables
    active_index = None
    lowest_possible_index = None
    found_process = False
    finish = False
    first_call = True

    # Search for process to choose
    for index in range(0, len(PROCESS_LIST)):
        
        # Process has to be arrived
        if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():

            # Store the lowest possible index to jump to the beginning of the array if we are at the end
            if first_call:
                first_call = False
                lowest_possible_index = index

            # For the case that only one process is left that is already arrived
            if len(PROCESS_LIST) == 1:
                found_process = True
                active_index = index

            # Choose the next bigger index in from the process array to actually get the robin round
            elif index > LAST_RR_INDEX[0]:
                found_process = True
                active_index = index
                break

    if lowest_possible_index != None and not found_process:
        active_index = lowest_possible_index
        found_process = True

    return found_process, active_index, finish