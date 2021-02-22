# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\rr_popup_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_rr_popup(object):
    def setupUi(self, rr_popup):
        rr_popup.setObjectName("rr_popup")
        rr_popup.resize(305, 136)
        rr_popup.setMinimumSize(QtCore.QSize(305, 136))
        rr_popup.setMaximumSize(QtCore.QSize(305, 136))
        rr_popup.setModal(False)
        self.rr_popup_spin = QtWidgets.QSpinBox(rr_popup)
        self.rr_popup_spin.setGeometry(QtCore.QRect(240, 40, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rr_popup_spin.setFont(font)
        self.rr_popup_spin.setMinimum(1)
        self.rr_popup_spin.setObjectName("rr_popup_spin")
        self.rr_popup_start = QtWidgets.QPushButton(rr_popup)
        self.rr_popup_start.setGeometry(QtCore.QRect(210, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rr_popup_start.setFont(font)
        self.rr_popup_start.setObjectName("rr_popup_start")
        self.rr_popup_cancel = QtWidgets.QPushButton(rr_popup)
        self.rr_popup_cancel.setGeometry(QtCore.QRect(110, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rr_popup_cancel.setFont(font)
        self.rr_popup_cancel.setObjectName("rr_popup_cancel")
        self.rr_popup_label = QtWidgets.QLabel(rr_popup)
        self.rr_popup_label.setGeometry(QtCore.QRect(10, 20, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rr_popup_label.setFont(font)
        self.rr_popup_label.setObjectName("rr_popup_label")

        self.retranslateUi(rr_popup)
        QtCore.QMetaObject.connectSlotsByName(rr_popup)

    def retranslateUi(self, rr_popup):
        _translate = QtCore.QCoreApplication.translate
        rr_popup.setWindowTitle(_translate("rr_popup", "RR Time Quantum"))
        self.rr_popup_start.setText(_translate("rr_popup", "Start"))
        self.rr_popup_cancel.setText(_translate("rr_popup", "Cancel"))
        self.rr_popup_label.setText(_translate("rr_popup", "<html><head/><body><p align=\"justify\">Insert a Time Quantum</p><p align=\"justify\">for Round Robin:</p></body></html>"))
