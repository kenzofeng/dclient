from PyQt5.QtCore import QThread, pyqtSignal
from remote import remote
import mydocker
from registry import myregistry


class WorkThread(QThread):
    finished = pyqtSignal(object)
    progress = pyqtSignal(object)

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.parent = parent

    def run(self):
        self.parent.setWaitCursor()
        self.progress.emit(50)
        dockerfile = remote.dockerfile()
        remote.getaccess()
        mydocker.docker_login_server()
        self.finished.emit(dockerfile)


class BuildThread(QThread):
    finished = pyqtSignal(object)
    progress = pyqtSignal(object)

    def __init__(self, projctpath, docker_text, tag_text, df_status, parent=None):
        super(BuildThread, self).__init__(parent)
        self.parent = parent
        self.projctpath = projctpath
        self.docker_text = docker_text
        self.tag_text = tag_text
        self.df_status = df_status

    def run(self):
        self.parent.setWaitCursor()
        self.progress.emit(50)
        mydocker.build_images(self.projctpath, self.docker_text, self.tag_text, self.df_status)
        self.finished.emit(100)


class PushThread(QThread):
    finished = pyqtSignal(object)
    progress = pyqtSignal(object)

    def __init__(self, tag_text, parent=None):
        super(PushThread, self).__init__(parent)
        self.parent = parent
        self.tag_text = tag_text

    def run(self):
        self.parent.setWaitCursor()
        self.progress.emit(50)
        mydocker.push_image(self.tag_text)
        self.finished.emit(100)


class DeleteThread(QThread):
    finished = pyqtSignal(object)
    progress = pyqtSignal(object)

    def __init__(self, image, tag, parent=None):
        super(DeleteThread, self).__init__(parent)
        self.parent = parent
        self.image = image
        self.tag = tag

    def run(self):
        self.parent.setWaitCursor()
        self.progress.emit(50)
        print(myregistry.delete_image(self.image, self.tag))
        self.finished.emit(self.image)


class PullThread(QThread):
    finished = pyqtSignal(object)
    progress = pyqtSignal(object)

    def __init__(self, image, tag, parent=None):
        super(PullThread, self).__init__(parent)
        self.parent = parent
        self.image = image
        self.tag = tag

    def run(self):
        self.parent.setWaitCursor()
        self.progress.emit(50)
        mydocker.pull_image(self.image, self.tag)
        self.finished.emit(100)
