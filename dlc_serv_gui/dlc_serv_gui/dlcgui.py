# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/media/aleksejs/DataHDD/work/codes/image-analysis/behavioural/dlc-scripts/dlc_serv_gui/dlc_serv_gui/dlcgui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlcgui(object):
    def setupUi(self, dlcgui):
        dlcgui.setObjectName("dlcgui")
        dlcgui.resize(980, 939)
        self.centralWidget = QtWidgets.QWidget(dlcgui)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.mainTabWidget = QtWidgets.QTabWidget(self.splitter)
        self.mainTabWidget.setObjectName("mainTabWidget")
        self.markTab = QtWidgets.QWidget()
        self.markTab.setObjectName("markTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.markTab)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.markTabWidget = QtWidgets.QTabWidget(self.markTab)
        self.markTabWidget.setObjectName("markTabWidget")
        self.markPathsTab = QtWidgets.QWidget()
        self.markPathsTab.setObjectName("markPathsTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.markPathsTab)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pathsNetworkVideoLineEdit = QtWidgets.QLineEdit(self.markPathsTab)
        self.pathsNetworkVideoLineEdit.setObjectName("pathsNetworkVideoLineEdit")
        self.gridLayout_3.addWidget(self.pathsNetworkVideoLineEdit, 2, 1, 1, 1)
        self.pathsLocalLineEdit = QtWidgets.QLineEdit(self.markPathsTab)
        self.pathsLocalLineEdit.setObjectName("pathsLocalLineEdit")
        self.gridLayout_3.addWidget(self.pathsLocalLineEdit, 1, 1, 1, 1)
        self.pathsImportLineEdit = QtWidgets.QLineEdit(self.markPathsTab)
        self.pathsImportLineEdit.setObjectName("pathsImportLineEdit")
        self.gridLayout_3.addWidget(self.pathsImportLineEdit, 4, 1, 1, 1)
        self.pathsImportButton = QtWidgets.QPushButton(self.markPathsTab)
        self.pathsImportButton.setObjectName("pathsImportButton")
        self.gridLayout_3.addWidget(self.pathsImportButton, 4, 2, 1, 1)
        self.pathsLocalLabel = QtWidgets.QLabel(self.markPathsTab)
        self.pathsLocalLabel.setObjectName("pathsLocalLabel")
        self.gridLayout_3.addWidget(self.pathsLocalLabel, 1, 0, 1, 1)
        self.pathsLocalButton = QtWidgets.QPushButton(self.markPathsTab)
        self.pathsLocalButton.setObjectName("pathsLocalButton")
        self.gridLayout_3.addWidget(self.pathsLocalButton, 1, 2, 1, 1)
        self.pathsNetworkVideoLabel = QtWidgets.QLabel(self.markPathsTab)
        self.pathsNetworkVideoLabel.setObjectName("pathsNetworkVideoLabel")
        self.gridLayout_3.addWidget(self.pathsNetworkVideoLabel, 2, 0, 1, 1)
        self.pathsNetworkVideoButton = QtWidgets.QPushButton(self.markPathsTab)
        self.pathsNetworkVideoButton.setObjectName("pathsNetworkVideoButton")
        self.gridLayout_3.addWidget(self.pathsNetworkVideoButton, 2, 2, 1, 1)
        self.pathsImportLabel = QtWidgets.QLabel(self.markPathsTab)
        self.pathsImportLabel.setObjectName("pathsImportLabel")
        self.gridLayout_3.addWidget(self.pathsImportLabel, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.pathsImportPathsButton = QtWidgets.QPushButton(self.markPathsTab)
        self.pathsImportPathsButton.setObjectName("pathsImportPathsButton")
        self.verticalLayout.addWidget(self.pathsImportPathsButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.markTabWidget.addTab(self.markPathsTab, "")
        self.markParamsTab = QtWidgets.QWidget()
        self.markParamsTab.setObjectName("markParamsTab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.markParamsTab)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.paramSelectionLabel = QtWidgets.QLabel(self.markParamsTab)
        self.paramSelectionLabel.setObjectName("paramSelectionLabel")
        self.gridLayout_2.addWidget(self.paramSelectionLabel, 4, 0, 1, 1)
        self.paramSelectionComboBox = QtWidgets.QComboBox(self.markParamsTab)
        self.paramSelectionComboBox.setObjectName("paramSelectionComboBox")
        self.paramSelectionComboBox.addItem("")
        self.paramSelectionComboBox.addItem("")
        self.gridLayout_2.addWidget(self.paramSelectionComboBox, 4, 1, 1, 1)
        self.paramNameLabel = QtWidgets.QLabel(self.markParamsTab)
        self.paramNameLabel.setObjectName("paramNameLabel")
        self.gridLayout_2.addWidget(self.paramNameLabel, 1, 0, 1, 1)
        self.paramDataLabel = QtWidgets.QLabel(self.markParamsTab)
        self.paramDataLabel.setObjectName("paramDataLabel")
        self.gridLayout_2.addWidget(self.paramDataLabel, 2, 0, 1, 1)
        self.paramNameLineEdit = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramNameLineEdit.setObjectName("paramNameLineEdit")
        self.gridLayout_2.addWidget(self.paramNameLineEdit, 1, 1, 1, 1)
        self.paramDateLineEdit = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramDateLineEdit.setObjectName("paramDateLineEdit")
        self.gridLayout_2.addWidget(self.paramDateLineEdit, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.paramCropMarginsXMin = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramCropMarginsXMin.setReadOnly(True)
        self.paramCropMarginsXMin.setObjectName("paramCropMarginsXMin")
        self.horizontalLayout.addWidget(self.paramCropMarginsXMin)
        self.paramCropMarginsXMax = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramCropMarginsXMax.setReadOnly(True)
        self.paramCropMarginsXMax.setObjectName("paramCropMarginsXMax")
        self.horizontalLayout.addWidget(self.paramCropMarginsXMax)
        self.paramCropMarginsYMin = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramCropMarginsYMin.setReadOnly(True)
        self.paramCropMarginsYMin.setObjectName("paramCropMarginsYMin")
        self.horizontalLayout.addWidget(self.paramCropMarginsYMin)
        self.paramCropMarginsYMax = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramCropMarginsYMax.setReadOnly(True)
        self.paramCropMarginsYMax.setObjectName("paramCropMarginsYMax")
        self.horizontalLayout.addWidget(self.paramCropMarginsYMax)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 1, 1, 1)
        self.paramNumFrameLabel = QtWidgets.QLabel(self.markParamsTab)
        self.paramNumFrameLabel.setObjectName("paramNumFrameLabel")
        self.gridLayout_2.addWidget(self.paramNumFrameLabel, 3, 0, 1, 1)
        self.paramNumFrameLineEdit = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramNumFrameLineEdit.setObjectName("paramNumFrameLineEdit")
        self.gridLayout_2.addWidget(self.paramNumFrameLineEdit, 3, 1, 1, 1)
        self.paramCroppingCheckBox = QtWidgets.QCheckBox(self.markParamsTab)
        self.paramCroppingCheckBox.setObjectName("paramCroppingCheckBox")
        self.gridLayout_2.addWidget(self.paramCroppingCheckBox, 5, 0, 1, 1)
        self.paramMarkingsLabel = QtWidgets.QLabel(self.markParamsTab)
        self.paramMarkingsLabel.setObjectName("paramMarkingsLabel")
        self.gridLayout_2.addWidget(self.paramMarkingsLabel, 7, 0, 1, 1)
        self.paramMarkingsLineEdit = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramMarkingsLineEdit.setObjectName("paramMarkingsLineEdit")
        self.gridLayout_2.addWidget(self.paramMarkingsLineEdit, 7, 1, 1, 1)
        self.paramMarginsLabel = QtWidgets.QLabel(self.markParamsTab)
        self.paramMarginsLabel.setObjectName("paramMarginsLabel")
        self.gridLayout_2.addWidget(self.paramMarginsLabel, 6, 0, 1, 1)
        self.paramProjectNameLabel = QtWidgets.QLabel(self.markParamsTab)
        self.paramProjectNameLabel.setObjectName("paramProjectNameLabel")
        self.gridLayout_2.addWidget(self.paramProjectNameLabel, 0, 0, 1, 1)
        self.paramProjectNameLineEdit = QtWidgets.QLineEdit(self.markParamsTab)
        self.paramProjectNameLineEdit.setObjectName("paramProjectNameLineEdit")
        self.gridLayout_2.addWidget(self.paramProjectNameLineEdit, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(50, 11, 11, 11)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.paramSampleImagesButton = QtWidgets.QPushButton(self.markParamsTab)
        self.paramSampleImagesButton.setObjectName("paramSampleImagesButton")
        self.verticalLayout_4.addWidget(self.paramSampleImagesButton)
        self.paramGuiMarkButton = QtWidgets.QPushButton(self.markParamsTab)
        self.paramGuiMarkButton.setObjectName("paramGuiMarkButton")
        self.verticalLayout_4.addWidget(self.paramGuiMarkButton)
        self.paramCreateTrainingSetButton = QtWidgets.QPushButton(self.markParamsTab)
        self.paramCreateTrainingSetButton.setObjectName("paramCreateTrainingSetButton")
        self.verticalLayout_4.addWidget(self.paramCreateTrainingSetButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.markTabWidget.addTab(self.markParamsTab, "")
        self.markCheckTab = QtWidgets.QWidget()
        self.markCheckTab.setObjectName("markCheckTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.markCheckTab)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkGraphicsView = QtWidgets.QGraphicsView(self.markCheckTab)
        self.checkGraphicsView.setObjectName("checkGraphicsView")
        self.verticalLayout_3.addWidget(self.checkGraphicsView)
        self.checkFrameSlider = QtWidgets.QSlider(self.markCheckTab)
        self.checkFrameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.checkFrameSlider.setObjectName("checkFrameSlider")
        self.verticalLayout_3.addWidget(self.checkFrameSlider)
        self.markTabWidget.addTab(self.markCheckTab, "")
        self.verticalLayout_7.addWidget(self.markTabWidget)
        self.mainTabWidget.addTab(self.markTab, "")
        self.trainTab = QtWidgets.QWidget()
        self.trainTab.setObjectName("trainTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.trainTab)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.trainTabWidget = QtWidgets.QTabWidget(self.trainTab)
        self.trainTabWidget.setObjectName("trainTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.connectConnectButton = QtWidgets.QPushButton(self.tab)
        self.connectConnectButton.setObjectName("connectConnectButton")
        self.gridLayout_5.addWidget(self.connectConnectButton, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.connectUsernameLabel = QtWidgets.QLabel(self.tab)
        self.connectUsernameLabel.setObjectName("connectUsernameLabel")
        self.gridLayout_6.addWidget(self.connectUsernameLabel, 1, 0, 1, 1)
        self.connectHostnameLabel = QtWidgets.QLabel(self.tab)
        self.connectHostnameLabel.setObjectName("connectHostnameLabel")
        self.gridLayout_6.addWidget(self.connectHostnameLabel, 0, 0, 1, 1)
        self.connectUsernameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.connectUsernameLineEdit.setObjectName("connectUsernameLineEdit")
        self.gridLayout_6.addWidget(self.connectUsernameLineEdit, 1, 1, 1, 1)
        self.connectPasswordLabel = QtWidgets.QLabel(self.tab)
        self.connectPasswordLabel.setObjectName("connectPasswordLabel")
        self.gridLayout_6.addWidget(self.connectPasswordLabel, 2, 0, 1, 1)
        self.connectHostnameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.connectHostnameLineEdit.setObjectName("connectHostnameLineEdit")
        self.gridLayout_6.addWidget(self.connectHostnameLineEdit, 0, 1, 1, 1)
        self.connectPasswordLineEdit = QtWidgets.QLineEdit(self.tab)
        self.connectPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.connectPasswordLineEdit.setObjectName("connectPasswordLineEdit")
        self.gridLayout_6.addWidget(self.connectPasswordLineEdit, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 2, 0, 1, 1)
        self.trainTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.trainTabWidget.addTab(self.tab_2, "")
        self.gridLayout_4.addWidget(self.trainTabWidget, 0, 0, 1, 1)
        self.mainTabWidget.addTab(self.trainTab, "")
        self.processTab = QtWidgets.QWidget()
        self.processTab.setObjectName("processTab")
        self.mainTabWidget.addTab(self.processTab, "")
        self.postprocessTab = QtWidgets.QWidget()
        self.postprocessTab.setObjectName("postprocessTab")
        self.mainTabWidget.addTab(self.postprocessTab, "")
        self.logTextEdit = QtWidgets.QTextEdit(self.splitter)
        self.logTextEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier 10 Pitch")
        font.setPointSize(7)
        self.logTextEdit.setFont(font)
        self.logTextEdit.setMouseTracking(True)
        self.logTextEdit.setReadOnly(True)
        self.logTextEdit.setObjectName("logTextEdit")
        self.verticalLayout_2.addWidget(self.splitter)
        dlcgui.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(dlcgui)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 980, 29))
        self.menuBar.setObjectName("menuBar")
        dlcgui.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(dlcgui)
        self.mainToolBar.setObjectName("mainToolBar")
        dlcgui.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(dlcgui)
        self.statusBar.setObjectName("statusBar")
        dlcgui.setStatusBar(self.statusBar)

        self.retranslateUi(dlcgui)
        self.mainTabWidget.setCurrentIndex(0)
        self.markTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(dlcgui)
        dlcgui.setTabOrder(self.mainTabWidget, self.pathsLocalLineEdit)
        dlcgui.setTabOrder(self.pathsLocalLineEdit, self.pathsLocalButton)
        dlcgui.setTabOrder(self.pathsLocalButton, self.pathsNetworkVideoLineEdit)
        dlcgui.setTabOrder(self.pathsNetworkVideoLineEdit, self.pathsNetworkVideoButton)
        dlcgui.setTabOrder(self.pathsNetworkVideoButton, self.pathsImportLineEdit)
        dlcgui.setTabOrder(self.pathsImportLineEdit, self.pathsImportButton)
        dlcgui.setTabOrder(self.pathsImportButton, self.pathsImportPathsButton)
        dlcgui.setTabOrder(self.pathsImportPathsButton, self.logTextEdit)
        dlcgui.setTabOrder(self.logTextEdit, self.paramNameLineEdit)
        dlcgui.setTabOrder(self.paramNameLineEdit, self.paramDateLineEdit)
        dlcgui.setTabOrder(self.paramDateLineEdit, self.paramNumFrameLineEdit)
        dlcgui.setTabOrder(self.paramNumFrameLineEdit, self.paramSelectionComboBox)
        dlcgui.setTabOrder(self.paramSelectionComboBox, self.paramCroppingCheckBox)
        dlcgui.setTabOrder(self.paramCroppingCheckBox, self.paramSampleImagesButton)
        dlcgui.setTabOrder(self.paramSampleImagesButton, self.paramGuiMarkButton)
        dlcgui.setTabOrder(self.paramGuiMarkButton, self.paramCreateTrainingSetButton)
        dlcgui.setTabOrder(self.paramCreateTrainingSetButton, self.checkGraphicsView)
        dlcgui.setTabOrder(self.checkGraphicsView, self.checkFrameSlider)
        dlcgui.setTabOrder(self.checkFrameSlider, self.trainTabWidget)
        dlcgui.setTabOrder(self.trainTabWidget, self.connectHostnameLineEdit)
        dlcgui.setTabOrder(self.connectHostnameLineEdit, self.connectUsernameLineEdit)
        dlcgui.setTabOrder(self.connectUsernameLineEdit, self.connectPasswordLineEdit)
        dlcgui.setTabOrder(self.connectPasswordLineEdit, self.connectConnectButton)
        dlcgui.setTabOrder(self.connectConnectButton, self.paramCropMarginsXMin)
        dlcgui.setTabOrder(self.paramCropMarginsXMin, self.paramCropMarginsXMax)
        dlcgui.setTabOrder(self.paramCropMarginsXMax, self.paramCropMarginsYMin)
        dlcgui.setTabOrder(self.paramCropMarginsYMin, self.paramCropMarginsYMax)
        dlcgui.setTabOrder(self.paramCropMarginsYMax, self.paramMarkingsLineEdit)

    def retranslateUi(self, dlcgui):
        _translate = QtCore.QCoreApplication.translate
        dlcgui.setWindowTitle(_translate("dlcgui", "dlcgui"))
        self.pathsImportButton.setText(_translate("dlcgui", "Open"))
        self.pathsLocalLabel.setText(_translate("dlcgui", "Local project folder"))
        self.pathsLocalButton.setText(_translate("dlcgui", "Open"))
        self.pathsNetworkVideoLabel.setText(_translate("dlcgui", "Video folder"))
        self.pathsNetworkVideoButton.setText(_translate("dlcgui", "Open"))
        self.pathsImportLabel.setText(_translate("dlcgui", "Import project folder"))
        self.pathsImportPathsButton.setText(_translate("dlcgui", "Import paths"))
        self.markTabWidget.setTabText(self.markTabWidget.indexOf(self.markPathsTab), _translate("dlcgui", "paths"))
        self.paramSelectionLabel.setText(_translate("dlcgui", "Selection"))
        self.paramSelectionComboBox.setItemText(0, _translate("dlcgui", "uniform"))
        self.paramSelectionComboBox.setItemText(1, _translate("dlcgui", "k-means"))
        self.paramNameLabel.setText(_translate("dlcgui", "Marker Name"))
        self.paramDataLabel.setText(_translate("dlcgui", "Date"))
        self.paramCropMarginsXMin.setText(_translate("dlcgui", "0"))
        self.paramCropMarginsXMax.setText(_translate("dlcgui", "0"))
        self.paramCropMarginsYMin.setText(_translate("dlcgui", "0"))
        self.paramCropMarginsYMax.setText(_translate("dlcgui", "0"))
        self.paramNumFrameLabel.setText(_translate("dlcgui", "Num Frames"))
        self.paramCroppingCheckBox.setText(_translate("dlcgui", "Cropping?"))
        self.paramMarkingsLabel.setText(_translate("dlcgui", "Markings"))
        self.paramMarginsLabel.setText(_translate("dlcgui", "Crop margins"))
        self.paramProjectNameLabel.setText(_translate("dlcgui", "Project name"))
        self.paramProjectNameLineEdit.setText(_translate("dlcgui", "TrackingMyCatWhyNot14_43"))
        self.paramSampleImagesButton.setText(_translate("dlcgui", "Sample Images"))
        self.paramGuiMarkButton.setText(_translate("dlcgui", "GUI: Mark"))
        self.paramCreateTrainingSetButton.setText(_translate("dlcgui", "Create Training Set"))
        self.markTabWidget.setTabText(self.markTabWidget.indexOf(self.markParamsTab), _translate("dlcgui", "params"))
        self.markTabWidget.setTabText(self.markTabWidget.indexOf(self.markCheckTab), _translate("dlcgui", "check"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.markTab), _translate("dlcgui", "mark"))
        self.connectConnectButton.setText(_translate("dlcgui", "Connect"))
        self.connectUsernameLabel.setText(_translate("dlcgui", "username"))
        self.connectHostnameLabel.setText(_translate("dlcgui", "hostname"))
        self.connectPasswordLabel.setText(_translate("dlcgui", "password"))
        self.trainTabWidget.setTabText(self.trainTabWidget.indexOf(self.tab), _translate("dlcgui", "connect"))
        self.trainTabWidget.setTabText(self.trainTabWidget.indexOf(self.tab_2), _translate("dlcgui", "Tab 2"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.trainTab), _translate("dlcgui", "train"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.processTab), _translate("dlcgui", "process"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.postprocessTab), _translate("dlcgui", "postprocess"))
        self.logTextEdit.setHtml(_translate("dlcgui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier 10 Pitch\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier\'; font-size:11pt;\"><br /></p></body></html>"))
