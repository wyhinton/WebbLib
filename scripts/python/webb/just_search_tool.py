import hou
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtSvg
from PySide2 import QtGui
import webbrowser
import urllib.parse

#embed svgs in tool rather than messing with file paths
class SVG():
    YT_LOGO = """<?xml version="1.0" encoding="UTF-8"?><svg id="Layer_2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 131.77 55.56"><defs><style>.cls-1{fill:#131313;}.cls-2{fill:#e42626;}</style></defs><g id="Layer_1-2"><g><path class="cls-2" d="M100.57,22.35c-.78,0-1.65,.47-2.47,1.22v16.14c.78,.8,1.65,1.18,2.45,1.18,1.41,0,2-.99,2-3.65v-11.44c0-2.66-.64-3.44-2.02-3.44m19.67,3.2c0-2.47-.64-3.2-2.21-3.2s-2.26,.71-2.26,3.18v2.94h4.47v-2.89"/><g><path class="cls-1" d="M49.18,44.94h-4.99v-2.92c-1.88,2.21-3.53,3.29-5.25,3.29-1.55,0-2.59-.71-3.15-2.05-.28-.82-.52-2.07-.52-3.93V18.12h4.99v21.79c.12,.71,.42,.99,1.06,.99,.94,0,1.84-.87,2.89-2.35V18.12h4.99v26.83M31.53,26.87c0-2.87-.54-5.01-1.55-6.35-1.32-1.88-3.41-2.59-5.53-2.59-2.4,0-4.24,.71-5.53,2.59-1.04,1.34-1.58,3.53-1.58,6.35v9.58c0,2.82,.47,4.8,1.51,6.12,1.32,1.88,3.48,2.82,5.58,2.82s4.28-.94,5.65-2.82c.94-1.32,1.41-3.29,1.41-6.12v-9.62l.05,.05Zm-4.94,10.12c.24,2.66-.59,4-2.12,4s-2.35-1.34-2.12-4v-10.64c-.24-2.66,.56-3.91,2.12-3.91s2.35,1.25,2.12,3.91v10.64Zm-14.75-6.64v14.59H6.59v-14.59S1.11,12.38,0,9.04H5.53l3.69,14.02,3.67-14h5.51l-6.59,21.27"/><path class="cls-2" d="M131,11.95s-.78-5.41-3.13-7.84c-2.99-3.18-6.35-3.18-7.86-3.34-10.99-.78-27.48-.78-27.48-.78h-.05s-16.47,0-27.46,.78c-1.53,.19-4.89,.19-7.88,3.34-2.35,2.4-3.11,7.84-3.11,7.84,0,0-.8,6.4-.8,12.8v6c0,6.4,.8,12.78,.8,12.78,0,0,.75,5.46,3.11,7.86,2.99,3.15,6.92,3.06,8.66,3.36,6.28,.61,26.71,.8,26.71,.8,0,0,16.54,0,27.53-.8,1.53-.19,4.87-.19,7.86-3.34,2.35-2.4,3.13-7.86,3.13-7.86,0,0,.75-6.38,.75-12.8v-6c0-6.4-.78-12.8-.78-12.8Zm-60.52,32.99h-5.25V14.35h-5.53v-4.99h16.57v4.99h-5.77v30.59h-.02Zm18.94,0h-4.99v-2.92c-1.88,2.21-3.53,3.29-5.25,3.29-1.55,0-2.59-.71-3.15-2.05-.28-.82-.52-2.07-.52-3.93V18.35h4.99v21.58c.12,.71,.42,.99,1.06,.99,.94,0,1.84-.87,2.89-2.35V18.35h4.96v26.59Zm18.12-7.95c0,2.45-.16,4.19-.47,5.32-.66,1.98-2.05,2.99-3.93,2.99-1.69,0-3.44-1.04-5.04-3.01v2.68h-4.75V9.37h4.71v11.58c1.55-1.88,3.29-2.99,5.06-2.99,1.88,0,3.15,1.11,3.76,3.06,.35,1.11,.66,2.82,.66,5.34v10.64Zm10.49,3.93c1.18,0,1.88-.66,2.12-1.95,.05-.24,.05-1.41,.05-3.34h4.99v.75c0,1.55-.12,2.66-.16,3.13-.16,1.08-.54,2.05-1.11,2.89-1.32,1.93-3.29,2.87-5.77,2.87s-4.35-.89-5.74-2.73c-1.01-1.34-1.65-3.29-1.65-6.12v-9.32c0-2.82,.59-5.04,1.6-6.4,1.36-1.81,3.29-2.78,5.69-2.78s4.28,.94,5.65,2.78c.94,1.36,1.53,3.44,1.53,6.28v5.48h-9.46v4.75c0,2.47,.71,3.69,2.31,3.69h-.05Z"/></g></g></g></svg>"""
    GOOGLE_LOGO = """<?xml version="1.0" encoding="UTF-8"?><svg id="Layer_2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 166.67 54.86"><defs><style>.cls-1{fill:#ea4535;}.cls-2{fill:#36a852;}.cls-3{fill:#f9bc15;}.cls-4{fill:#557ebf;}</style></defs><g id="Layer_1-2"><g><path class="cls-1" d="M71.32,28.87c0,7.89-6.17,13.71-13.75,13.71s-13.75-5.82-13.75-13.71,6.17-13.71,13.75-13.71,13.75,5.76,13.75,13.71Zm-6.02,0c0-4.93-3.58-8.31-7.73-8.31s-7.73,3.37-7.73,8.31,3.58,8.31,7.73,8.31,7.73-3.43,7.73-8.31Z"/><path class="cls-3" d="M100.99,28.87c0,7.89-6.17,13.71-13.75,13.71s-13.75-5.82-13.75-13.71,6.17-13.71,13.75-13.71,13.75,5.76,13.75,13.71Zm-6.02,0c0-4.93-3.58-8.31-7.73-8.31s-7.73,3.37-7.73,8.31,3.58,8.31,7.73,8.31,7.73-3.43,7.73-8.31Z"/><path class="cls-4" d="M129.43,15.99v24.61c0,10.12-5.97,14.26-13.03,14.26-6.64,0-10.64-4.44-12.15-8.08l5.24-2.18c.93,2.23,3.22,4.86,6.9,4.86,4.52,0,7.32-2.79,7.32-8.04v-1.97h-.21c-1.35,1.66-3.94,3.12-7.22,3.12-6.85,0-13.13-5.97-13.13-13.65s6.28-13.76,13.13-13.76c3.27,0,5.87,1.45,7.22,3.07h.21v-2.23h5.72Zm-5.29,12.92c0-4.83-3.22-8.36-7.32-8.36s-7.63,3.53-7.63,8.36,3.48,8.26,7.63,8.26,7.32-3.48,7.32-8.26Z"/><path class="cls-2" d="M138.85,1.56V41.74h-5.87V1.56h5.87Z"/><path class="cls-1" d="M161.74,33.38l4.67,3.12c-1.51,2.23-5.14,6.08-11.42,6.08-7.79,0-13.6-6.02-13.6-13.71,0-8.15,5.87-13.71,12.93-13.71s10.59,5.66,11.73,8.72l.62,1.56-18.33,7.59c1.4,2.75,3.59,4.15,6.64,4.15s5.19-1.51,6.75-3.8h0Zm-14.38-4.93l12.25-5.09c-.67-1.71-2.7-2.91-5.09-2.91-3.06,0-7.32,2.7-7.16,7.99Z"/><path class="cls-4" d="M21.59,25.31v-5.82h19.6c.19,1.01,.29,2.21,.29,3.51,0,4.36-1.19,9.76-5.04,13.6-3.74,3.89-8.52,5.97-14.85,5.97-11.73,0-21.6-9.56-21.6-21.29S9.87,0,21.6,0c6.49,0,11.11,2.55,14.59,5.87l-4.1,4.1c-2.49-2.34-5.87-4.15-10.49-4.15-8.57,0-15.27,6.9-15.27,15.47s6.7,15.47,15.27,15.47c5.56,0,8.72-2.23,10.75-4.26,1.64-1.64,2.73-3.99,3.15-7.2h-13.9Z"/></g></g></svg>"""
    SIDEFX_LOGO = """<?xml version="1.0" encoding="UTF-8"?><svg id="Layer_2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 266.03 57.12"><defs><style>.cls-1{fill:#fff;}.cls-2{fill:#f26722;}</style></defs><g id="Layer_1-2"><g><g><path class="cls-2" d="M14.68,35.39c2.79-.54,3.92-3.04,3.93-4.92,.01-2.02-1.85-5.23-6.51-5.19-5.92,.17-9.56,4.33-9.74,9.48-.18,6.47,5.85,10.76,12.12,10.94,9.19,.2,14.66-5.83,14.64-14.6,.05-7.94-6.31-15.7-15.91-16.04-5.22-.31-9.61,1.12-12.97,3.47l-.04,5.92c3.16-3.67,7.9-5.38,12.01-5.29,6.96,.11,12.29,5.44,12.32,11.36-.04,5.71-2.43,9.87-8.84,10.81-3.48,.54-8.97-1.52-8.66-6.81,.16-2.71,2.25-4.23,4.69-4.15-2.46,3.19,.73,5.5,2.96,5.03Z"/><path class="cls-2" d="M46.98,35.94l8.47,4.37,.07-12.04-6.83,.65,6.85-3.72,.15-24.78-13.64-.08c.54,1.95,2.49,3.36,2.47,6.56-.03,4.46-5.33,5.47-5.42,10.06-.1,4.46,3.17,5.59,3.28,9.28,.05,3.62-1.49,5.28-1.49,5.28,0,0,.91-1.11,.51-3.83-.73-5.5-5.95-5.95-6.06-10.76-.11-4.18,2.89-5.13,2.91-8.89-.04-4.11-3.79-5.59-4.2-7.82L.34,0l-.08,12.88c3.63-2.07,8.03-3.29,12.97-3.26,13.44,.08,21.94,9.54,21.87,21.37-.08,12.25-8.69,19.93-20.17,19.99-6.61,.1-11.75-2.72-14.86-6.57l-.07,11,36.34,.23,4.34-15.64,3.66,15.76,11,.07,.06-10.37-8.43-9.52Z"/></g><g><path class="cls-1" d="M64.78,49.76l2.95-3.39c4.29,3.93,8.46,5.9,14.24,5.94,5.57,.03,9.28-2.94,9.3-7.04v-.07c.02-3.83-2.05-6.07-10.74-7.93-9.52-2.15-13.96-5.24-13.92-12.06v-.14c.04-6.54,5.85-11.31,13.72-11.26,6.06,.04,10.36,1.8,14.59,5.17l-2.74,3.6c-3.88-3.16-7.7-4.57-12.02-4.6-5.43-.03-8.86,2.94-8.88,6.63v.14c-.03,3.9,2.12,6.14,11.23,8.15,9.25,2.08,13.54,5.51,13.5,11.85v.14c-.05,7.1-5.99,11.73-14.28,11.68-6.61-.04-12.03-2.3-16.94-6.79Z"/><path class="cls-1" d="M100.93,13.57l5.22,.03-.03,5.08-5.22-.03,.03-5.08Zm.21,11.77l4.59,.03-.19,30.7-4.59-.03,.19-30.7Z"/><path class="cls-1" d="M110.99,40.86v-.14c.06-10.02,7.41-15.97,14.79-15.92,5.71,.04,9.38,3.12,11.72,6.62l.12-18.52,4.59,.03-.27,43.37-4.59-.03,.04-6.2c-2.53,3.67-6.17,6.78-11.81,6.75-7.38,.02-14.65-5.87-14.59-15.96Zm26.59,.1v-.14c.05-7.1-5.36-11.87-11.06-11.9-5.92-.04-10.82,4.32-10.86,11.77v.14c-.05,7.24,5.01,11.94,10.72,11.97s11.17-4.73,11.21-11.84Z"/><path class="cls-1" d="M146.85,41.08v-.14c.06-8.84,6.37-15.97,14.86-15.92,9.12,.06,14.3,7.33,14.24,16.31,0,.63,0,.97-.08,1.46l-24.37-.15c.58,6.69,5.3,10.41,10.73,10.44,4.25,.03,7.18-1.7,9.7-4.26l2.84,2.59c-3.08,3.39-6.86,5.74-12.71,5.7-8.42-.05-15.28-6.57-15.22-16.04Zm24.38-1.66c-.45-5.57-3.62-10.47-9.75-10.5-5.36-.03-9.43,4.4-10.02,10.38l19.77,.12Z"/><path class="cls-1" d="M181.82,14.98l31.68,.2-.05,8.28-22.49-.14-.06,8.84,19.84,.12-.05,8.28-19.84-.12-.1,16.08-9.12-.06,.26-41.49h-.07Z"/><path class="cls-1" d="M254.78,15.44l-14.05,20.24,14.35,21.32-10.72-.07-9.17-14.33-9.49,14.21-10.37-.06,14.61-21.07-13.8-20.55,10.72,.07,8.62,13.56,8.93-13.45,10.37,.06v.07Z"/></g><path class="cls-1" d="M257.96,19.22c0-.35,.07-.7,.15-1.04s.21-.69,.42-.97l.63-.83c.21-.28,.49-.48,.84-.62,.28-.21,.63-.27,.98-.41,.35-.07,.7-.13,1.05-.13s.7,.07,1.04,.15,.69,.21,.97,.42l.83,.63c.28,.28,.48,.49,.62,.84,.21,.28,.27,.63,.41,.98,.07,.35,.13,.7,.13,1.05s-.07,.7-.15,1.04-.21,.63-.42,.97c-.14,.28-.35,.55-.63,.83s-.49,.48-.84,.62-.63,.27-.98,.41c-.35,.07-.7,.13-1.05,.13s-.7-.07-1.04-.15-.63-.21-.97-.42l-.83-.63c-.28-.28-.48-.49-.62-.84-.21-.28-.27-.63-.41-.98-.07-.35-.13-.7-.13-1.05Zm.63,0c0,.49,.06,.91,.27,1.32s.41,.77,.69,1.12c.28,.28,.62,.56,1.04,.7,.42,.21,.83,.28,1.32,.29,.28,0,.63-.07,.91-.13s.56-.21,.84-.34c.28-.14,.49-.35,.7-.55s.35-.42,.56-.69c.14-.28,.28-.56,.35-.83,.07-.28,.14-.63,.14-.9s-.07-.63-.13-.91-.21-.56-.34-.84c-.14-.28-.35-.49-.55-.7s-.42-.42-.69-.56-.49-.28-.83-.35c-.28-.07-.63-.14-.9-.14-.49,0-.91,.06-1.32,.27s-.77,.41-1.05,.76c-.28,.28-.56,.69-.7,1.11-.21,.49-.28,.9-.29,1.39Zm2.64,.57v1.81h-1.06l.03-4.88h1.67c.63,.01,1.11,.16,1.46,.37,.28,.21,.48,.56,.48,1.05,0,.35-.07,.63-.28,.83-.21,.21-.42,.42-.84,.48,.07,.07,.14,.07,.21,.14,.07,.07,.07,.14,.14,.21l1.1,1.75h-.97c-.14,0-.28-.08-.28-.15l-.9-1.54-.14-.14c-.07,0-.14-.07-.21-.07h-.42v.14Zm0-.7h.56c.21,0,.35,0,.49-.06,.14,0,.21-.07,.28-.14s.14-.14,.14-.28c0-.07,.07-.21,.07-.35s0-.21-.07-.35c0-.07-.07-.14-.14-.21-.07-.07-.14-.14-.28-.14s-.28-.07-.42-.07h-.63v1.6Z"/></g></g></svg>"""
    CLOSE_ICON = """<?xml version="1.0" encoding="UTF-8"?><svg id="Layer_2" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6.92 6.92"><defs><style>.cls-1{fill:#e42626;}</style></defs><g id="Layer_1-2"><path class="cls-1" d="M6.83,1.29L5.63,.09c-.12-.12-.32-.12-.45,0l-1.75,1.75L1.71,.12c-.12-.12-.32-.12-.45,0L.12,1.26c-.12,.12-.12,.32,0,.45l1.72,1.72L.09,5.18c-.12,.12-.12,.32,0,.45l1.2,1.2c.12,.12,.32,.12,.45,0l1.75-1.75,1.72,1.72c.12,.12,.32,.12,.45,0l1.14-1.14c.12-.12,.12-.32,0-.45l-1.72-1.72,1.75-1.75c.12-.12,.12-.32,0-.45Z"/></g></svg>"""

