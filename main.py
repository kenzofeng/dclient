import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QFileDialog, \
    QMessageBox, QProgressDialog
from ui.View import RepositoryView
from config import myconfig
from form import Ui_Form
from mythreads import WorkThread, BuildThread, PushThread
import mydocker


class mywindow(QDialog, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.setFixedSize(986, 557)
        self.setupUi(self)
        self.ProjectPath.setText(myconfig.project)
        self.Tag.setText(myconfig.tag)
        self.HOME.setCursor(Qt.PointingHandCursor)
        self.buildbutton.setCursor(Qt.PointingHandCursor)
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.show()
        self.wait = QProgressDialog('Loading.......', None, 0, 100, self)
        self.wait.setWindowTitle('info')
        self.wait.setWindowFlag(Qt.WindowCloseButtonHint)
        self.wait.show()
        self.worker = WorkThread(self)
        self.worker.progress.connect(self.set_wait)
        self.worker.finished.connect(self.finished)
        self.worker.start()
        self.RView = RepositoryView(self.tab_2)
        self.RView.display_Repositories()
        self.HOME.clicked.connect(self.RView.Home)

    def set_wait(self, value):
        self.wait.setValue(int(value))

    def setWaitCursor(self):
        self.wait.setCursor(Qt.WaitCursor)
        self.setCursor(Qt.WaitCursor)

    def setArrowCursor(self):
        self.setCursor(Qt.ArrowCursor)

    def finished(self, dockerfile):
        self.textEdit.setHtml(dockerfile)
        self.RView.get_Repositories()
        self.set_wait(100)
        self.setArrowCursor()

    def folderDialog(self):
        dialog = QFileDialog(self, 'Select Project Path')
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.show()
        if dialog.exec_() == QDialog.Accepted:
            return (dialog.selectedFiles()[0])

    def buildimage(self):
        projctpath = self.ProjectPath.text()
        docker_text = self.textEdit.toPlainText()
        tag_text = self.Tag.text()
        if not os.path.exists(projctpath):
            QMessageBox.critical(self, 'Error Message', 'Project Path is not exists',
                                 QMessageBox.Yes, QMessageBox.Yes)
        elif tag_text == "":
            QMessageBox.critical(self, 'Error Message', 'Please Input Tag\nTag Format:project_name:version\n'
                                                        'for example: accor-adapter:1.2.2',
                                 QMessageBox.Yes, QMessageBox.Yes)
        else:
            reply = QMessageBox.question(self, 'Message', 'build image?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.wait = QProgressDialog('build image.......', None, 0, 100)
                self.wait.setWindowTitle('info')
                self.wait.setWindowFlag(Qt.WindowCloseButtonHint)
                self.wait.show()
                build_worker = BuildThread(projctpath, docker_text, tag_text, self)
                build_worker.progress.connect(self.set_wait)
                build_worker.finished.connect(self.set_wait)
                build_worker.start()

    def pushimage(self):
        tag_text = self.Tag.text()
        if tag_text == "":
            QMessageBox.critical(self, 'Error Message', 'Please Input Tag\nTag Format:project_name:version\n'
                                                        'for example: accor-adapter:1.2.2',
                                 QMessageBox.Yes, QMessageBox.Yes)
        else:
            reply = QMessageBox.question(self, 'Message', 'push image?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.wait = QProgressDialog('build image.......', None, 0, 100)
                self.wait.setWindowTitle('info')
                self.wait.setWindowFlag(Qt.WindowCloseButtonHint)
                self.wait.show()
                build_worker = PushThread(tag_text, self)
                build_worker.progress.connect(self.set_wait)
                build_worker.finished.connect(self.set_wait)
                build_worker.start()

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
