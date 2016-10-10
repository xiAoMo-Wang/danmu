# -*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore

import danmu_window


class DanmuApp(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        self.danmu_windows = list()

        QtGui.QWidget.__init__(self, *args, **kwargs)

        self.setWindowTitle('danmu')

        self.init_window()

        main_btn = QtGui.QPushButton('main button', self)

        self.connect(main_btn, QtCore.SIGNAL('clicked()'), self.button_clicked)

        desktop = QtGui.QDesktopWidget()
        screen_center = desktop.screenGeometry(desktop.primaryScreen()).center()
        # print screen_center
        self.resize(600, 400)
        self.move(screen_center.x() - self.width() / 2, screen_center.y() - self.height() / 2)

        self.show()

    def button_clicked(self):
        """
        按钮被点击的信号槽 打印出信号发出者的名称
        :return:
        """
        print self.sender().text()

    def init_window(self):
        """
        初始化屏幕窗口
        :return:
        为每个屏幕创建一个弹幕窗口 用于弹幕的显示 并将创建的Widget对象加入列表
        """
        # 获取QDesktopWidget
        desktop = QtGui.QDesktopWidget()
        # 获取屏幕数量
        screen_count = desktop.screenCount()
        # 遍历每个屏幕并为其创建DanmuWindow对象
        for i in range(screen_count):
            w = danmu_window.DanmuWindow(i, self)
            self.danmu_windows.append(w)
        # 调试用 打印出每个屏幕对应的窗口对象
        for w in self.danmu_windows:
            print w
