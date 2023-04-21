# -*- coding:utf-8 -*-

import logging
import sys

from PyQt5.QtCore import PYQT_VERSION_STR as QT_VERSION

__appname__="Albedo"


__version__ = "1.0"


QT4 = QT_VERSION[0] == "4"
QT5 = QT_VERSION[0] == "5"
del QT_VERSION

PY2 = sys.version[0] == "2"
PY3 = sys.version[0] == "3"
del sys
