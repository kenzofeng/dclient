import sys
from PyQt5.QtWidgets import QApplication, QDialog
from form import Ui_Form
import text
import mydocker
import io


class mywindow(QDialog, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.textEdit.setText(text.dockerfile)

    def buildimage(self):
        projctpath = self.ProjectPath.text()
        df = io.BytesIO(self.textEdit.toPlainText().encode('utf-8'))
        mydocker.build_images(projctpath, df)


app = QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
