# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/case_lights.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CaseLights(object):
    def setupUi(self, CaseLights):
        CaseLights.setObjectName("CaseLights")
        CaseLights.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CaseLights)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(-1, -1, -1, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout.addWidget(self.pauseButton, 2, 0, 1, 1)
        self.whiteButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whiteButton.sizePolicy().hasHeightForWidth())
        self.whiteButton.setSizePolicy(sizePolicy)
        self.whiteButton.setObjectName("whiteButton")
        self.gridLayout.addWidget(self.whiteButton, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.rgbButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rgbButton.sizePolicy().hasHeightForWidth())
        self.rgbButton.setSizePolicy(sizePolicy)
        self.rgbButton.setObjectName("rgbButton")
        self.gridLayout.addWidget(self.rgbButton, 0, 0, 1, 1)
        self.pulseButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pulseButton.sizePolicy().hasHeightForWidth())
        self.pulseButton.setSizePolicy(sizePolicy)
        self.pulseButton.setObjectName("pulseButton")
        self.gridLayout.addWidget(self.pulseButton, 0, 1, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        CaseLights.setCentralWidget(self.centralwidget)

        self.retranslateUi(CaseLights)
        QtCore.QMetaObject.connectSlotsByName(CaseLights)

    def retranslateUi(self, CaseLights):
        _translate = QtCore.QCoreApplication.translate
        CaseLights.setWindowTitle(_translate("CaseLights", "MainWindow"))
        self.pauseButton.setText(_translate("CaseLights", "Pause"))
        self.whiteButton.setText(_translate("CaseLights", "White"))
        self.pushButton_7.setText(_translate("CaseLights", "N/A"))
        self.rgbButton.setText(_translate("CaseLights", "RGB"))
        self.pulseButton.setText(_translate("CaseLights", "Pulse"))
        self.clearButton.setText(_translate("CaseLights", "Clear"))

