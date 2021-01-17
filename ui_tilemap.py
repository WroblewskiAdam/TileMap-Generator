# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tilemap.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mapview import MapView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(744, 588)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.height = QSpinBox(self.frame_4)
        self.height.setObjectName(u"height")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.height.sizePolicy().hasHeightForWidth())
        self.height.setSizePolicy(sizePolicy4)
        self.height.setMinimum(1)
        self.height.setMaximum(999999999)
        self.height.setValue(70)

        self.horizontalLayout_5.addWidget(self.height)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.label_3)

        self.width = QSpinBox(self.frame_4)
        self.width.setObjectName(u"width")
        sizePolicy4.setHeightForWidth(self.width.sizePolicy().hasHeightForWidth())
        self.width.setSizePolicy(sizePolicy4)
        self.width.setMinimum(1)
        self.width.setMaximum(999999999)
        self.width.setValue(70)

        self.horizontalLayout_9.addWidget(self.width)


        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.label_4)

        self.density = QSpinBox(self.frame_4)
        self.density.setObjectName(u"density")
        sizePolicy4.setHeightForWidth(self.density.sizePolicy().hasHeightForWidth())
        self.density.setSizePolicy(sizePolicy4)
        self.density.setMinimum(0)
        self.density.setMaximum(100)
        self.density.setValue(40)

        self.horizontalLayout_10.addWidget(self.density)


        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMouseTracking(True)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.generateButton = QPushButton(self.frame)
        self.generateButton.setObjectName(u"generateButton")
        sizePolicy2.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy2)
        self.generateButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.generateButton)

        self.deleteIslandButton = QPushButton(self.frame)
        self.deleteIslandButton.setObjectName(u"deleteIslandButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.deleteIslandButton.sizePolicy().hasHeightForWidth())
        self.deleteIslandButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.deleteIslandButton)

        self.biomButton = QPushButton(self.frame)
        self.biomButton.setObjectName(u"biomButton")
        sizePolicy5.setHeightForWidth(self.biomButton.sizePolicy().hasHeightForWidth())
        self.biomButton.setSizePolicy(sizePolicy5)
        self.biomButton.setCheckable(False)
        self.biomButton.setChecked(False)
        self.biomButton.setAutoRepeat(False)
        self.biomButton.setAutoExclusive(False)
        self.biomButton.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.biomButton)

        self.deleteBiomButton = QPushButton(self.frame)
        self.deleteBiomButton.setObjectName(u"deleteBiomButton")
        sizePolicy5.setHeightForWidth(self.deleteBiomButton.sizePolicy().hasHeightForWidth())
        self.deleteBiomButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.deleteBiomButton)

        self.saveButton = QPushButton(self.frame)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy5.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.saveButton)


        self.verticalLayout_3.addWidget(self.frame)

        self.splitter = QSplitter(self.tab)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Horizontal)
        self.islandList = QListWidget(self.splitter)
        self.islandList.setObjectName(u"islandList")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.islandList.sizePolicy().hasHeightForWidth())
        self.islandList.setSizePolicy(sizePolicy6)
        self.islandList.setMouseTracking(True)
        self.splitter.addWidget(self.islandList)
        self.stack = QStackedWidget(self.splitter)
        self.stack.setObjectName(u"stack")
        sizePolicy1.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy1)
        self.stack.setCursor(QCursor(Qt.ArrowCursor))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label)

        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.islandMap = MapView(self.page_2)
        self.islandMap.setObjectName(u"islandMap")

        self.verticalLayout_2.addWidget(self.islandMap)

        self.stack.addWidget(self.page_2)
        self.splitter.addWidget(self.stack)

        self.verticalLayout_3.addWidget(self.splitter)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.islandInfo = QLabel(self.tab)
        self.islandInfo.setObjectName(u"islandInfo")
        sizePolicy2.setHeightForWidth(self.islandInfo.sizePolicy().hasHeightForWidth())
        self.islandInfo.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.islandInfo)

        self.mapInfo = QLabel(self.tab)
        self.mapInfo.setObjectName(u"mapInfo")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.mapInfo.sizePolicy().hasHeightForWidth())
        self.mapInfo.setSizePolicy(sizePolicy7)

        self.horizontalLayout_12.addWidget(self.mapInfo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_11 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.highlightCheck = QCheckBox(self.tab_2)
        self.highlightCheck.setObjectName(u"highlightCheck")

        self.verticalLayout_8.addWidget(self.highlightCheck)

        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.waterRBG1 = QSpinBox(self.frame_3)
        self.waterRBG1.setObjectName(u"waterRBG1")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.waterRBG1.sizePolicy().hasHeightForWidth())
        self.waterRBG1.setSizePolicy(sizePolicy8)
        self.waterRBG1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.waterRBG1.setMaximum(255)
        self.waterRBG1.setValue(10)

        self.horizontalLayout_3.addWidget(self.waterRBG1)

        self.waterRBG2 = QSpinBox(self.frame_3)
        self.waterRBG2.setObjectName(u"waterRBG2")
        sizePolicy8.setHeightForWidth(self.waterRBG2.sizePolicy().hasHeightForWidth())
        self.waterRBG2.setSizePolicy(sizePolicy8)
        self.waterRBG2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.waterRBG2.setMaximum(255)
        self.waterRBG2.setValue(65)

        self.horizontalLayout_3.addWidget(self.waterRBG2)

        self.waterRBG3 = QSpinBox(self.frame_3)
        self.waterRBG3.setObjectName(u"waterRBG3")
        sizePolicy8.setHeightForWidth(self.waterRBG3.sizePolicy().hasHeightForWidth())
        self.waterRBG3.setSizePolicy(sizePolicy8)
        self.waterRBG3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.waterRBG3.setMaximum(255)
        self.waterRBG3.setValue(148)

        self.horizontalLayout_3.addWidget(self.waterRBG3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.islandRBG1 = QSpinBox(self.frame_5)
        self.islandRBG1.setObjectName(u"islandRBG1")
        sizePolicy8.setHeightForWidth(self.islandRBG1.sizePolicy().hasHeightForWidth())
        self.islandRBG1.setSizePolicy(sizePolicy8)
        self.islandRBG1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.islandRBG1.setMaximum(255)
        self.islandRBG1.setValue(10)

        self.horizontalLayout_4.addWidget(self.islandRBG1)

        self.islandRBG2 = QSpinBox(self.frame_5)
        self.islandRBG2.setObjectName(u"islandRBG2")
        sizePolicy8.setHeightForWidth(self.islandRBG2.sizePolicy().hasHeightForWidth())
        self.islandRBG2.setSizePolicy(sizePolicy8)
        self.islandRBG2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.islandRBG2.setMaximum(255)
        self.islandRBG2.setValue(138)

        self.horizontalLayout_4.addWidget(self.islandRBG2)

        self.islandRBG3 = QSpinBox(self.frame_5)
        self.islandRBG3.setObjectName(u"islandRBG3")
        sizePolicy8.setHeightForWidth(self.islandRBG3.sizePolicy().hasHeightForWidth())
        self.islandRBG3.setSizePolicy(sizePolicy8)
        self.islandRBG3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.islandRBG3.setMaximum(255)
        self.islandRBG3.setValue(22)

        self.horizontalLayout_4.addWidget(self.islandRBG3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.tab_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_12)

        self.minIslandSurface = QSpinBox(self.frame_8)
        self.minIslandSurface.setObjectName(u"minIslandSurface")
        self.minIslandSurface.setMinimum(1)
        self.minIslandSurface.setMaximum(999999999)

        self.verticalLayout_15.addWidget(self.minIslandSurface)

        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        sizePolicy7.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy7)
        font = QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_13)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.biomTermFrame = QFrame(self.tab_2)
        self.biomTermFrame.setObjectName(u"biomTermFrame")
        self.biomTermFrame.setFrameShape(QFrame.StyledPanel)
        self.biomTermFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.biomTermFrame)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.biomTermFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_10)

        self.biomTerm = QSpinBox(self.biomTermFrame)
        self.biomTerm.setObjectName(u"biomTerm")
        self.biomTerm.setMinimum(1)
        self.biomTerm.setMaximum(999999999)

        self.verticalLayout_14.addWidget(self.biomTerm)

        self.label_11 = QLabel(self.biomTermFrame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy7.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy7)
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_11)


        self.verticalLayout_16.addLayout(self.verticalLayout_14)


        self.verticalLayout_8.addWidget(self.biomTermFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.horizontalLayout_11.addLayout(self.verticalLayout_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.biomListFrame = QFrame(self.tab_2)
        self.biomListFrame.setObjectName(u"biomListFrame")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.biomListFrame.sizePolicy().hasHeightForWidth())
        self.biomListFrame.setSizePolicy(sizePolicy9)
        self.biomListFrame.setLayoutDirection(Qt.LeftToRight)
        self.biomListFrame.setFrameShape(QFrame.NoFrame)
        self.biomListFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.biomListFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.biomListLabel = QLabel(self.biomListFrame)
        self.biomListLabel.setObjectName(u"biomListLabel")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.biomListLabel.sizePolicy().hasHeightForWidth())
        self.biomListLabel.setSizePolicy(sizePolicy10)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        self.biomListLabel.setFont(font1)
        self.biomListLabel.setFrameShape(QFrame.NoFrame)
        self.biomListLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.biomListLabel)

        self.biomList = QListWidget(self.biomListFrame)
        self.biomList.setObjectName(u"biomList")
        sizePolicy11 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.biomList.sizePolicy().hasHeightForWidth())
        self.biomList.setSizePolicy(sizePolicy11)
        self.biomList.setStyleSheet(u"")
        self.biomList.setMovement(QListView.Static)
        self.biomList.setResizeMode(QListView.Fixed)

        self.verticalLayout_12.addWidget(self.biomList)

        self.frame_6 = QFrame(self.biomListFrame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy12 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy12)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.biomRBG1 = QSpinBox(self.frame_6)
        self.biomRBG1.setObjectName(u"biomRBG1")
        sizePolicy8.setHeightForWidth(self.biomRBG1.sizePolicy().hasHeightForWidth())
        self.biomRBG1.setSizePolicy(sizePolicy8)
        self.biomRBG1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.biomRBG1.setMaximum(255)
        self.biomRBG1.setValue(0)

        self.horizontalLayout_6.addWidget(self.biomRBG1)

        self.biomRBG2 = QSpinBox(self.frame_6)
        self.biomRBG2.setObjectName(u"biomRBG2")
        sizePolicy8.setHeightForWidth(self.biomRBG2.sizePolicy().hasHeightForWidth())
        self.biomRBG2.setSizePolicy(sizePolicy8)
        self.biomRBG2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.biomRBG2.setMaximum(255)
        self.biomRBG2.setValue(0)

        self.horizontalLayout_6.addWidget(self.biomRBG2)

        self.biomRBG3 = QSpinBox(self.frame_6)
        self.biomRBG3.setObjectName(u"biomRBG3")
        sizePolicy8.setHeightForWidth(self.biomRBG3.sizePolicy().hasHeightForWidth())
        self.biomRBG3.setSizePolicy(sizePolicy8)
        self.biomRBG3.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.biomRBG3.setMaximum(255)
        self.biomRBG3.setValue(0)

        self.horizontalLayout_6.addWidget(self.biomRBG3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.newBiomNameLabel = QLabel(self.frame_6)
        self.newBiomNameLabel.setObjectName(u"newBiomNameLabel")
        self.newBiomNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.newBiomNameLabel)

        self.newBiomName = QLineEdit(self.frame_6)
        self.newBiomName.setObjectName(u"newBiomName")
        self.newBiomName.setCursor(QCursor(Qt.IBeamCursor))
        self.newBiomName.setMouseTracking(True)
        self.newBiomName.setMaxLength(20)
        self.newBiomName.setAlignment(Qt.AlignCenter)
        self.newBiomName.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.verticalLayout_10.addWidget(self.newBiomName)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.biomSliderRGB1 = QSlider(self.frame_6)
        self.biomSliderRGB1.setObjectName(u"biomSliderRGB1")
        self.biomSliderRGB1.setMaximum(255)
        self.biomSliderRGB1.setOrientation(Qt.Horizontal)
        self.biomSliderRGB1.setInvertedAppearance(False)
        self.biomSliderRGB1.setInvertedControls(False)
        self.biomSliderRGB1.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_11.addWidget(self.biomSliderRGB1)

        self.biomSliderRGB2 = QSlider(self.frame_6)
        self.biomSliderRGB2.setObjectName(u"biomSliderRGB2")
        self.biomSliderRGB2.setMaximum(255)
        self.biomSliderRGB2.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.biomSliderRGB2)

        self.biomSliderRGB3 = QSlider(self.frame_6)
        self.biomSliderRGB3.setObjectName(u"biomSliderRGB3")
        self.biomSliderRGB3.setMaximum(255)
        self.biomSliderRGB3.setOrientation(Qt.Horizontal)

        self.verticalLayout_11.addWidget(self.biomSliderRGB3)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)

        self.addBiomPatternButton = QPushButton(self.frame_6)
        self.addBiomPatternButton.setObjectName(u"addBiomPatternButton")

        self.verticalLayout_13.addWidget(self.addBiomPatternButton)

        self.deleteBiomPatternButton = QPushButton(self.frame_6)
        self.deleteBiomPatternButton.setObjectName(u"deleteBiomPatternButton")

        self.verticalLayout_13.addWidget(self.deleteBiomPatternButton)

        self.changeWaterRGBButton = QPushButton(self.frame_6)
        self.changeWaterRGBButton.setObjectName(u"changeWaterRGBButton")

        self.verticalLayout_13.addWidget(self.changeWaterRGBButton)

        self.changeIslandRGBButton = QPushButton(self.frame_6)
        self.changeIslandRGBButton.setObjectName(u"changeIslandRGBButton")

        self.verticalLayout_13.addWidget(self.changeIslandRGBButton)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.colourDisplay = QGraphicsView(self.biomListFrame)
        self.colourDisplay.setObjectName(u"colourDisplay")
        sizePolicy9.setHeightForWidth(self.colourDisplay.sizePolicy().hasHeightForWidth())
        self.colourDisplay.setSizePolicy(sizePolicy9)
        self.colourDisplay.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.colourDisplay)


        self.horizontalLayout_11.addWidget(self.biomListFrame)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 744, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.generateButton.setDefault(False)
        self.stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tile Map Generator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Height ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Islands density", None))
        self.generateButton.setText(QCoreApplication.translate("MainWindow", u"Generate Map", None))
        self.deleteIslandButton.setText(QCoreApplication.translate("MainWindow", u"Delete Island", None))
        self.biomButton.setText(QCoreApplication.translate("MainWindow", u"Add Bioms", None))
        self.deleteBiomButton.setText(QCoreApplication.translate("MainWindow", u"Delete Bioms", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save Picture", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Generate map first", None))
        self.islandInfo.setText("")
        self.mapInfo.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Generator", None))
        self.highlightCheck.setText(QCoreApplication.translate("MainWindow", u"Highlight Island", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Water RGB code", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Island RGB code", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Minimal island surface", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"if value given here is greater than total islands surface calculated from \"island density\" only one island will apper with surface corresponding to \"islands density\"", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Minimal island surface to apply biom", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"value determines on which islands bioms will be generated", None))
        self.biomListLabel.setText(QCoreApplication.translate("MainWindow", u"Biom List", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RGB code", None))
        self.newBiomNameLabel.setText(QCoreApplication.translate("MainWindow", u"biom name", None))
        self.newBiomName.setInputMask("")
        self.newBiomName.setText("")
        self.newBiomName.setPlaceholderText("")
        self.addBiomPatternButton.setText(QCoreApplication.translate("MainWindow", u"Add new biom pattern", None))
        self.deleteBiomPatternButton.setText(QCoreApplication.translate("MainWindow", u"Delete biom pattern", None))
        self.changeWaterRGBButton.setText(QCoreApplication.translate("MainWindow", u"Change Water RGB Code", None))
        self.changeIslandRGBButton.setText(QCoreApplication.translate("MainWindow", u"Change island RGB Code", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

