"""
Modul for a Counter thread showing the Current "Clock Time" of the "virtual" CPU
"""

import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.processor import Processor

class Scheduler(QRunnable):
    """
    Class to create a thread in our GUI Process in order to have a Widget updating
    itself without the window freezing
    """

    def __init__(self, window_to_work):
        """
        Constructor of Counter_Worker
        param   {obj}   window_to_work - Is the Object aof the class Window in which this widget shall be working
        """
        super(Scheduler, self).__init__()
        self.window = window_to_work


    def run(self):
        single_core = Processor()

        while single_core.get_clock_time() <= 10:
            #TODO interrupt button as statement
            clock_time = single_core.get_clock_time_step()
            time.sleep(1)
            self.window.system_clock_display.display(clock_time)
            self.window.system_clock_display.repaint()
        
        clock_time = single_core.reset_clock_time()
        self.window.system_clock_display.display(clock_time)
