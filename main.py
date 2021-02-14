"""
Main for a small scheduler sim with gui; this its mainly for testing at the moment
"""
import sys
import time
from datetime import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from scheduler_sim_gui import Ui_main_window
from src.processor import Processor
from src.const import PROCESS_LIST
from src.process import Process

class Window(QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Add Button
        self.pushButton_add.clicked.connect(self.add_process_to_queue)


    def add_process_to_queue(self):

        arrival_time = self.spin_arraival_time.value()
        burst_time = self.spin_burst_time.value()

        PROCESS_LIST.append(Process(arrival_time, burst_time))

        pid = PROCESS_LIST[-1].get_pid()
        arrival_time = PROCESS_LIST[-1].get_arrival_time()
        burst_time = PROCESS_LIST[-1].get_burst_time()

        current_time = datetime.now().strftime("[%H:%M:%S]\t")
        self.terminal_output.append(f"{current_time}Process added.\tPID: {pid}\tArrival: {arrival_time}\tBurst: {burst_time}")

    def start_btn_state(self):
        if not self.pushButton.isChecked():
            self.threadpool = QThreadPool()
            self.start_app()

    def start_app(self):

        test_worker = Counter_Worker(self)
        self.threadpool.start(test_worker)


class Counter_Worker(QRunnable):

    def __init__(self, window_to_work):
        super(Counter_Worker, self).__init__()
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

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
