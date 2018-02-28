import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget, QFileDialog, \
    QMessageBox, QTableWidget, QAbstractScrollArea, QTableWidgetItem, QProgressDialog
from PyQt5.QtCore import QRect, QCoreApplication
from form import Ui_Form
import text


class mywindow(QDialog, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.textEdit.setHtml(text.dockerfile)
        RepositoriesView = MyTableView(self.tab_2)
        RepositoriesView.display_Repositories()
        RepositoriesView.get_Repositories()

    def folderDialog(self):
        dialog = QFileDialog(self, 'select Project Path')
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.show()
        if dialog.exec_() == QDialog.Accepted:
            return (dialog.selectedFiles()[0])

    def buildimage(self):
        projctpath = self.ProjectPath.text()
        if projctpath != "":
            reply = QMessageBox.question(self, 'Message', 'docker build image?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                import mydocker
                mydocker.build_images(projctpath, self.textEdit.toPlainText(), self.Tag.text())

        else:
            print("Error Message:please select project path")

    def selectfolder(self):
        self.ProjectPath.setText(self.folderDialog())


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
        super(Deletebutton, self).__init__(parent)
        self.index = None


app = QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
