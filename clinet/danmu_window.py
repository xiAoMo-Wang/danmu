# -*- coding:utf-8 -*-

from PyQt4 import QtGui, Qt


class DanmuWindow(QtGui.QWidget):
    def __init__(self, screen_number, parent, *args, **kwargs):
        """
        DanmuWindow初始化函数
        :param screen_number: int 所对应的屏幕编号
        :param parent: QWidget 父对象 DanmuApp
        为对应屏幕创建DanmuWindow
        窗口顶置 透明 直接透过鼠标与键盘操作到下一层 无边框
        """
        # 创建父类对象
        QtGui.QWidget.__init__(self, *args, **kwargs)
        # 设置父对象
        self.setParent(parent)

        # 获得屏幕编号对应的屏幕大小信息
        desktop = QtGui.QDesktopWidget()
        geo = desktop.screenGeometry(screen_number)
        # print geo.topLeft()

        # 设置窗口为全屏 高和宽均为屏幕高和宽
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

        #将窗口移动到屏幕左上角
        self.move(geo.topLeft())

        #显示窗口
        self.show()

        # 调试用
        print self.testAttribute(Qt.Qt.WA_Disabled)
