# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 860)
        MainWindow.setMinimumSize(QtCore.QSize(1260, 860))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(255, 255, 37, 255), stop:0.0795455 rgba(255, 212, 0, 255), stop:0.147727 rgba(241, 194, 0, 255), stop:0.238636 rgba(232, 187, 48, 255), stop:0.301136 rgba(243, 164, 97, 255), stop:0.636364 rgba(81, 135, 255, 255), stop:1 rgba(14, 95, 230, 255))")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    border-radius: 5;\n"
"    background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab::hover{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border: 3px solid #000000;\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"    background-color: rgb(255, 170, 0);\n"
"    border: 3px solid #000000;\n"
"    width: 100px;\n"
"    border-radius: 2px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    padding: 6px 0px;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(80, 80))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(230, 120, 271, 81))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 170, 0);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #000000;\n"
"font: 75 18pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 18pt \"Comic Sans MS\";\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.tab_4)
        self.progressBar.setGeometry(QtCore.QRect(250, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color:rgb(224, 250, 255);\n"
"color:rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-radius:10px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.397727 rgba(255, 90, 90, 255), stop:1 rgba(230, 255, 0, 255));\n"
"}\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.layoutWidget = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget.setGeometry(QtCore.QRect(-1, 0, 1241, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(1050, 540, 221, 171))
        self.label_4.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("descargar.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(1090, 440, 141, 111))
        self.label_5.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Mi proyecto.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 120, 181, 71))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 170, 0);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #000000;\n"
"font: 75 18pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 18pt \"Comic Sans MS\";\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.total = QtWidgets.QLabel(self.tab_4)
        self.total.setGeometry(QtCore.QRect(660, 330, 41, 33))
        self.total.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 170, 0);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #000000;\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"}")
        self.total.setAlignment(QtCore.Qt.AlignCenter)
        self.total.setObjectName("total")
        self.corriente = QtWidgets.QLabel(self.tab_4)
        self.corriente.setGeometry(QtCore.QRect(490, 380, 41, 33))
        self.corriente.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 170, 0);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #000000;\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"}")
        self.corriente.setAlignment(QtCore.Qt.AlignCenter)
        self.corriente.setObjectName("corriente")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(300, 380, 181, 33))
        self.label_6.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(300, 330, 351, 33))
        self.label_9.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(720, 330, 241, 33))
        self.label_10.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(540, 380, 371, 33))
        self.label_11.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(350, 430, 501, 33))
        self.label_12.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(350, 490, 571, 33))
        self.label_17.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_17.setObjectName("label_17")
        self.vibla = QtWidgets.QLabel(self.tab_4)
        self.vibla.setGeometry(QtCore.QRect(300, 430, 41, 33))
        self.vibla.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 170, 0);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #000000;\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"}")
        self.vibla.setAlignment(QtCore.Qt.AlignCenter)
        self.vibla.setObjectName("vibla")
        self.vibll = QtWidgets.QLabel(self.tab_4)
        self.vibll.setGeometry(QtCore.QRect(300, 490, 41, 33))
        self.vibll.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 170, 0);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-width: 2px;\n"
"border-style: solid;\n"
"border-color: #000000;\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"}")
        self.vibll.setAlignment(QtCore.Qt.AlignCenter)
        self.vibll.setObjectName("vibll")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../GUI/5238556.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(200, 40, 831, 211))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(200, 270, 831, 211))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(200, 500, 831, 211))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(1050, 540, 221, 171))
        self.label_13.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("descargar.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(1090, 440, 141, 111))
        self.label_14.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Mi proyecto.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(-10, -6, 1251, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../GUI/1664200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(200, 40, 831, 211))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(200, 270, 831, 211))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(200, 500, 831, 211))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(1, 1, 1241, 35))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(1090, 440, 141, 111))
        self.label_15.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("Mi proyecto.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(1050, 540, 221, 171))
        self.label_16.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("descargar.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../GUI/2018905.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(200, 40, 831, 211))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(200, 270, 831, 211))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(200, 500, 831, 211))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(-4, 1, 1241, 35))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.label_39 = QtWidgets.QLabel(self.tab_3)
        self.label_39.setGeometry(QtCore.QRect(1050, 540, 221, 171))
        self.label_39.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_39.setText("")
        self.label_39.setPixmap(QtGui.QPixmap("descargar.png"))
        self.label_39.setScaledContents(True)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.tab_3)
        self.label_40.setGeometry(QtCore.QRect(1090, 440, 141, 111))
        self.label_40.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 0), stop:0.35 rgba(255, 255, 255, 0), stop:0.4 rgba(255, 255, 255, 0), stop:0.425 rgba(255, 255, 255, 0), stop:0.44 rgba(252, 252, 252, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_40.setText("")
        self.label_40.setPixmap(QtGui.QPixmap("Mi proyecto.png"))
        self.label_40.setScaledContents(True)
        self.label_40.setObjectName("label_40")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../GUI/2018982.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detector de Anomalías"))
        self.pushButton.setText(_translate("MainWindow", "Realizar pronóstico"))
        self.label_8.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">Información Adicional</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Detalles"))
        self.total.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.corriente.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">de los cuales </span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">Se detectaron un total de </span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">puntos anómalos,</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">son de corriente eléctrica,</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">de la vibración del lado del acople, y</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">de la vibración del lado libre de la bomba.</span></p></body></html>"))
        self.vibla.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.vibll.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">Señales entrantes</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">Pronóstico</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#000000;\">Detección de Anomalías</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

