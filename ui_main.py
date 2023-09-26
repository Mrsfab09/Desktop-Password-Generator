# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainoRypdX.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 594)
        MainWindow.setStyleSheet("background-color:rgb(18, 26, 38);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(0, 4, 811, 591))
        self.label.setStyleSheet("background-color: rgb(18, 26, 38);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(90, 340, 641, 61))
        self.label_2.setStyleSheet(
            "background-color: rgb(78, 78, 91);\n" "border-radius:10px;"
        )
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setGeometry(QRect(290, 450, 211, 51))
        self.pushButton.setStyleSheet(
            "background-color: rgb(46, 153, 247);\n"
            "color:white;\n"
            "font-size: 20px;\n"
            "font-weight:600;\n"
            "border: none;\n"
            "border-radius:10px;"
        )
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(360, 30, 81, 31))
        self.label_3.setStyleSheet(
            "color:white;\n"
            "font-size: 25px;\n"
            "font-weight:600;\n"
            "text-align: center;"
        )
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(330, 90, 51, 21))
        self.label_4.setStyleSheet(
            "color:white;\n" "font-weight:500;\n" "font-size: 15px;"
        )
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setGeometry(QRect(430, 90, 42, 22))
        self.spinBox.setStyleSheet(
            "background-color: rgb(78, 78, 91);\n" "border:none;"
        )
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(310, 130, 101, 21))
        self.label_6.setStyleSheet(
            "color:white;\n" "font-weight:500;\n" "font-size: 15px;"
        )
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setGeometry(QRect(430, 130, 42, 22))
        self.spinBox_2.setStyleSheet(
            "background-color: rgb(78, 78, 91);\n" "border:none;"
        )
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(310, 170, 101, 21))
        self.label_7.setStyleSheet(
            "color:white;\n" "font-weight:500;\n" "font-size: 15px;"
        )
        self.spinBox_3 = QSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setGeometry(QRect(430, 170, 42, 22))
        self.spinBox_3.setStyleSheet(
            "background-color: rgb(78, 78, 91);\n" "border:none;"
        )
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QRect(310, 210, 101, 21))
        self.label_8.setStyleSheet(
            "color:white;\n" "font-weight:500;\n" "font-size: 15px;"
        )
        self.spinBox_4 = QSpinBox(self.centralwidget)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setGeometry(QRect(430, 210, 42, 22))
        self.spinBox_4.setStyleSheet(
            "background-color: rgb(78, 78, 91);\n" "border:none;"
        )
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.label_9.setGeometry(QRect(310, 250, 101, 21))
        self.label_9.setStyleSheet(
            "color:white;\n" "font-weight:500;\n" "font-size: 15px;"
        )
        self.spinBox_5 = QSpinBox(self.centralwidget)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_5.setGeometry(QRect(430, 250, 42, 22))
        self.spinBox_5.setStyleSheet(
            "background-color: rgb(78, 78, 91);\n" "border:none;"
        )
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Generating", None)
        )
        self.label_3.setText(QCoreApplication.translate("MainWindow", "MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Long:", None))
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Small letters:", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", "Uppercase:", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", "Special signs:", None)
        )
        self.label_9.setText(QCoreApplication.translate("MainWindow", "Numbers:", None))

    # retranslateUi
