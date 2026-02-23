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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 200)
        MainWindow.setMinimumSize(QSize(400, 200))
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
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.openMagnify.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Opens a menu that allows you to magnify the screen.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.openMagnify.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Magnifies the screen.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.openMagnify.setText(QCoreApplication.translate("MainWindow", u"Open Magnification Menu...", None))
        self.contrast.setText(QCoreApplication.translate("MainWindow", u"Contrast Screenshot", None))
        self.transcribe.setText(QCoreApplication.translate("MainWindow", u"Transcribe...", None))
    # retranslateUi

