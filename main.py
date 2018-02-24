import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem,QPushButton,QHBoxLayout,QWidget,QAbstractItemView
from form import Ui_Form
import text


class mywindow(QDialog, Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.textEdit.setText(text.dockerfile)
        self.addtableItem()

    def addtableItem(self):
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setColumnWidth(1,600)
        self.tableWidget.setColumnWidth(2,100)

        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setRowCount(2)
        deletebutton = QPushButton('delete')
        deletebutton.setStyleSheet("background-color: rgb(255,0,0);")
        detailbutton = QPushButton('datail')
        widget = QWidget()
        hLayout = QHBoxLayout()
        hLayout.addWidget(deletebutton)
        hLayout.addWidget(detailbutton)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        self.tableWidget.setCellWidget(0,2,widget)
        self.tableWidget.setItem(0, 1, QTableWidgetItem("text2", ))
        # self.tableWidget.do

    def buildimage(self):
        import io
        import mydocker
        projctpath = self.ProjectPath.text()
        df = io.BytesIO(self.textEdit.toPlainText().encode('utf-8'))
        # mydocker.build_images(projctpath, df)


app = QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())
