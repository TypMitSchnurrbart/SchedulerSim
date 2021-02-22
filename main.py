"""
Main for a small scheduler sim with gui; this its mainly for testing at the moment
Author:     Alexander Müller
Version:    0.7.1
Date:       14.02.2021
"""

# Load system libraries---------------------------------------------------
import sys
import time
from datetime import datetime

# Load PyQt5 Library Classes----------------------------------------------
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Load Constants----------------------------------------------------------
from src.const import PROCESS_LIST, FCFS, SJF, HELPER, TEXT_DELAY, SRTF
from src.const import RR, RR_QUANTUM, PBS, EDF, HELP_URL, HRRN

# Load different Classes--------------------------------------------------
from src.process import Process
from src.scheduler import Scheduler
from src.helper import Helper
from src.rr_popup import RRPopup
from scheduler_sim_gui import Ui_main_window


#-------------------------------------------------------------------------
#   Main Window Class
#   importing from QtDesginer Created UI translated to python
#-------------------------------------------------------------------------
class Window(QMainWindow, Ui_main_window):
    """
    Class of our GUI
    parent  QMainWindow
    parent  Ui_main_window
    """

    # Class Constructor with parent Constructor as super
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Click Event for Add Button
        self.pushButton_add.clicked.connect(self.add_process_to_queue)
        self.pushButton_start.clicked.connect(self.determine_scheduler)
        self.pushButton_cancel.clicked.connect(self.cancel_all)
        self.pushButton_help.clicked.connect(self.open_help)


    def add_process_to_queue(self):
        """
        Function to create a Process Object from the inserted data in the Window
        """

        # Get Data From Window
        arrival_time = self.spin_arrival_time.value()
        burst_time = self.spin_burst_time.value()
        niceness = self.spin_niceness.value()
        deadline = self.spin_deadline.value()

        # Check if the given deadline is even possible
        if arrival_time + burst_time > deadline:
            self.display_text("Couldnt add Process because its not doable within its deadline!")
            return

        # Create Process based on Data
        PROCESS_LIST.append(Process(arrival_time, burst_time, niceness, deadline))

        # Prep output for text box
        pid = PROCESS_LIST[-1].get_pid()
        arrival_time = PROCESS_LIST[-1].get_arrival_time()
        burst_time = PROCESS_LIST[-1].get_burst_time()
        niceness = PROCESS_LIST[-1].get_niceness()
        deadline = PROCESS_LIST[-1].get_deadline()

        # Give user feedback to successful creatin an Process
        self.terminal_output.append(f"{HELPER[0].get_current_time()}Process added.\tPID: {pid}\tArrival: {arrival_time}\tBurst: {burst_time}\tPriority: {niceness}\tDeadline: {deadline}")
        self.terminal_output.ensureCursorVisible()

        # Reset the spinboxes values
        self.reset_spin_boxes()

        return


    def determine_scheduler(self):
        """
        Decide which scheduler has been choosen
        """

        # First check if there is even a process
        if len(PROCESS_LIST) == 0:
            self.display_text("Please add at least a Process first!")
            return

        if self.radio_fcfs.isChecked():
            self.start_scheduling(FCFS)

        elif self.radio_sjf.isChecked():
            self.start_scheduling(SJF)

        elif self.radio_srtf.isChecked():
            self.start_scheduling(SRTF)

        elif self.radio_rrobin.isChecked():

            # Creatin a Dialog for the Time Quantum
            dialog = RRPopup()
            dialog.exec()

            if RR_QUANTUM[0] != 0:
                self.start_scheduling(RR)

        elif self.radio_pbs.isChecked():
            self.start_scheduling(PBS)
        
        elif self.radio_edf.isChecked():
            self.start_scheduling(EDF)

        elif self.radio_hrrn.isChecked():
            self.start_scheduling(HRRN)
            
        else:
            self.display_text("Choose a Scheduler Algorithm!")

    
    def start_scheduling(self, chosen_scheduler):
        """
        Start the scheduling thread so the window doesnt freeze
        param - {int} - chosen_scheduler- short variable for the scheduler, look in consts
        """
        # Start Scheduliung progress; is a class even necessary? dont know
        self.thread_handler = QThreadPool()

        scheduler = Scheduler(self, chosen_scheduler)
        self.thread_handler.start(scheduler)


    def cancel_all(self):
        """
        Function to clear all add Processes 
        """
        # Delete all added Processes from the back to have it nice and smooth
        max_range = len(PROCESS_LIST)
        for i in range(0, max_range):
            index = (max_range - 1) - i
            del PROCESS_LIST[index]

        # Reset all SpinBoxes
        self.reset_spin_boxes()
        self.display_text("Cleared all processes in Queue!")


    def reset_spin_boxes(self):
        """
        Reset all Spinboxes to their default values
        """
        # Reset the spinboxes values
        self.spin_arrival_time.setValue(0)
        self.spin_burst_time.setValue(1)
        self.spin_niceness.setValue(0)
        self.spin_deadline.setValue(1)


    def display_text(self, output):
        """
        Display the Text with the current time
        param - {string} - output - Text to display
        return - {int} - default Zero
        """
        # Give user feedback
        time.sleep(TEXT_DELAY) 
        self.terminal_output.append(f"{HELPER[0].get_current_time()}{output}")
        self.terminal_output.ensureCursorVisible()
        

    def display_end_line(self):
        """
        Possibility to end the line without the timestamp
        """
        #Create and of Line
        time.sleep(TEXT_DELAY) 
        self.terminal_output.append("<br>")
        self.terminal_output.ensureCursorVisible()


    def open_help(self):
        """
        Method to open the help site
        """
        # Load URL from consts and open it
        url = QUrl(HELP_URL)
        QDesktopServices.openUrl(url)
        

if __name__ == "__main__":

    # Create our Helper object
    HELPER.append(Helper())

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