class SearchPlatform():
    def __init__(self, baseUrl, svg, name, searchVar, home_url):
        self.baseUrl = baseUrl
        self.searchVar = searchVar
        self.svg = svg
        self.name = name
        self.homeUrl = "https://www.youtube.com/"

YouTube = SearchPlatform("https://www.youtube.com/results?", SVG.YT_LOGO, "YouTube", "search_query","https://www.youtube.com/" )  
Google = SearchPlatform("https://www.google.com/search?", SVG.GOOGLE_LOGO, "Google", "q", "https://www.google.com/")  
SideFX = SearchPlatform("https://www.sidefx.com/forum/search/?action=search&search_in=all&sort_by=0&sort_dir=DESC&forum=0&show_as=topics&", SVG.SIDEFX_LOGO, "SideFX Forums", "keywords", "https://www.sidefx.com/forum/")  
Platforms = [Google, YouTube, SideFX]

#extend QLineEdit to add custom handling of Tab press 
class LineInput(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(LineInput, self).__init__(
            # parent
        )
        self.window = parent
    def keyPressEvent(self, event):
        if(event.key() == QtCore.Qt.Key_Tab):
            self.window.switchSearch()
        QtWidgets.QLineEdit.keyPressEvent(self, event)

class SearchPopup(QtWidgets.QDialog):
    def __init__(self, platform: SearchPlatform = Google):
        super(SearchPopup, self).__init__(
            hou.qt.mainWindow(),
        )
        #make window relative to size of parent
        self.relX = .2
        self.relY = .075
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        width = hou.qt.mainWindow().width()
        height = hou.qt.mainWindow().height()
        self.width =  width * self.relX
        self.height = height * self.relY
        
        self.platform = platform
        self.searchTerm = ""
        self.url = ""

        self.configure_dialog()
        self.widgets()
        self.layouts()
        self.connections()
    #release the searchInputs hold on the keyboard whenever the window is closed
    def closeEvent(self):
        self.searchInput.releaseKeyboard()

    def configure_dialog(self)->None:
        self.setMinimumWidth(self.width)
        self.setMinimumHeight(self.height)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setWindowFlags(self.windowFlags() |  QtCore.Qt.WindowStaysOnTopHint |  QtCore.Qt.X11BypassWindowManagerHint)
        self.setWindowFlags( QtCore.Qt.X11BypassWindowManagerHint| QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |  QtCore.Qt.X11BypassWindowManagerHint| QtCore.Qt.Popup | QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self)

    def connections(self)->None:
        self.searchInput.textChanged.connect(self.updateSearchTerm)
        self.searchInput.returnPressed.connect(self.searchInternet)
        self.searchInput.installEventFilter(self.searchInput)
        self.icon.mouseReleaseEvent = lambda event:self.openHomePage()
        self.closeButton.mouseReleaseEvent = lambda event:self.close()

    def layouts(self)->None:
        self.container = QtWidgets.QWidget(self)
        self.container.setMinimumWidth(self.width)
        self.container.setMinimumHeight(self.height)
        # self.container.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
        self.hBox = QtWidgets.QVBoxLayout(self)
        self.hBox.addWidget(self.icon)
        self.hBox.addWidget(self.searchInput)

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
    
    def openHomePage(self)->None:
        webbrowser.open(self.platform.homeUrl)    

    def searchInternet(self)->None:
        if self.searchTerm != "":
            webbrowser.open(self.url)
            self.close()
    
    #positions the popup at the mouse location see https://gist.github.com/justinfx/1951709
    def showEvent(self, event):
        geom = self.frameGeometry()
        geom.moveCenter(QtGui.QCursor.pos())
        self.setGeometry(geom)
        super(SearchPopup, self).showEvent(event)

    def switchSearch(self)->None:
        curInd = Platforms.index(self.platform)
        newInd = (curInd + 1) % len(Platforms) 
        self.updatePlatform(Platforms[newInd])
    
    def updatePlatform(self, platform):
        self.platform = platform
        self.updateSvg(self.platform.svg)
        self.searchInput.setPlaceholderText("Search {}".format(self.platform.name))
        
    def updateSearchTerm(self)->None:
        self.searchTerm = self.searchInput.text()
        if self.searchTerm != "":
            self.searchInput.setStyleSheet(
            """
            border: 1px solid grey;
            border-color: #52BD95;
            """
        )
        else:
            self.searchInput.setStyleSheet(
            """
            border: 1px solid grey;
            border-color: #8ea6bb;
            """
        )
        self.formatSearchLink()
    
    def formatSearchLink(self)->str:
        params = {self.platform.searchVar: self.searchTerm}
        search = urllib.parse.urlencode(params)
        url = self.platform.baseUrl + search
        self.url = url

    def makeSvg(self, svg_string: str)->QtSvg.QSvgWidget:
        svg_bytes = bytearray(svg_string, encoding='utf-8')
        defaultSize = QtSvg.QSvgRenderer(svg_bytes).defaultSize()
        svgWidget = QtSvg.QSvgWidget()
        svgWidget.renderer().load(svg_bytes)
        svgWidget.setGeometry(100,100,100,100)
        svgWidget.setFixedSize(defaultSize)
        svgWidget.setStyleSheet(
            """
            background:rgba(18, 18, 18, 0);
            """
        )
        return svgWidget
    
    def updateSvg(self, svg_string):
        svg_bytes = bytearray(svg_string, encoding='utf-8')
        defaultSize = QtSvg.QSvgRenderer(svg_bytes).defaultSize()
        svgWidget = self.icon
        svgWidget.renderer().load(svg_bytes)
        svgWidget.setGeometry(100,100,100,100)
        svgWidget.setFixedSize(defaultSize)
        svgWidget.setStyleSheet(
            """
            background:rgba(18, 18, 18, 0);
            """
        )
    
    def widgets(self)->None:
        self.searchInput = LineInput(self)
        f = self.searchInput.font()
        f.setPointSize(14)
        self.searchInput.setFont(f)
        #grab the keyboard so we can automatically start typing in the LineInput
        self.searchInput.grabKeyboard()
        self.searchInput.setPlaceholderText("Search {}".format(self.platform.name))
        self.searchInput.setStyleSheet(
            """
            border: 1px solid grey;
            border-color: #8ea6bb;
            """
        )
        self.searchInput.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self.closeButton = QtWidgets.QPushButton("Close")
        self.icon = self.makeSvg(self.platform.svg)

def main():
    for widget in hou.qt.mainWindow().children():
        try:
            if widget.isSearchWindow:
                widget.close()
        except:
            None

    popup = SearchPopup()
    popup.setModal(True)
    popup.show()


