# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(713, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.match_btn = QPushButton(self.centralwidget)
        self.match_btn.setObjectName(u"match_btn")

        self.verticalLayout.addWidget(self.match_btn)

        self.start_btn = QPushButton(self.centralwidget)
        self.start_btn.setObjectName(u"start_btn")

        self.verticalLayout.addWidget(self.start_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.chess_text = QLineEdit(self.centralwidget)
        self.chess_text.setObjectName(u"chess_text")

        self.verticalLayout.addWidget(self.chess_text)

        self.pai_text = QLineEdit(self.centralwidget)
        self.pai_text.setObjectName(u"pai_text")

        self.verticalLayout.addWidget(self.pai_text)

        self.from_text = QLineEdit(self.centralwidget)
        self.from_text.setObjectName(u"from_text")

        self.verticalLayout.addWidget(self.from_text)

        self.to_text = QLineEdit(self.centralwidget)
        self.to_text.setObjectName(u"to_text")

        self.verticalLayout.addWidget(self.to_text)

        self.move_btn = QPushButton(self.centralwidget)
        self.move_btn.setObjectName(u"move_btn")

        self.verticalLayout.addWidget(self.move_btn)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_area = QTextEdit(self.centralwidget)
        self.text_area.setObjectName(u"text_area")

        self.gridLayout.addWidget(self.text_area, 1, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.match_btn.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d", None))
        self.start_btn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6e38\u620f", None))
        self.chess_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u68cb\u5b50id", None))
        self.pai_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u724cid", None))
        self.from_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"from\u4f4d\u7f6e", None))
        self.to_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"to\u4f4d\u7f6e", None))
        self.move_btn.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u52a8", None))
    # retranslateUi

