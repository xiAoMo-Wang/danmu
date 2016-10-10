# -*- coding:utf-8 -*-

import sys

from PyQt4 import QtGui

import danmu_app

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    dm_app = danmu_app.DanmuApp()

    sys.exit(app.exec_())