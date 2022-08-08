import hou
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtSvg


class Bookmarks(QtWidgets.QWidget):
    def __init__(self, parent):
        super(Bookmarks, self).__init__(
            parent
        )
        self.bookmarks = ["https://www.sidefx.com/docs/houdini/basics/config_menus.html#configuration-files", "https://www.youtube.com/shorts/psu7LYIyQAo"]
        self.widgets()
        # self.layouts()
        # self.connections()
        
    def widgets(self):
        self.container = QtWidgets.QGridLayout()
        for index, b in enumerate(self.bookmarks):
            widg = QtWidgets.QPushButton()
            widg.setText(b)
            widg.setFixedSize(100, 30)
            self.container.addWidget(widg)
            # widg.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
            