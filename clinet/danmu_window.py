# -*- coding:utf-8 -*-

from PyQt4 import QtGui, Qt


class DanmuWindow(QtGui.QWidget):
    def __init__(self, screen_number, parent, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)

        self.setParent(parent)

        desktop = QtGui.QDesktopWidget()
        geo = desktop.screenGeometry(screen_number)
        # print geo.topLeft()

        self.resize(geo.width(), geo.height())
        self.setWindowFlags(Qt.Qt.X11BypassWindowManagerHint
                            | Qt.Qt.WindowStaysOnTopHint
                            | Qt.Qt.ToolTip
                            | Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.Qt.WA_DeleteOnClose, True)
        self.setAttribute(Qt.Qt.WA_Disabled, True)
        self.setAttribute(Qt.Qt.WA_TransparentForMouseEvents, True)
        self.setStyleSheet('background: transparent')

        self.move(geo.topLeft())

        self.show()
        print self.testAttribute(Qt.Qt.WA_Disabled)


