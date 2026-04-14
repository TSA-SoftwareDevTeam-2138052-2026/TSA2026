# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose_transcript_mode.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 200)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.captionsButton = QPushButton(Dialog)
        self.captionsButton.setObjectName(u"captionsButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captionsButton.sizePolicy().hasHeightForWidth())
        self.captionsButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setWeight(QFont.DemiBold)
        self.captionsButton.setFont(font)

        self.gridLayout.addWidget(self.captionsButton, 0, 0, 1, 1)

        self.transcriptButton = QPushButton(Dialog)
        self.transcriptButton.setObjectName(u"transcriptButton")
        sizePolicy.setHeightForWidth(self.transcriptButton.sizePolicy().hasHeightForWidth())
        self.transcriptButton.setSizePolicy(sizePolicy)
        self.transcriptButton.setFont(font)

        self.gridLayout.addWidget(self.transcriptButton, 0, 1, 1, 1)

        self.bothButton = QPushButton(Dialog)
        self.bothButton.setObjectName(u"bothButton")
        sizePolicy.setHeightForWidth(self.bothButton.sizePolicy().hasHeightForWidth())
        self.bothButton.setSizePolicy(sizePolicy)
        self.bothButton.setFont(font)

        self.gridLayout.addWidget(self.bothButton, 1, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.captionsButton.setText(QCoreApplication.translate("Dialog", u"Caption a video", None))
        self.transcriptButton.setText(QCoreApplication.translate("Dialog", u"Transcribe a video", None))
        self.bothButton.setText(QCoreApplication.translate("Dialog", u"Do both", None))
    # retranslateUi

