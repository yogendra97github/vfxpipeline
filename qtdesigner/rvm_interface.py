# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rvm_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(462, 317)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.source_v = QLabel(self.centralwidget)
        self.source_v.setObjectName(u"source_v")
        self.source_v.setGeometry(QRect(20, 20, 91, 31))
        self.dest_v = QLabel(self.centralwidget)
        self.dest_v.setObjectName(u"dest_v")
        self.dest_v.setGeometry(QRect(20, 70, 71, 16))
        self.output_v = QLabel(self.centralwidget)
        self.output_v.setObjectName(u"output_v")
        self.output_v.setGeometry(QRect(20, 120, 81, 21))
        self.source_l = QLineEdit(self.centralwidget)
        self.source_l.setObjectName(u"source_l")
        self.source_l.setGeometry(QRect(130, 30, 271, 20))
        self.dest_l = QLineEdit(self.centralwidget)
        self.dest_l.setObjectName(u"dest_l")
        self.dest_l.setGeometry(QRect(130, 70, 271, 20))
        self.output_l = QLineEdit(self.centralwidget)
        self.output_l.setObjectName(u"output_l")
        self.output_l.setGeometry(QRect(130, 120, 271, 20))
        self.source_p = QPushButton(self.centralwidget)
        self.source_p.setObjectName(u"source_p")
        self.source_p.setGeometry(QRect(400, 30, 21, 23))
        self.dest_p = QPushButton(self.centralwidget)
        self.dest_p.setObjectName(u"dest_p")
        self.dest_p.setGeometry(QRect(400, 70, 21, 23))
        self.output_p = QPushButton(self.centralwidget)
        self.output_p.setObjectName(u"output_p")
        self.output_p.setGeometry(QRect(400, 120, 21, 23))
        self.start_p = QPushButton(self.centralwidget)
        self.start_p.setObjectName(u"start_p")
        self.start_p.setGeometry(QRect(300, 152, 121, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.start_p.setFont(font1)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 200, 441, 23))
        self.progressBar.setValue(24)
        self.open_p = QPushButton(self.centralwidget)
        self.open_p.setObjectName(u"open_p")
        self.open_p.setGeometry(QRect(20, 240, 131, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 462, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HQ VFX FRT-V1.0", None))
        self.source_v.setText(QCoreApplication.translate("MainWindow", u"SOURCE VIDEO", None))
        self.dest_v.setText(QCoreApplication.translate("MainWindow", u"DEST VIDEO", None))
        self.output_v.setText(QCoreApplication.translate("MainWindow", u"OUPUT PATH", None))
        self.source_p.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.dest_p.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.output_p.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.start_p.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.open_p.setText(QCoreApplication.translate("MainWindow", u"OPEN OUTPUT DIR", None))
    # retranslateUi

