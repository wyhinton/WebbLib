import hou
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtSvg
from PySide2 import QtGui

import webb
from webb.search_widget import WebSearcherWidget
from webb.bookmarks import Bookmarks
from importlib import reload
# reload(webb.search_widget)
# reload(webb.bookmarks)

class UtilityPalette(QtWidgets.QDialog):
    def __init__(self):
        super(UtilityPalette, self).__init__(
            hou.qt.mainWindow(),
        )
        #make window relative to size of parent
        self.relX = .2
        self.relY = .2
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        width = hou.qt.mainWindow().width()
        height = hou.qt.mainWindow().height()
        self.width =  width * self.relX
        self.height = height * self.relY
        self.isUtilityPalette = True
        self.web_search_widget = WebSearcherWidget(self)
        # self.bookmarks = Bookmarks(self)
        self.configure_dialog()
        self.widgets()
        self.layouts()
        self.connections()
    #release the searchInputs hold on the keyboard whenever the window is closed
    def closeEvent(self, event):
        self.web_search_widget.handleClose()
        # print("closed")

    def configure_dialog(self)->None:
        self.setMinimumWidth(self.width)
        self.setMinimumHeight(self.height)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setWindowFlags(self.windowFlags() |  QtCore.Qt.WindowStaysOnTopHint |  QtCore.Qt.X11BypassWindowManagerHint)
        self.setWindowFlags( QtCore.Qt.X11BypassWindowManagerHint| QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |  QtCore.Qt.X11BypassWindowManagerHint| QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self)

    def connections(self)->None:
        self.closeButton.mouseReleaseEvent = lambda event:self.close()

    def layouts(self)->None:
        self.container = QtWidgets.QWidget(self)
        self.container.setMinimumWidth(self.width)
        self.container.setMinimumHeight(self.height)
        # self.container.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
        self.grid = QtWidgets.QGridLayout(self)
        self.grid.addLayout(self.web_search_widget.container, 0, 0, 1, 1)
        # self.grid.addLayout(self.bookmarks.container, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        # self.grid.addWidget(self.closeButton, 1, 0, 1, 1)

        radius = 5
        self.container.setStyleSheet(
            """
            background:rgba(18, 18, 18, .7);
            border-top-left-radius:{0}px;
            border-bottom-left-radius:{0}px;
            border-top-right-radius:{0}px;
            border-bottom-right-radius:{0}px;
            """.format(radius)
        )
    
    #positions the popup at the mouse location see https://gist.github.com/justinfx/1951709
    def showEvent(self, event):
        # print("diing show")s
        geom = self.frameGeometry()
        geom.moveCenter(QtGui.QCursor.pos())
        self.setGeometry(geom)
        super(UtilityPalette, self).showEvent(event)
    
    def widgets(self)->None:
        self.closeButton = QtWidgets.QPushButton("Close")


def main():
    # print("running")
    for widget in hou.qt.mainWindow().children():
        try:
            if widget.isUtilityPalette:
                widget.close()
        except:
            None

    popup = UtilityPalette()
    popup.setModal(True)
    popup.show()


