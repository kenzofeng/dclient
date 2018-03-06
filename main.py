import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QFileDialog, \
    QMessageBox, QTableWidget, QAbstractScrollArea, QTableWidgetItem, QProgressDialog
from PyQt5.QtCore import QRect, QCoreApplication, Qt
from form import Ui_Form
from config import myconfig
from mythreads import WorkThread


class mywindow(QDialog, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(986, 557)
        self.setupUi(self)
        self.ProjectPath.setText(myconfig.project)
        self.Tag.setText(myconfig.tag)
        self.show()
        self.wait = QProgressDialog('Loading.......', None, 0, 100)
        self.wait.setWindowFlag(Qt.WindowCloseButtonHint)
        self.wait.show()
        self.worker = WorkThread(self)
        self.worker.progress.connect(self.progress)
        self.worker.finished.connect(self.finished)
        self.worker.start()

    def progress(self, value):
        self.wait.setValue(int(value))

    def finished(self, dockerfile):
        self.textEdit.setHtml(dockerfile)
        RepositoriesView = MyTableView(self.tab_2)
        RepositoriesView.display_Repositories()
        RepositoriesView.get_Repositories()
        self.wait.setValue(100)

    def folderDialog(self):
        dialog = QFileDialog(self, 'Select Project Path')
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.show()
        if dialog.exec_() == QDialog.Accepted:
            return (dialog.selectedFiles()[0])

    def buildimage(self):
        projctpath = self.ProjectPath.text()
        tag = self.Tag.text()
        if not os.path.exists(projctpath):
            QMessageBox.critical(self, 'Error Message', 'Project Path is not exists',
                                 QMessageBox.Yes, QMessageBox.Yes)
        elif tag == "":
            QMessageBox.critical(self, 'Error Message', 'Please Input Tag\nTag Format:project_name:version\n'
                                                        'for example: accor-adapter:1.2.2',
                                 QMessageBox.Yes, QMessageBox.Yes)
        else:
            reply = QMessageBox.question(self, 'Message', 'docker build image?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                import mydocker
                mydocker.build_images(projctpath, self.textEdit.toPlainText(), self.Tag.text())

    def selectfolder(self):
        self.ProjectPath.setText(self.folderDialog())

    def closeEvent(self, QCloseEvent):
        myconfig.project = self.ProjectPath.text()
        myconfig.tag = self.Tag.text()
        myconfig.save_config()


class MyTableView(QTableWidget):
    def __init__(self, parent=None):
        super(MyTableView, self).__init__(parent)
        self.setObjectName("myview")

    def display_Repositories(self):
        self.setGeometry(QRect(10, 50, 961, 491))
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.setColumnCount(3)
        self.setRowCount(0)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setStretchLastSection(True)
        item = self.horizontalHeaderItem(0)
        item.setText(QCoreApplication.translate("Form", "Repository Name"))
        item = self.horizontalHeaderItem(1)
        item.setText(QCoreApplication.translate("Form", "Repository URI"))
        item = self.horizontalHeaderItem(2)
        item.setText(QCoreApplication.translate("Form", "Action"))
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 600)
        self.setColumnWidth(2, 100)

    def display_detail_Repository(self):
        item = self.horizontalHeaderItem(0)
        item.setText(QCoreApplication.translate("Form", "tag"))
        item = self.horizontalHeaderItem(1)
        item.setText(QCoreApplication.translate("Form", "URI"))
        item = self.horizontalHeaderItem(2)
        item.setText(QCoreApplication.translate("Form", "Action"))
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 600)
        self.setColumnWidth(2, 100)

    def delete_Repository(self):
        print(self.sender().index)

    def detail_Repository(self):
        print(self.sender().objectName())
        button = self.sender()
        print(button.pos())
        index = self.indexAt(button.pos())
        print(index.row(), index.column())

    def get_Repositories(self):
        import myaws
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setRowCount(len(myaws.reposiories))
        for row, rep in enumerate(myaws.reposiories):
            self.setItem(row, 0, QTableWidgetItem(rep["name"], ))
            self.setItem(row, 1, QTableWidgetItem(rep["uri"], ))
            deletebutton = QPushButton("Delete", self, clicked=self.delete_Repository)
            deletebutton.setStyleSheet("background-color: rgb(255,0,0);")
            deletebutton.index = [row, 1]
            deletebutton.setObjectName(rep["name"])
            detailbutton = QPushButton("Detail", self, clicked=self.detail_Repository)
            detailbutton.index = [row, 2]
            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(deletebutton)
            hLayout.addWidget(detailbutton)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)
            self.setCellWidget(row, 2, widget)


class MyProgressDialog(QProgressDialog):
    def __init__(self, parent=None):
        super(MyProgressDialog, self).__init__(parent)


class Mybutton(QPushButton):
    def __init__(self, parent=None):
        super(Mybutton, self).__init__(parent)
        self.index = None


app = QApplication(sys.argv)
window = mywindow()
sys.exit(app.exec_())
