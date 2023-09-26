# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashScreenGeneratorXeZenN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMenuBar,
    QProgressBar,
    QSizePolicy,
    QStatusBar,
    QWidget,
)


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(803, 449)
        SplashScreen.setSizeIncrement(QSize(640, 400))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(
            "QFrame {\n"
            "	background-color:rgb(18, 26, 38);\n"
            "	color:rgb(220,220,220);\n"
            "	border-radius: 10px;\n"
            "}"
        )
        self.dropShadowFrame.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(140, 70, 521, 101))
        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet("color:rgb(56, 189, 248);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-4)
        self.label_2 = QLabel(self.dropShadowFrame)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(0, 160, 771, 31))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet("color:rgb(98, 114, 164);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(-4)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QRect(90, 280, 641, 23))
        self.progressBar.setStyleSheet(
            "QProgressBar{\n"
            "	background-color:rgb(98, 114, 164);\n"
            "	color:rgb(200,200,200);\n"
            "	font-size: 18px;\n"
            "	border-style: none;\n"
            "	border-radius:10px;\n"
            "	text-align:center;\n"
            "}\n"
            "QProgressBar::chunk{\n"
            "border-radius:10px;\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 255, 255), stop:0.971591 rgba(56, 189, 248, 255))\n"
            "}"
        )
        self.progressBar.setValue(24)
        self.label_3 = QLabel(self.dropShadowFrame)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(80, 310, 661, 31))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setStyleSheet("color:rgb(98, 114, 164);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setIndent(-4)
        self.label_4 = QLabel(self.dropShadowFrame)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(340, 350, 751, 31))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet("color:rgb(98, 114, 164);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setIndent(-4)

        self.horizontalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SplashScreen)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 22))
        SplashScreen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SplashScreen)
        self.statusbar.setObjectName("statusbar")
        SplashScreen.setStatusBar(self.statusbar)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(
            QCoreApplication.translate("SplashScreen", "MainWindow", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p><span style=" font-weight:700;">Password </span>generator</p></body></html>',
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p><span style=" font-size:14pt;">Randomize passwords with great ease</span></p></body></html>',
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p><span style=" font-size:11pt;">loading...</span></p></body></html>',
                None,
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p><span style=" font-size:9pt; font-weight:700;">Create:</span><span style=" font-size:9pt;"> Fabian</span></p><p><br/></p><p><br/></p><p><br/></p></body></html>',
                None,
            )
        )

    # retranslateUi
