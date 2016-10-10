# -*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore

import danmu_window

class DanmuApp(QtGui.QWidget):

    def __init__(self, *args, **kwargs):
        self.danmu_windows = list()

        QtGui.QWidget.__init__(self, *args, **kwargs)

        self.setWindowTitle('danmu')

        self.init_windows()

        mainBtn = QtGui.QPushButton('main button', self)

        self.connect(mainBtn, QtCore.SIGNAL('clicked()'), self.buttonClicked)

        desktop = QtGui.QDesktopWidget()
        screen_center = desktop.screenGeometry(desktop.primaryScreen()).center()
        # print screen_center
        self.resize(600, 400)
        self.move(screen_center.x() - self.width() / 2, screen_center.y() - self.height() / 2)

        self.show()

    def buttonClicked(self):
        print self.sender().text()

    def init_windows(self):

        desktop = QtGui.QDesktopWidget()
        screen_count = desktop.screenCount()
        for i in range(screen_count):
            w = danmu_window.DanmuWindow(i, self)
            self.danmu_windows.append(w)
        for w in self.danmu_windows:
            print w
