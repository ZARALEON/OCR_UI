# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1131, 689)
        MainWindow.setStyleSheet("QWidget{\n"
"    font: 10pt \"Microsoft YaHei UI\";\n"
"}\n"
"")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnOpenImg = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenImg.sizePolicy().hasHeightForWidth())
        self.btnOpenImg.setSizePolicy(sizePolicy)
        self.btnOpenImg.setMinimumSize(QtCore.QSize(0, 0))
        self.btnOpenImg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnOpenImg.setObjectName("btnOpenImg")
        self.verticalLayout_5.addWidget(self.btnOpenImg)
        self.btnOpenDir = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenDir.setObjectName("btnOpenDir")
        self.verticalLayout_5.addWidget(self.btnOpenDir)
        self.btnEditShape = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditShape.setObjectName("btnEditShape")
        self.verticalLayout_5.addWidget(self.btnEditShape)
        self.btnAddShape = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddShape.setObjectName("btnAddShape")
        self.verticalLayout_5.addWidget(self.btnAddShape)
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setObjectName("btnNext")
        self.verticalLayout_5.addWidget(self.btnNext)
        self.btnPrev = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrev.setObjectName("btnPrev")
        self.verticalLayout_5.addWidget(self.btnPrev)
        self.btnStartProcess = QtWidgets.QPushButton(self.centralwidget)
        self.btnStartProcess.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btnStartProcess.setFont(font)
        self.btnStartProcess.setAutoFillBackground(False)
        self.btnStartProcess.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 160, 230) ;\n"
"border-radius: 5px;\n"
"height: 28;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"font-size: 16px bold;\n"
"margin: 2px 2px;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"border: 2px solid rgb(0, 160, 230);\n"
"color: black\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 255, 40);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../zsy/.designer/icons/done_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStartProcess.setIcon(icon)
        self.btnStartProcess.setFlat(False)
        self.btnStartProcess.setObjectName("btnStartProcess")
        self.verticalLayout_5.addWidget(self.btnStartProcess)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.scrollAreaCanvas = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaCanvas.setWidgetResizable(True)
        self.scrollAreaCanvas.setObjectName("scrollAreaCanvas")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 694, 627))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaCanvas.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollAreaCanvas)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidgetResult = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetResult.setObjectName("tabWidgetResult")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollAreaLabellist = QtWidgets.QScrollArea(self.tab)
        self.scrollAreaLabellist.setWidgetResizable(True)
        self.scrollAreaLabellist.setObjectName("scrollAreaLabellist")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 241, 571))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaLabellist.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.addWidget(self.scrollAreaLabellist)
        self.tabWidgetResult.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.listWidgetResults = QtWidgets.QListWidget(self.tab_2)
        self.listWidgetResults.setSelectionRectVisible(False)
        self.listWidgetResults.setObjectName("listWidgetResults")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.listWidgetResults.addItem(item)
        self.verticalLayout_6.addWidget(self.listWidgetResults)
        self.btnCopyAll = QtWidgets.QPushButton(self.tab_2)
        self.btnCopyAll.setObjectName("btnCopyAll")
        self.verticalLayout_6.addWidget(self.btnCopyAll)
        self.btnSaveAll = QtWidgets.QPushButton(self.tab_2)
        self.btnSaveAll.setObjectName("btnSaveAll")
        self.verticalLayout_6.addWidget(self.btnSaveAll)
        self.tabWidgetResult.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidgetResult)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(1, 8)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1131, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidgetResult.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "demo"))
        self.btnOpenImg.setText(_translate("MainWindow", "打开图片"))
        self.btnOpenDir.setText(_translate("MainWindow", "打开文件夹"))
        self.btnEditShape.setText(_translate("MainWindow", "编辑区域"))
        self.btnAddShape.setText(_translate("MainWindow", "添加区域"))
        self.btnNext.setText(_translate("MainWindow", "下一张"))
        self.btnPrev.setText(_translate("MainWindow", "上一张"))
        self.btnStartProcess.setText(_translate("MainWindow", "开始"))
        self.label.setText(_translate("MainWindow", "识别结果"))
        self.tabWidgetResult.setTabText(self.tabWidgetResult.indexOf(self.tab), _translate("MainWindow", "区域"))
        __sortingEnabled = self.listWidgetResults.isSortingEnabled()
        self.listWidgetResults.setSortingEnabled(False)
        item = self.listWidgetResults.item(0)
        item.setText(_translate("MainWindow", "测试1"))
        self.listWidgetResults.setSortingEnabled(__sortingEnabled)
        self.btnCopyAll.setText(_translate("MainWindow", "复制到剪贴板"))
        self.btnSaveAll.setText(_translate("MainWindow", "保存"))
        self.tabWidgetResult.setTabText(self.tabWidgetResult.indexOf(self.tab_2), _translate("MainWindow", "文本"))
