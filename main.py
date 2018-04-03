import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QFileDialog, \
    QMessageBox, QProgressDialog
from ui.View import RepositoryView, TagView
from config import myconfig
from form import Ui_Form
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
        RView = RepositoryView(self.tab_2)
        RView.display_Repositories()
        RView.get_Repositories()
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
