# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DayChart.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_DayChart(object):
    def setupUi(self, DayChart):
        DayChart.setObjectName("DayChart")
        DayChart.resize(1143, 768)
        self.centralwidget = QtWidgets.QWidget(DayChart)
        self.centralwidget.setObjectName("centralwidget")
        self.sym_lbl = QtWidgets.QLabel(self.centralwidget)
        self.sym_lbl.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.sym_lbl.setObjectName("sym_lbl")
        self.date_lbl = QtWidgets.QLabel(self.centralwidget)
        self.date_lbl.setGeometry(QtCore.QRect(150, 20, 91, 16))
        self.date_lbl.setObjectName("date_lbl")
        self.sym_in = QtWidgets.QLineEdit(self.centralwidget)
        self.sym_in.setGeometry(QtCore.QRect(10, 50, 113, 22))
        self.sym_in.setObjectName("sym_in")
        self.date_in = QtWidgets.QDateEdit(self.centralwidget)
        self.date_in.setGeometry(QtCore.QRect(140, 50, 110, 22))
        self.date_in.setObjectName("date_in")
        self.get_btn = QtWidgets.QPushButton(self.centralwidget)
        self.get_btn.setGeometry(QtCore.QRect(270, 50, 93, 21))
        self.get_btn.setObjectName("get_btn")
        self.MplGraph = MplGraph(self.centralwidget)
        self.MplGraph.setGeometry(QtCore.QRect(70, 160, 981, 491))
        self.MplGraph.setObjectName("MplGraph")
        DayChart.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DayChart)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1143, 26))
        self.menubar.setObjectName("menubar")
        self.menuasdfsd = QtWidgets.QMenu(self.menubar)
        self.menuasdfsd.setObjectName("menuasdfsd")
        DayChart.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DayChart)
        self.statusbar.setObjectName("statusbar")
        DayChart.setStatusBar(self.statusbar)
        self.actionSave_data = QtWidgets.QAction(DayChart)
        self.actionSave_data.setObjectName("actionSave_data")
        self.menuasdfsd.addSeparator()
        self.menuasdfsd.addAction(self.actionSave_data)
        self.menubar.addAction(self.menuasdfsd.menuAction())

        self.retranslateUi(DayChart)
        QtCore.QMetaObject.connectSlotsByName(DayChart)

    def retranslateUi(self, DayChart):
        _translate = QtCore.QCoreApplication.translate
        DayChart.setWindowTitle(_translate("DayChart", "Daily Chart"))
        self.sym_lbl.setText(_translate("DayChart", "Enter Symbol"))
        self.date_lbl.setText(_translate("DayChart", "Enter Date"))
        self.get_btn.setText(_translate("DayChart", "Get Data"))
        self.menuasdfsd.setTitle(_translate("DayChart", "File"))
        self.actionSave_data.setText(_translate("DayChart", "Save data"))

from Exploration.mplgraph import MplGraph
