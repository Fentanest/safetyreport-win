# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(379, 532)
        Dialog.setMinimumSize(QSize(379, 532))
        Dialog.setMaximumSize(QSize(379, 532))
        Dialog.setStyleSheet(u"* {\n"
"font-family: \"Noto Sans\";\n"
"font-size: 9pt;\n"
"}\n"
"\n"
"\n"
"QDialog {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QGroupBox {\n"
"background-color: rgb(244, 246, 251)\n"
"}\n"
"\n"
"QListView {\n"
"background-color: #ffffff;\n"
"}\n"
"\n"
"/* RadioButton \uae30\ubcf8 indicator \uc2a4\ud0c0\uc77c */\n"
"QRadioButton::indicator:unchecked {\n"
"background-color: white;\n"
"border: 2px solid white;\n"
"}\n"
"/* \uc120\ud0dd \uc2dc \uc0c9\uae54 */\n"
"QRadioButton::indicator:checked {\n"
"background-color: black;\n"
"border: 2px solid white;\n"
"}")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(90, 480, 180, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 340, 240))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 32, 300, 190))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBoxTelegrambot = QCheckBox(self.layoutWidget)
        self.checkBoxTelegrambot.setObjectName(u"checkBoxTelegrambot")

        self.gridLayout.addWidget(self.checkBoxTelegrambot, 0, 0, 1, 3)

        self.labelToken = QLabel(self.layoutWidget)
        self.labelToken.setObjectName(u"labelToken")
        self.labelToken.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelToken, 1, 0, 1, 1)

        self.lineEditToken = QLineEdit(self.layoutWidget)
        self.lineEditToken.setObjectName(u"lineEditToken")

        self.gridLayout.addWidget(self.lineEditToken, 1, 1, 1, 2)

        self.labelChatID = QLabel(self.layoutWidget)
        self.labelChatID.setObjectName(u"labelChatID")
        self.labelChatID.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelChatID, 2, 0, 1, 1)

        self.lineEditChatID = QLineEdit(self.layoutWidget)
        self.lineEditChatID.setObjectName(u"lineEditChatID")

        self.gridLayout.addWidget(self.lineEditChatID, 2, 1, 1, 2)

        self.checkBoxGoogleSheet = QCheckBox(self.layoutWidget)
        self.checkBoxGoogleSheet.setObjectName(u"checkBoxGoogleSheet")

        self.gridLayout.addWidget(self.checkBoxGoogleSheet, 3, 0, 1, 3)

        self.labelGoogleSheet = QLabel(self.layoutWidget)
        self.labelGoogleSheet.setObjectName(u"labelGoogleSheet")
        self.labelGoogleSheet.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelGoogleSheet, 4, 0, 1, 2)

        self.lineEditGoogleSheet = QLineEdit(self.layoutWidget)
        self.lineEditGoogleSheet.setObjectName(u"lineEditGoogleSheet")

        self.gridLayout.addWidget(self.lineEditGoogleSheet, 4, 2, 1, 1)

        self.labelGoogleSheetJSON = QLabel(self.layoutWidget)
        self.labelGoogleSheetJSON.setObjectName(u"labelGoogleSheetJSON")
        self.labelGoogleSheetJSON.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelGoogleSheetJSON, 5, 0, 1, 2)

        self.pushButtonGoogleSheetJSON = QPushButton(self.layoutWidget)
        self.pushButtonGoogleSheetJSON.setObjectName(u"pushButtonGoogleSheetJSON")

        self.gridLayout.addWidget(self.pushButtonGoogleSheetJSON, 5, 2, 1, 1)

        self.labelGoogleSheetJSONstatus = QLabel(self.layoutWidget)
        self.labelGoogleSheetJSONstatus.setObjectName(u"labelGoogleSheetJSONstatus")
        self.labelGoogleSheetJSONstatus.setMinimumSize(QSize(70, 0))

        self.gridLayout.addWidget(self.labelGoogleSheetJSONstatus, 5, 3, 1, 1)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 280, 340, 180))
        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 35, 300, 123))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButtonUseChrome = QRadioButton(self.layoutWidget1)
        self.radioButtonUseChrome.setObjectName(u"radioButtonUseChrome")

        self.verticalLayout.addWidget(self.radioButtonUseChrome)

        self.checkBoxHeadless = QCheckBox(self.layoutWidget1)
        self.checkBoxHeadless.setObjectName(u"checkBoxHeadless")

        self.verticalLayout.addWidget(self.checkBoxHeadless)

        self.radioButtonUseHub = QRadioButton(self.layoutWidget1)
        self.radioButtonUseHub.setObjectName(u"radioButtonUseHub")

        self.verticalLayout.addWidget(self.radioButtonUseHub)

        self.lineEditHubURL = QLineEdit(self.layoutWidget1)
        self.lineEditHubURL.setObjectName(u"lineEditHubURL")

        self.verticalLayout.addWidget(self.lineEditHubURL)

        self.groupBox.raise_()
        self.buttonBox.raise_()
        self.groupBox_2.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\ucd94\uac00 \uae30\ub2a5 \ud65c\uc131\ud654", None))
        self.checkBoxTelegrambot.setText(QCoreApplication.translate("Dialog", u"\ud154\ub808\uadf8\ub7a8 \ubd07 \ud65c\uc131\ud654", None))
        self.labelToken.setText(QCoreApplication.translate("Dialog", u"Token:", None))
        self.labelChatID.setText(QCoreApplication.translate("Dialog", u"Chat_id:", None))
        self.checkBoxGoogleSheet.setText(QCoreApplication.translate("Dialog", u"\uad6c\uae00\uc2dc\ud2b8 \ud65c\uc131\ud654", None))
        self.labelGoogleSheet.setText(QCoreApplication.translate("Dialog", u"\uad6c\uae00 \uc2dc\ud2b8 \uc8fc\uc18c:", None))
        self.labelGoogleSheetJSON.setText(QCoreApplication.translate("Dialog", u"JSON\ud30c\uc77c:", None))
        self.pushButtonGoogleSheetJSON.setText(QCoreApplication.translate("Dialog", u"\ucc3e\uc544\ubcf4\uae30", None))
        self.labelGoogleSheetJSONstatus.setText(QCoreApplication.translate("Dialog", u"\ucc3e\uc744 \uc218 \uc5c6\uc74c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Selenium Hub \ud65c\uc131\ud654", None))
        self.radioButtonUseChrome.setText(QCoreApplication.translate("Dialog", u"No(\ub370\uc2a4\ud06c\ud0d1 \ud06c\ub86c \uc0ac\uc6a9, \uae30\ubcf8\uac12)", None))
        self.checkBoxHeadless.setText(QCoreApplication.translate("Dialog", u"Headless", None))
        self.radioButtonUseHub.setText(QCoreApplication.translate("Dialog", u"Yes(Selenium Hub \uc8fc\uc18c \uc785\ub825 \ud544\uc694)", None))
    # retranslateUi

