# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(986, 557)
        Form.setAcceptDrops(False)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 991, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.buildbutton = QtWidgets.QPushButton(self.tab)
        self.buildbutton.setGeometry(QtCore.QRect(870, 410, 91, 41))
        self.buildbutton.setObjectName("buildbutton")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 831, 491))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.ProjectPath = QtWidgets.QLineEdit(self.layoutWidget)
        self.ProjectPath.setObjectName("ProjectPath")
        self.gridLayout.addWidget(self.ProjectPath, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.Tag = QtWidgets.QLineEdit(self.layoutWidget)
        self.Tag.setObjectName("Tag")
        self.gridLayout.addWidget(self.Tag, 3, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.gridLayout.addWidget(self.groupBox, 6, 0, 1, 3)
        self.toolButton = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 2, 3, 1, 1)
        self.UseDockerFile = QtWidgets.QCheckBox(self.layoutWidget)
        self.UseDockerFile.setChecked(True)
        self.UseDockerFile.setObjectName("UseDockerFile")
        self.gridLayout.addWidget(self.UseDockerFile, 6, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(870, 470, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget.raise_()
        self.buildbutton.raise_()
        self.pushButton.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 961, 461))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(250)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.HOME = QtWidgets.QPushButton(self.tab_2)
        self.HOME.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.HOME.setObjectName("HOME")
        self.tabWidget.addTab(self.tab_2, "")
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.ProjectPath, self.buildbutton)
        Form.setTabOrder(self.buildbutton, self.tabWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Docker Client"))
        self.buildbutton.setText(_translate("Form", "Build"))
        self.label.setText(_translate("Form", "Project Path:"))
        self.label_2.setText(_translate("Form", "Tag:"))
        self.groupBox.setTitle(_translate("Form", "DockerFile:"))
        self.toolButton.setText(_translate("Form", "..."))
        self.UseDockerFile.setText(_translate("Form", "DockerFile"))
        self.pushButton.setText(_translate("Form", "push"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Docker Project"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Repository Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Action"))
        self.HOME.setText(_translate("Form", "HOME"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Docker Registry"))

