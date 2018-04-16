from PyQt5.QtCore import QRect, QCoreApplication
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QWidget, QTableWidget, QAbstractScrollArea, QTableWidgetItem
from registry import myregistry


class RepositoryView(QTableWidget):
    def __init__(self, parent=None):
        super(RepositoryView, self).__init__(parent)
        self.setObjectName("rview")
        self.setGeometry(QRect(10, 50, 961, 491))
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.setColumnCount(2)
        self.setRowCount(0)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        self.horizontalHeader().setDefaultSectionSize(250)
        self.horizontalHeader().setStretchLastSection(True)

    def Home(self):
        self.display_Repositories()
        self.get_Repositories()

    def display_Repositories(self):
        item = self.horizontalHeaderItem(0)
        item.setText(QCoreApplication.translate("Form", "Repository Name"))
        item = self.horizontalHeaderItem(1)
        item.setText(QCoreApplication.translate("Form", "Action"))
        self.setColumnWidth(0, 700)
        self.setColumnWidth(1, 100)

    def display_Tags(self, name):
        item = self.horizontalHeaderItem(0)
        item.setText(QCoreApplication.translate("Form", "{} Tag".format(name)))
        item = self.horizontalHeaderItem(1)
        item.setText(QCoreApplication.translate("Form", "Action"))
        self.setColumnWidth(0, 700)
        self.setColumnWidth(1, 100)

    def delete_Repository(self):
        pass
        # print(self.sender().index)

    def detail_Repository(self):
        try:
            image_name = self.sender().objectName()
            self.display_Tags(image_name)
            self.get_Tags(image_name)
        except Exception as e:
            print(e)
        # print(self.sender().objectName())
        # button = self.sender()
        # print(button.pos())
        # index = self.indexAt(button.pos())
        # print(index.row(), index.column())

    def delete_tag(self):
        print(self.sender().index)

    def pull_tag(self):
        pass

    def get_Repositories(self):
        repositories = myregistry.repositories_list()
        self.setRowCount(len(repositories))
        for row, rep in enumerate(repositories):
            self.setItem(row, 0, QTableWidgetItem(rep, ))
            deletebutton = QPushButton("Delete", self, clicked=self.delete_Repository)
            deletebutton.setStyleSheet("background-color: rgb(255,0,0);")
            deletebutton.index = [row, 1]
            deletebutton.setObjectName(rep)
            detailbutton = QPushButton("Detail", self, clicked=self.detail_Repository)
            detailbutton.index = [row, 2]
            detailbutton.setObjectName(rep)
            widget = QWidget()
            hLayout = QHBoxLayout()
            hLayout.addWidget(deletebutton)
            hLayout.addWidget(detailbutton)
            hLayout.setContentsMargins(5, 2, 5, 2)
            widget.setLayout(hLayout)
            self.setCellWidget(row, 1, widget)

    def get_Tags(self, name):
        tags = myregistry.image_tags_list(name)
        if tags:
            self.setRowCount(len(tags))
            for row, rep in enumerate(tags):
                self.setItem(row, 0, QTableWidgetItem(rep, ))
                deletebutton = QPushButton("Delete", self, clicked=self.delete_tag)
                deletebutton.setStyleSheet("background-color: rgb(255,0,0);")
                deletebutton.index = [row, 1]
                deletebutton.setObjectName(rep)
                detailbutton = QPushButton("Pull", self, clicked=self.delete_tag)
                detailbutton.index = [row, 2]
                detailbutton.setObjectName(rep)
                widget = QWidget()
                hLayout = QHBoxLayout()
                hLayout.addWidget(deletebutton)
                hLayout.addWidget(detailbutton)
                hLayout.setContentsMargins(5, 2, 5, 2)
                widget.setLayout(hLayout)
                self.setCellWidget(row, 1, widget)
