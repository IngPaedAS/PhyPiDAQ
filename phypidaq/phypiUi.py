# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phypi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhyPiWindow(object):
    def setupUi(self, PhyPiWindow):
        PhyPiWindow.setObjectName("PhyPiWindow")
        PhyPiWindow.resize(705, 590)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PhyPiWindow.sizePolicy().hasHeightForWidth())
        PhyPiWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(PhyPiWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_Main = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_Main.setGeometry(QtCore.QRect(-1, 0, 711, 591))
        self.tab_Main.setStatusTip("")
        self.tab_Main.setObjectName("tab_Main")
        self.Tab_Control = QtWidgets.QWidget()
        self.Tab_Control.setWhatsThis("")
        self.Tab_Control.setObjectName("Tab_Control")
        self.label_Picture = QtWidgets.QLabel(self.Tab_Control)
        self.label_Picture.setGeometry(QtCore.QRect(160, 250, 90, 70))
        self.label_Picture.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_Picture.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_Picture.setText("")
        self.label_Picture.setPixmap(QtGui.QPixmap("images/PhiPiLogo.png"))
        self.label_Picture.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Picture.setObjectName("label_Picture")
        self.label_caption = QtWidgets.QLabel(self.Tab_Control)
        self.label_caption.setGeometry(QtCore.QRect(230, 220, 391, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_caption.setFont(font)
        self.label_caption.setObjectName("label_caption")
        self.label_DAQconfig = QtWidgets.QLabel(self.Tab_Control)
        self.label_DAQconfig.setGeometry(QtCore.QRect(60, 426, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label_DAQconfig.setFont(font)
        self.label_DAQconfig.setTextFormat(QtCore.Qt.PlainText)
        self.label_DAQconfig.setObjectName("label_DAQconfig")
        self.lE_DAQConfFile = QtWidgets.QLineEdit(self.Tab_Control)
        self.lE_DAQConfFile.setGeometry(QtCore.QRect(160, 430, 371, 32))
        self.lE_DAQConfFile.setText("")
        self.lE_DAQConfFile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lE_DAQConfFile.setReadOnly(True)
        self.lE_DAQConfFile.setObjectName("lE_DAQConfFile")
        self.pB_StartRun = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_StartRun.setGeometry(QtCore.QRect(599, 517, 101, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/start.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_StartRun.setIcon(icon)
        self.pB_StartRun.setIconSize(QtCore.QSize(24, 24))
        self.pB_StartRun.setObjectName("pB_StartRun")
        self.pB_FileSelect = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_FileSelect.setGeometry(QtCore.QRect(540, 430, 31, 34))
        self.pB_FileSelect.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/open-folder.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_FileSelect.setIcon(icon1)
        self.pB_FileSelect.setObjectName("pB_FileSelect")
        self.pB_abort = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_abort.setGeometry(QtCore.QRect(660, 0, 41, 41))
        self.pB_abort.setAccessibleDescription("")
        self.pB_abort.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/application-exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_abort.setIcon(icon2)
        self.pB_abort.setIconSize(QtCore.QSize(20, 20))
        self.pB_abort.setAutoDefault(False)
        self.pB_abort.setObjectName("pB_abort")
        self.lE_WorkDir = QtWidgets.QLineEdit(self.Tab_Control)
        self.lE_WorkDir.setGeometry(QtCore.QRect(160, 380, 371, 32))
        self.lE_WorkDir.setReadOnly(True)
        self.lE_WorkDir.setObjectName("lE_WorkDir")
        self.label_WorkDir = QtWidgets.QLabel(self.Tab_Control)
        self.label_WorkDir.setGeometry(QtCore.QRect(76, 386, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label_WorkDir.setFont(font)
        self.label_WorkDir.setObjectName("label_WorkDir")
        self.pB_WDselect = QtWidgets.QPushButton(self.Tab_Control)
        self.pB_WDselect.setGeometry(QtCore.QRect(540, 380, 31, 34))
        self.pB_WDselect.setText("")
        self.pB_WDselect.setIcon(icon1)
        self.pB_WDselect.setObjectName("pB_WDselect")
        self.label_2 = QtWidgets.QLabel(self.Tab_Control)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 551, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/PhyPiDAQdiagram.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Tab_Control)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(11, 475, 681, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Picture.raise_()
        self.label_caption.raise_()
        self.label_DAQconfig.raise_()
        self.lE_DAQConfFile.raise_()
        self.pB_StartRun.raise_()
        self.pB_FileSelect.raise_()
        self.lE_WorkDir.raise_()
        self.label_WorkDir.raise_()
        self.pB_WDselect.raise_()
        self.label_2.raise_()
        self.pB_abort.raise_()
        self.verticalLayoutWidget.raise_()
        self.tab_Main.addTab(self.Tab_Control, "")
        self.Tab_Config = QtWidgets.QWidget()
        self.Tab_Config.setObjectName("Tab_Config")
        self.tabConfig = QtWidgets.QTabWidget(self.Tab_Config)
        self.tabConfig.setEnabled(True)
        self.tabConfig.setGeometry(QtCore.QRect(10, 10, 821, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabConfig.sizePolicy().hasHeightForWidth())
        self.tabConfig.setSizePolicy(sizePolicy)
        self.tabConfig.setMinimumSize(QtCore.QSize(811, 0))
        self.tabConfig.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabConfig.setObjectName("tabConfig")
        self.tab_phypiConfig = QtWidgets.QWidget()
        self.tab_phypiConfig.setEnabled(True)
        self.tab_phypiConfig.setObjectName("tab_phypiConfig")
        self.pTE_phypiConfig = QtWidgets.QPlainTextEdit(self.tab_phypiConfig)
        self.pTE_phypiConfig.setGeometry(QtCore.QRect(0, 10, 681, 431))
        self.pTE_phypiConfig.setReadOnly(True)
        self.pTE_phypiConfig.setObjectName("pTE_phypiConfig")
        self.pB_reloadConfig = QtWidgets.QPushButton(self.tab_phypiConfig)
        self.pB_reloadConfig.setEnabled(False)
        self.pB_reloadConfig.setGeometry(QtCore.QRect(500, 440, 171, 21))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_reloadConfig.setIcon(icon3)
        self.pB_reloadConfig.setCheckable(False)
        self.pB_reloadConfig.setChecked(False)
        self.pB_reloadConfig.setAutoDefault(False)
        self.pB_reloadConfig.setObjectName("pB_reloadConfig")
        self.tabConfig.addTab(self.tab_phypiConfig, "")
        self.tab_DeviceConfig0 = QtWidgets.QWidget()
        self.tab_DeviceConfig0.setObjectName("tab_DeviceConfig0")
        self.pTE_DeviceConfig0 = QtWidgets.QPlainTextEdit(self.tab_DeviceConfig0)
        self.pTE_DeviceConfig0.setGeometry(QtCore.QRect(0, 10, 681, 411))
        self.pTE_DeviceConfig0.setReadOnly(True)
        self.pTE_DeviceConfig0.setObjectName("pTE_DeviceConfig0")
        self.pB_DeviceSelect0 = QtWidgets.QPushButton(self.tab_DeviceConfig0)
        self.pB_DeviceSelect0.setGeometry(QtCore.QRect(490, 423, 181, 34))
        self.pB_DeviceSelect0.setIcon(icon1)
        self.pB_DeviceSelect0.setObjectName("pB_DeviceSelect0")
        self.tabConfig.addTab(self.tab_DeviceConfig0, "")
        self.tab_DeviceConfig1 = QtWidgets.QWidget()
        self.tab_DeviceConfig1.setEnabled(False)
        self.tab_DeviceConfig1.setObjectName("tab_DeviceConfig1")
        self.pTE_DeviceConfig1 = QtWidgets.QPlainTextEdit(self.tab_DeviceConfig1)
        self.pTE_DeviceConfig1.setGeometry(QtCore.QRect(0, 0, 681, 421))
        self.pTE_DeviceConfig1.setReadOnly(True)
        self.pTE_DeviceConfig1.setObjectName("pTE_DeviceConfig1")
        self.pB_DeviceSelect1 = QtWidgets.QPushButton(self.tab_DeviceConfig1)
        self.pB_DeviceSelect1.setGeometry(QtCore.QRect(490, 423, 181, 34))
        self.pB_DeviceSelect1.setIcon(icon1)
        self.pB_DeviceSelect1.setObjectName("pB_DeviceSelect1")
        self.tabConfig.addTab(self.tab_DeviceConfig1, "")
        self.tab_DeviceConfig2 = QtWidgets.QWidget()
        self.tab_DeviceConfig2.setEnabled(False)
        self.tab_DeviceConfig2.setObjectName("tab_DeviceConfig2")
        self.pTE_DeviceConfig2 = QtWidgets.QPlainTextEdit(self.tab_DeviceConfig2)
        self.pTE_DeviceConfig2.setGeometry(QtCore.QRect(0, 0, 681, 421))
        self.pTE_DeviceConfig2.setReadOnly(True)
        self.pTE_DeviceConfig2.setObjectName("pTE_DeviceConfig2")
        self.pB_DeviceSelect2 = QtWidgets.QPushButton(self.tab_DeviceConfig2)
        self.pB_DeviceSelect2.setGeometry(QtCore.QRect(490, 423, 181, 34))
        self.pB_DeviceSelect2.setIcon(icon1)
        self.pB_DeviceSelect2.setObjectName("pB_DeviceSelect2")
        self.tabConfig.addTab(self.tab_DeviceConfig2, "")
        self.rB_EditMode = QtWidgets.QRadioButton(self.Tab_Config)
        self.rB_EditMode.setGeometry(QtCore.QRect(596, 4, 91, 30))
        self.rB_EditMode.setObjectName("rB_EditMode")
        self.tab_Main.addTab(self.Tab_Config, "")
        self.Tab_Help = QtWidgets.QWidget()
        self.Tab_Help.setObjectName("Tab_Help")
        self.TE_Help = QtWidgets.QTextEdit(self.Tab_Help)
        self.TE_Help.setGeometry(QtCore.QRect(10, 30, 691, 481))
        self.TE_Help.setUndoRedoEnabled(False)
        self.TE_Help.setReadOnly(True)
        self.TE_Help.setPlaceholderText("")
        self.TE_Help.setObjectName("TE_Help")
        self.pB_Help = QtWidgets.QPushButton(self.Tab_Help)
        self.pB_Help.setGeometry(QtCore.QRect(10, 0, 88, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/flagUK.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Help.setIcon(icon4)
        self.pB_Help.setObjectName("pB_Help")
        self.pB_Hilfe = QtWidgets.QPushButton(self.Tab_Help)
        self.pB_Hilfe.setGeometry(QtCore.QRect(110, 0, 88, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/flagDE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Hilfe.setIcon(icon5)
        self.pB_Hilfe.setObjectName("pB_Hilfe")
        self.tab_Main.addTab(self.Tab_Help, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 550, 60, 31))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.lE_RunTag = QtWidgets.QLineEdit(self.centralwidget)
        self.lE_RunTag.setGeometry(QtCore.QRect(99, 552, 113, 30))
        self.lE_RunTag.setObjectName("lE_RunTag")
        self.pB_SaveDefault = QtWidgets.QPushButton(self.centralwidget)
        self.pB_SaveDefault.setGeometry(QtCore.QRect(230, 550, 141, 34))
        self.pB_SaveDefault.setObjectName("pB_SaveDefault")
        PhyPiWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PhyPiWindow)
        self.tab_Main.setCurrentIndex(0)
        self.tabConfig.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PhyPiWindow)

    def retranslateUi(self, PhyPiWindow):
        _translate = QtCore.QCoreApplication.translate
        PhyPiWindow.setWindowTitle(_translate("PhyPiWindow", "PhiPiDAQ"))
        self.tab_Main.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Output  / Configuration / Help</p></body></html>"))
        self.Tab_Control.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Control Panel</p></body></html>"))
        self.label_Picture.setToolTip(_translate("PhyPiWindow", "PhyPi Data Aquitision with Raspberry Pi"))
        self.label_caption.setText(_translate("PhyPiWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#0000ff;\">D</span><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">ata </span><span style=\" font-size:16pt; font-weight:600; color:#0000ff;\">A</span><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">c</span><span style=\" font-size:16pt; font-weight:600; color:#0000ff;\">q</span><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">uisition </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">for </span><span style=\" font-size:16pt; font-weight:600; color:#0000ff;\">Phy</span><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">sics </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">with Raspberry </span><span style=\" font-size:16pt; font-weight:600; color:#0000ff;\">Pi</span><span style=\" font-size:16pt; font-weight:600; color:#00007f;\"/></p></body></html>"))
        self.label_DAQconfig.setText(_translate("PhyPiWindow", "DAQ config: "))
        self.lE_DAQConfFile.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>DAQ configuration file (type .daq)</p></body></html>"))
        self.pB_StartRun.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Start Data Acquisition</p></body></html>"))
        self.pB_StartRun.setText(_translate("PhyPiWindow", "  StartRun"))
        self.pB_FileSelect.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>selecd daq configuration file</p></body></html>"))
        self.pB_abort.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Exit PhyPi Gui</p></body></html>"))
        self.label_WorkDir.setText(_translate("PhyPiWindow", "Work Dir: "))
        self.pB_WDselect.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>select working directory (where ouput is stored)</p></body></html>"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Control), _translate("PhyPiWindow", "Control"))
        self.Tab_Config.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Config Panel</p></body></html>"))
        self.tabConfig.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Configuration Files</p></body></html>"))
        self.tab_phypiConfig.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>PhyPi Configuration</p></body></html>"))
        self.pTE_phypiConfig.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Main PhyPi Configuration File</p></body></html>"))
        self.pB_reloadConfig.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>reload device configuation files if names or paths changed</p></body></html>"))
        self.pB_reloadConfig.setText(_translate("PhyPiWindow", "reload device config(s)"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_phypiConfig), _translate("PhyPiWindow", "PhyPi Config"))
        self.tab_DeviceConfig0.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>(1st) Device Configuration</p></body></html>"))
        self.pTE_DeviceConfig0.setToolTip(_translate("PhyPiWindow", "Device Configuration"))
        self.pB_DeviceSelect0.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>load template device configuration</p></body></html>"))
        self.pB_DeviceSelect0.setText(_translate("PhyPiWindow", "   load Device Config"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_DeviceConfig0), _translate("PhyPiWindow", "Device Config"))
        self.tab_DeviceConfig1.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>2nd Device Configuration </p></body></html>"))
        self.pB_DeviceSelect1.setText(_translate("PhyPiWindow", "     load Device Config"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_DeviceConfig1), _translate("PhyPiWindow", "2nd Device"))
        self.pB_DeviceSelect2.setText(_translate("PhyPiWindow", "     load Device Config"))
        self.tabConfig.setTabText(self.tabConfig.indexOf(self.tab_DeviceConfig2), _translate("PhyPiWindow", "3rd Device"))
        self.rB_EditMode.setText(_translate("PhyPiWindow", "Edit Mode"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Config), _translate("PhyPiWindow", "Configuration"))
        self.Tab_Help.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Info &amp; Help</p></body></html>"))
        self.pB_Help.setText(_translate("PhyPiWindow", "English"))
        self.pB_Hilfe.setText(_translate("PhyPiWindow", "Deutsch"))
        self.tab_Main.setTabText(self.tab_Main.indexOf(self.Tab_Help), _translate("PhyPiWindow", "Help / Hilfe"))
        self.label.setWhatsThis(_translate("PhyPiWindow", "<html><head/><body><p>common name</p></body></html>"))
        self.label.setText(_translate("PhyPiWindow", "Name:"))
        self.lE_RunTag.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>Name for the run</p></body></html>"))
        self.lE_RunTag.setText(_translate("PhyPiWindow", "phypi"))
        self.pB_SaveDefault.setToolTip(_translate("PhyPiWindow", "<html><head/><body><p>save all config files</p></body></html>"))
        self.pB_SaveDefault.setText(_translate("PhyPiWindow", "Save Config"))

