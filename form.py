# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1004, 557)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1031, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(910, 480, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(20, 30, 611, 401))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Version = QtWidgets.QLineEdit(self.widget)
        self.Version.setObjectName("Version")
        self.gridLayout.addWidget(self.Version, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ProjectPath = QtWidgets.QLineEdit(self.widget)
        self.ProjectPath.setObjectName("ProjectPath")
        self.gridLayout.addWidget(self.ProjectPath, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setMinimumSize(QtCore.QSize(585, 302))
        self.textEdit.setMaximumSize(QtCore.QSize(585, 302))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)
        self.ProjectPath.raise_()
        self.label.raise_()
        self.groupBox.raise_()
        self.Version.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.groupBox.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(Form.buildimage)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.ProjectPath, self.Version)
        Form.setTabOrder(self.Version, self.textEdit)
        Form.setTabOrder(self.textEdit, self.pushButton)
        Form.setTabOrder(self.pushButton, self.tabWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Docker Client"))
        self.pushButton.setText(_translate("Form", "Build"))
        self.label.setText(_translate("Form", "Project Path:"))
        self.label_2.setText(_translate("Form", "Version:"))
        self.groupBox.setTitle(_translate("Form", "DockerFile:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))

