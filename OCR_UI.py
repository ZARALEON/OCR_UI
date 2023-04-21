import argparse
import codecs
import logging
import os
import os.path as osp
import sys
from OCR_UI import __appname__
from OCR_UI.app import MainWindow
from OCR_UI.utils import newIcon
from PyQt5 import QtCore, QtGui, QtWidgets


def main():
    QtCore.QCoreApplication.setOrganizationDomain("ZARALEON")
    QtCore.QCoreApplication.setApplicationName(__appname__)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(__appname__)
    app.setWindowIcon(newIcon())
    win = MainWindow()

    win.show()
    win.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
