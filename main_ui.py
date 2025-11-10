# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(478, 505)
        MainWindow.setMinimumSize(QSize(478, 505))
        MainWindow.setMaximumSize(QSize(478, 505))
        MainWindow.setStyleSheet(u"* {\n"
"font-family: \"Noto Sans\";\n"
"font-size: 9pt;\n"
"}\n"
"\n"
"QMainWindow > QWidget {\n"
"    background-color: #f0f0f0;\n"
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
        self.actionOptions = QAction(MainWindow)
        self.actionOptions.setObjectName(u"actionOptions")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.actionOptions.setIcon(icon)
        self.actionDebug = QAction(MainWindow)
        self.actionDebug.setObjectName(u"actionDebug")
        self.actionDebug.setCheckable(True)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.actionDebug.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowserLogview = QTextBrowser(self.centralwidget)
        self.textBrowserLogview.setObjectName(u"textBrowserLogview")
        self.textBrowserLogview.setGeometry(QRect(10, 220, 450, 240))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 240, 101))
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 206, 60))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelID = QLabel(self.layoutWidget)
        self.labelID.setObjectName(u"labelID")
        self.labelID.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelID, 0, 0, 1, 1)

        self.lineEditID = QLineEdit(self.layoutWidget)
        self.lineEditID.setObjectName(u"lineEditID")

        self.gridLayout.addWidget(self.lineEditID, 0, 1, 1, 1)

        self.labelPW = QLabel(self.layoutWidget)
        self.labelPW.setObjectName(u"labelPW")
        self.labelPW.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelPW, 1, 0, 1, 1)

        self.lineEditPW = QLineEdit(self.layoutWidget)
        self.lineEditPW.setObjectName(u"lineEditPW")
        self.lineEditPW.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEditPW, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(260, 10, 200, 200))
        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(11, 30, 170, 170))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButtonStart = QRadioButton(self.layoutWidget1)
        self.radioButtonStart.setObjectName(u"radioButtonStart")

        self.gridLayout_2.addWidget(self.radioButtonStart, 0, 0, 1, 1)

        self.radioButtonStartmin = QRadioButton(self.layoutWidget1)
        self.radioButtonStartmin.setObjectName(u"radioButtonStartmin")

        self.gridLayout_2.addWidget(self.radioButtonStartmin, 1, 0, 1, 1)

        self.spinBoxValuemin = QSpinBox(self.layoutWidget1)
        self.spinBoxValuemin.setObjectName(u"spinBoxValuemin")

        self.gridLayout_2.addWidget(self.spinBoxValuemin, 1, 1, 1, 1)

        self.radioButtonStartpage = QRadioButton(self.layoutWidget1)
        self.radioButtonStartpage.setObjectName(u"radioButtonStartpage")
        self.radioButtonStartpage.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.radioButtonStartpage, 2, 0, 1, 1)

        self.lineEditValuepage = QLineEdit(self.layoutWidget1)
        self.lineEditValuepage.setObjectName(u"lineEditValuepage")

        self.gridLayout_2.addWidget(self.lineEditValuepage, 2, 1, 1, 1)

        self.radioButtonStartforce = QRadioButton(self.layoutWidget1)
        self.radioButtonStartforce.setObjectName(u"radioButtonStartforce")

        self.gridLayout_2.addWidget(self.radioButtonStartforce, 3, 0, 1, 1)

        self.radioButtonStartreset = QRadioButton(self.layoutWidget1)
        self.radioButtonStartreset.setObjectName(u"radioButtonStartreset")

        self.gridLayout_2.addWidget(self.radioButtonStartreset, 4, 0, 1, 1)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 120, 240, 40))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonStart = QPushButton(self.layoutWidget2)
        self.pushButtonStart.setObjectName(u"pushButtonStart")

        self.horizontalLayout.addWidget(self.pushButtonStart)

        self.pushButtonCancel = QPushButton(self.layoutWidget2)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout.addWidget(self.pushButtonCancel)

        self.pushButtonSavefile = QPushButton(self.layoutWidget2)
        self.pushButtonSavefile.setObjectName(u"pushButtonSavefile")

        self.horizontalLayout.addWidget(self.pushButtonSavefile)

        MainWindow.setCentralWidget(self.centralwidget)
        self.layoutWidget2.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.textBrowserLogview.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 478, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionOptions)
        self.menu.addAction(self.actionDebug)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOptions.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00\uae30\ub2a5", None))
#if QT_CONFIG(shortcut)
        self.actionOptions.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionDebug.setText(QCoreApplication.translate("MainWindow", u"\ub514\ubc84\uadf8 \ub85c\uadf8 \ud65c\uc131\ud654", None))
#if QT_CONFIG(shortcut)
        self.actionDebug.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+D", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\uc548\uc804\uc2e0\ubb38\uace0 \ub85c\uadf8\uc778", None))
        self.labelID.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.labelPW.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\ud06c\ub864\ub9c1 \ubaa8\ub4dc \uc9c0\uc815", None))
        self.radioButtonStart.setText(QCoreApplication.translate("MainWindow", u"\uc77c\ubc18 \ud0d0\uc0c9", None))
        self.radioButtonStartmin.setText(QCoreApplication.translate("MainWindow", u"\uc870\uac74\ubd80 \ud0d0\uc0c9", None))
        self.radioButtonStartpage.setText(QCoreApplication.translate("MainWindow", u"\ud398\uc774\uc9c0 \uc9c0\uc815", None))
        self.lineEditValuepage.setInputMask("")
        self.lineEditValuepage.setPlaceholderText(QCoreApplication.translate("MainWindow", u": , \ub85c \uad6c\ubd84", None))
        self.radioButtonStartforce.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uac31\uc2e0", None))
        self.radioButtonStartreset.setText(QCoreApplication.translate("MainWindow", u"\uac15\uc81c \ucd08\uae30\ud654", None))
        self.pushButtonStart.setText(QCoreApplication.translate("MainWindow", u"\ud06c\ub864\ub9c1 \uc2dc\uc791", None))
#if QT_CONFIG(shortcut)
        self.pushButtonStart.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.pushButtonCancel.setText(QCoreApplication.translate("MainWindow", u"\uc791\uc5c5 \uc911\uc9c0", None))
        self.pushButtonSavefile.setText(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140\ub9cc \uc800\uc7a5", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uc635\uc158", None))
    # retranslateUi

