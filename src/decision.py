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
    param - {obj} - single_core - Processor instance
    return - {bool} - found_process - True / False if there is a process to work on
    return - {int} - active_index - index of the Process to work with in PROCESS_LIST; can be None
    return - {bool} - finish - True / False to know if we have to check for context switching
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
    param - {obj} - single_core - Processor instance
    return - {bool} - found_process - True / False if there is a process to work on
    return - {int} - active_index - index of the Process to work with in PROCESS_LIST; can be None
    return - {bool} - finish - True / False to know if we have to check for context switching
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
    param - {obj} - single_core - Processor instance
    return - {bool} - found_process - True / False if there is a process to work on
    return - {int} - active_index - index of the Process to work with in PROCESS_LIST; can be None
    return - {bool} - finish - True / False to know if we have to check for context switching
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
    param - {obj} - single_core - Processor instance
    return - {bool} - found_process - True / False if there is a process to work on
    return - {int} - active_index - index of the Process to work with in PROCESS_LIST; can be None
    return - {bool} - finish - True / False to know if we have to check for context switching
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

#----------------------------------------------------------------------------------------------------------
# priority based scheduling
#----------------------------------------------------------------------------------------------------------
def priority_based(single_core):
    """
    Implementation of a scheduler based on the niceness
    param - {obj} - single_core - Processor instance
    return - {bool} - found_process - True / False if there is a process to work on
    return - {int} - active_index - index of the Process to work with in PROCESS_LIST; can be None
    return - {bool} - finish - False to know if we have to check for context switching
    """

    # Needed Variables
    found_process = False
    active_index = None
    finish = True

    first_call = True

    # Find process with lowest niceness, scaling from -19 to 20
    for index in range(0, len(PROCESS_LIST)):

        # Process has to be arrived already.
        if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():
            
            # Differ from first call so we have values to compare
            if not first_call:
                investigated_niceness = PROCESS_LIST[index].get_niceness()
                
                # Check for lower niceness; if same wins the lower pid
                if investigated_niceness < smallest_niceness:
                    active_index = index
                    smallest_niceness = investigated_niceness
                    found_process = True
        
            else:
                smallest_niceness = PROCESS_LIST[index].get_niceness()
                active_index = index
                first_call = False
                found_process = True
    
    return found_process, active_index, finish


#----------------------------------------------------------------------------------------------------------
# Earliest Deadline First
#----------------------------------------------------------------------------------------------------------
def earliest_deadline_first(single_core):
    """
    Implementation of a scheduler based on the given deadlines; with context switching
    param - {obj} - single_core - Processor instance
    return - {bool} - found_process - True / False if there is a process to work on
    return - {int} - active_index - index of the Process to work with in PROCESS_LIST; can be None
    return - {bool} - finish - True to know if we have to check for context switching
    """

    # Needed Variables
    found_process = False
    active_index = None
    finish = False

    first_call = True

    # Search for the arrived process with the earliest deadline
    for index in range(0, len(PROCESS_LIST)):

        # Check if the process has arrived yet
        if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():

            # Differ from first case so we have values to compare
            if not first_call:
                
                # Save one call to the getter 
                investigated_deadline = PROCESS_LIST[index].get_deadline()

                # Check for the lowest deadline we can find
                if investigated_deadline < earliest_deadline:
                    earliest_deadline = investigated_deadline
                    active_index = index
                    found_process = True

            else:
                earliest_deadline = PROCESS_LIST[index].get_deadline()
                found_process = True
                active_index = index
                first_call = False
    
    return found_process, active_index, finish


#----------------------------------------------------------------------------------------------------------
# Highest Response Ratio Next
#----------------------------------------------------------------------------------------------------------
def highest_response_ratio_next(single_core):
    """
    Implementation of a scheduler based on the "highest response ratio"
    Means weighing burst time with already waited time
    param - {obj} - single_core - Processor instance
    return - {bool} - found_process - True / False if there is a process to work on
    return - {int} - active_index - index of the Process to work with in PROCESS_LIST; can be None
    return - {bool} - finish - True to know if we have to check for context switching
    """

    # Needed Variables
    found_process = False
    active_index = None
    finish = True

    first_call = True

    # Search for the arrived process with the earliest deadline
    for index in range(0, len(PROCESS_LIST)):

        # Check for all process that arrived already
        if PROCESS_LIST[index].get_arrival_time() <= single_core.get_clock_time():

            # Differ from first call so we have values to compare
            if not first_call:

                # Compute the compare value
                investigated_response_ratio = 1 + PROCESS_LIST[index].get_waiting_time() / PROCESS_LIST[index].get_burst_time()

                # Higher Respone Ratio Wins
                if investigated_response_ratio > highest_response_ratio:
                    highest_response_ratio = investigated_response_ratio
                    active_index = index
                    found_process = True

            else:
                highest_response_ratio = 1 + PROCESS_LIST[index].get_waiting_time() / PROCESS_LIST[index].get_burst_time()
                active_index = index
                found_process = True
                first_call = False
    

    return found_process, active_index, finish