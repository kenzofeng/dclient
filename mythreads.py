from PyQt5.QtCore import QThread, pyqtSignal
from remote import Remote

class WorkThread(QThread):
    finished = pyqtSignal(object)

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.parent = parent

    def run(self):
        dockerfile = Remote.dockerfile()
        # self.parent.wait.setValue(100)
        self.finished.emit(dockerfile)
