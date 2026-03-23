# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 200)
        MainWindow.setMinimumSize(QSize(400, 200))
        self.action_set_tiny = QAction(MainWindow)
        self.action_set_tiny.setObjectName(u"action_set_tiny")
        self.action_set_tiny.setCheckable(True)
        self.action_set_base = QAction(MainWindow)
        self.action_set_base.setObjectName(u"action_set_base")
        self.action_set_base.setCheckable(True)
        self.action_set_base.setChecked(True)
        self.action_set_small = QAction(MainWindow)
        self.action_set_small.setObjectName(u"action_set_small")
        self.action_set_small.setCheckable(True)
        self.action_set_medium = QAction(MainWindow)
        self.action_set_medium.setObjectName(u"action_set_medium")
        self.action_set_medium.setCheckable(True)
        self.action_set_large = QAction(MainWindow)
        self.action_set_large.setObjectName(u"action_set_large")
        self.action_set_large.setCheckable(True)
        self.action_set_turbo = QAction(MainWindow)
        self.action_set_turbo.setObjectName(u"action_set_turbo")
        self.action_set_turbo.setCheckable(True)
        self.actionCredits = QAction(MainWindow)
        self.actionCredits.setObjectName(u"actionCredits")
        self.actionLicenses = QAction(MainWindow)
        self.actionLicenses.setObjectName(u"actionLicenses")
        self.actionShortcuts = QAction(MainWindow)
        self.actionShortcuts.setObjectName(u"actionShortcuts")
        self.actionReset_Preferences = QAction(MainWindow)
        self.actionReset_Preferences.setObjectName(u"actionReset_Preferences")
        self.actionClear_Whisper_Model_Cache = QAction(MainWindow)
        self.actionClear_Whisper_Model_Cache.setObjectName(u"actionClear_Whisper_Model_Cache")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.openMagnify = QPushButton(self.centralwidget)
        self.openMagnify.setObjectName(u"openMagnify")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openMagnify.sizePolicy().hasHeightForWidth())
        self.openMagnify.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setWeight(QFont.DemiBold)
        self.openMagnify.setFont(font)

        self.horizontalLayout.addWidget(self.openMagnify)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.contrast = QPushButton(self.centralwidget)
        self.contrast.setObjectName(u"contrast")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.contrast.sizePolicy().hasHeightForWidth())
        self.contrast.setSizePolicy(sizePolicy1)
        self.contrast.setFont(font)

        self.verticalLayout.addWidget(self.contrast)

        self.transcribe = QPushButton(self.centralwidget)
        self.transcribe.setObjectName(u"transcribe")
        sizePolicy.setHeightForWidth(self.transcribe.sizePolicy().hasHeightForWidth())
        self.transcribe.setSizePolicy(sizePolicy)
        self.transcribe.setFont(font)

        self.verticalLayout.addWidget(self.transcribe)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 600, 33))
        self.menuOptions = QMenu(self.menuBar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuChange_Model = QMenu(self.menuOptions)
        self.menuChange_Model.setObjectName(u"menuChange_Model")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuOptions.addAction(self.menuChange_Model.menuAction())
        self.menuChange_Model.addAction(self.action_set_tiny)
        self.menuChange_Model.addAction(self.action_set_base)
        self.menuChange_Model.addAction(self.action_set_small)
        self.menuChange_Model.addAction(self.action_set_medium)
        self.menuChange_Model.addAction(self.action_set_large)
        self.menuChange_Model.addAction(self.action_set_turbo)
        self.menuHelp.addAction(self.actionShortcuts)
        self.menuHelp.addAction(self.actionLicenses)
        self.menuHelp.addAction(self.actionCredits)
        self.menuHelp.addAction(self.actionClear_Whisper_Model_Cache)
        self.menuHelp.addAction(self.actionReset_Preferences)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_set_tiny.setText(QCoreApplication.translate("MainWindow", u"tiny (fastest/least accurate)", None))
        self.action_set_base.setText(QCoreApplication.translate("MainWindow", u"base", None))
        self.action_set_small.setText(QCoreApplication.translate("MainWindow", u"small", None))
        self.action_set_medium.setText(QCoreApplication.translate("MainWindow", u"medium", None))
        self.action_set_large.setText(QCoreApplication.translate("MainWindow", u"large (slowest/most accurate)", None))
        self.action_set_turbo.setText(QCoreApplication.translate("MainWindow", u"turbo (large but faster)", None))
        self.actionCredits.setText(QCoreApplication.translate("MainWindow", u"Credits...", None))
        self.actionLicenses.setText(QCoreApplication.translate("MainWindow", u"Licenses...", None))
        self.actionShortcuts.setText(QCoreApplication.translate("MainWindow", u"Guide...", None))
        self.actionReset_Preferences.setText(QCoreApplication.translate("MainWindow", u"Reset Preferences...", None))
        self.actionClear_Whisper_Model_Cache.setText(QCoreApplication.translate("MainWindow", u"Clear Whisper Model Cache", None))
#if QT_CONFIG(tooltip)
        self.openMagnify.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Opens a menu that allows you to magnify the screen.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.openMagnify.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Magnifies the screen.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.openMagnify.setText(QCoreApplication.translate("MainWindow", u"Open Magnification Menu...", None))
        self.contrast.setText(QCoreApplication.translate("MainWindow", u"Contrast Screenshot", None))
        self.transcribe.setText(QCoreApplication.translate("MainWindow", u"Captions...", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuChange_Model.setTitle(QCoreApplication.translate("MainWindow", u"Change Transcription Model", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

