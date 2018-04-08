from PyQt5.QtCore import QThread, pyqtSignal
from remote import Remote
import mydocker


class WorkThread(QThread):
    finished = pyqtSignal(object)
    progress = pyqtSignal(object)

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.parent = parent

    def run(self):
        self.progress.emit(50)
        dockerfile = Remote.dockerfile()
        self.finished.emit(dockerfile)


class BuildThread(QThread):
    finished = pyqtSignal(object)
    progress = pyqtSignal(object)

    def __init__(self, projctpath, docker_text, tag_text, parent=None):
        super(BuildThread, self).__init__(parent)
        self.parent = parent
        self.projctpath = projctpath
        self.docker_text = docker_text
        self.tag_text = tag_text

    def run(self):
        self.progress.emit(50)
        mydocker.build_images(self.projctpath, self.docker_text, self.tag_text)
        self.finished.emit(100)


class PushThread(QThread):
    finished = pyqtSignal(object)
    progress = pyqtSignal(object)

    def __init__(self, tag_text, parent=None):
        super(PushThread, self).__init__(parent)
        self.parent = parent
        self.tag_text = tag_text

    def run(self):
        self.progress.emit(50)
        mydocker.push_image(self.tag_text)
        self.finished.emit(100)
