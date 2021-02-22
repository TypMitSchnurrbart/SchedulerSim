"""
Module inheriting the class for the rr time quatum popup
"""
# Used libraries
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Module Class Imports
from rr_popup_dialog import Ui_rr_popup

# Constant Imports
from src.const import RR_QUANTUM


class RRPopup(QDialog, Ui_rr_popup):

    # Class Constructor with parent Constructor as super
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.rr_popup_start.clicked.connect(self.start)
        self.rr_popup_cancel.clicked.connect(self.cancel)


    def start(self):
        """
        Read the inserted time in the dialog
        return - {int} - inserted_value
        """

        RR_QUANTUM[0] = (self.rr_popup_spin.value())
        self.close()

    @staticmethod
    def cancel(self):
        """
        Inserting canceled return to main window as it is
        """
        self.close()

