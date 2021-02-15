"""
Main for a small scheduler sim with gui; this its mainly for testing at the moment
Author:     Alexander Müller
Version:    0.1.1
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
from src.const import PROCESS_LIST

# Load different Classes--------------------------------------------------
from src.process import Process
from src.scheduler import Scheduler
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


    def add_process_to_queue(self):
        """
        Function to create a Process Object from the inserted data in the Window
        """

        # Get Data From Window
        arrival_time = self.spin_arrival_time.value()
        burst_time = self.spin_burst_time.value()
        niceness = self.spin_niceness.value()
        deadline = self.spin_deadline.value()

        # Create Process based on Data
        PROCESS_LIST.append(Process(arrival_time, burst_time, niceness, deadline))

        # Prep output for text box
        pid = PROCESS_LIST[-1].get_pid()
        arrival_time = PROCESS_LIST[-1].get_arrival_time()
        burst_time = PROCESS_LIST[-1].get_burst_time()
        niceness = PROCESS_LIST[-1].get_niceness()
        deadline = PROCESS_LIST[-1].get_deadline()
        current_time = datetime.now().strftime("[%H:%M:%S]\t")

        # Give user feedback to successful creatin an Process
        self.terminal_output.append(f"{current_time}Process added.\tPID: {pid}\tArrival: {arrival_time}\tBurst: {burst_time}\tPriority: {niceness}\tDeadline: {deadline}")

        # Reset the spinboxes values
        self.spin_arrival_time.setValue(0)
        self.spin_burst_time.setValue(1)
        self.spin_niceness.setValue(0)
        self.spin_deadline.setValue(1)

        return


    def determine_scheduler(self):

        # Determine which radio button is pressed

        return

    
    def start_scheduling(self, chosen_scheduler):
        
        # Start Scheduliung progress; is a class even necessary? dont know
        self.thread_handler = QThreadPool()
        self.start_app()

        scheduler = Scheduler(self)
        self.thread_handler.start(scheduler)

        return

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
