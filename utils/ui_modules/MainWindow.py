# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 470)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 591, 161))
        self.wordVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.wordVerticalLayout.setSpacing(10)
        self.wordVerticalLayout.setObjectName(u"wordVerticalLayout")
        self.wordVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.wordZoneLabel = QLabel(self.verticalLayoutWidget)
        self.wordZoneLabel.setObjectName(u"wordZoneLabel")
        font1 = QFont()
        font1.setPointSize(14)
        self.wordZoneLabel.setFont(font1)

        self.wordVerticalLayout.addWidget(self.wordZoneLabel)

        self.wordLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.wordLineEdit.setObjectName(u"wordLineEdit")
        self.wordLineEdit.setEnabled(True)
        self.wordLineEdit.setReadOnly(True)

        self.wordVerticalLayout.addWidget(self.wordLineEdit)

        self.translateTextEdit = QTextEdit(self.verticalLayoutWidget)
        self.translateTextEdit.setObjectName(u"translateTextEdit")
        self.translateTextEdit.setEnabled(True)
        self.translateTextEdit.setReadOnly(True)

        self.wordVerticalLayout.addWidget(self.translateTextEdit)

        self.sampleEditingButtonHorizontalLayout = QHBoxLayout()
        self.sampleEditingButtonHorizontalLayout.setSpacing(15)
        self.sampleEditingButtonHorizontalLayout.setObjectName(u"sampleEditingButtonHorizontalLayout")
        self.addSampleButton = QPushButton(self.verticalLayoutWidget)
        self.addSampleButton.setObjectName(u"addSampleButton")

        self.sampleEditingButtonHorizontalLayout.addWidget(self.addSampleButton)

        self.editSampleButton = QPushButton(self.verticalLayoutWidget)
        self.editSampleButton.setObjectName(u"editSampleButton")

        self.sampleEditingButtonHorizontalLayout.addWidget(self.editSampleButton)

        self.deleteSampleButton = QPushButton(self.verticalLayoutWidget)
        self.deleteSampleButton.setObjectName(u"deleteSampleButton")

        self.sampleEditingButtonHorizontalLayout.addWidget(self.deleteSampleButton)


        self.wordVerticalLayout.addLayout(self.sampleEditingButtonHorizontalLayout)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 190, 591, 211))
        self.examplesVerticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.examplesVerticalLayout.setSpacing(10)
        self.examplesVerticalLayout.setObjectName(u"examplesVerticalLayout")
        self.examplesVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.exampleZoneLabel = QLabel(self.verticalLayoutWidget_2)
        self.exampleZoneLabel.setObjectName(u"exampleZoneLabel")
        self.exampleZoneLabel.setFont(font1)

        self.examplesVerticalLayout.addWidget(self.exampleZoneLabel)

        self.textEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)

        self.examplesVerticalLayout.addWidget(self.textEdit)

        self.plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setReadOnly(True)

        self.examplesVerticalLayout.addWidget(self.plainTextEdit)

        self.exampleButtonsHorizontalLayout = QHBoxLayout()
        self.exampleButtonsHorizontalLayout.setSpacing(10)
        self.exampleButtonsHorizontalLayout.setObjectName(u"exampleButtonsHorizontalLayout")
        self.leftExampleButton = QPushButton(self.verticalLayoutWidget_2)
        self.leftExampleButton.setObjectName(u"leftExampleButton")

        self.exampleButtonsHorizontalLayout.addWidget(self.leftExampleButton)

        self.addExampleButton = QPushButton(self.verticalLayoutWidget_2)
        self.addExampleButton.setObjectName(u"addExampleButton")

        self.exampleButtonsHorizontalLayout.addWidget(self.addExampleButton)

        self.editExampleButton = QPushButton(self.verticalLayoutWidget_2)
        self.editExampleButton.setObjectName(u"editExampleButton")

        self.exampleButtonsHorizontalLayout.addWidget(self.editExampleButton)

        self.deleteExampleButton = QPushButton(self.verticalLayoutWidget_2)
        self.deleteExampleButton.setObjectName(u"deleteExampleButton")

        self.exampleButtonsHorizontalLayout.addWidget(self.deleteExampleButton)

        self.rightExampleButton = QPushButton(self.verticalLayoutWidget_2)
        self.rightExampleButton.setObjectName(u"rightExampleButton")

        self.exampleButtonsHorizontalLayout.addWidget(self.rightExampleButton)


        self.examplesVerticalLayout.addLayout(self.exampleButtonsHorizontalLayout)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 420, 591, 29))
        self.actionButtonHorizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.actionButtonHorizontalLayout.setSpacing(20)
        self.actionButtonHorizontalLayout.setObjectName(u"actionButtonHorizontalLayout")
        self.actionButtonHorizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.previousSampleButton = QPushButton(self.horizontalLayoutWidget_2)
        self.previousSampleButton.setObjectName(u"previousSampleButton")

        self.actionButtonHorizontalLayout.addWidget(self.previousSampleButton)

        self.randomSampleButton = QPushButton(self.horizontalLayoutWidget_2)
        self.randomSampleButton.setObjectName(u"randomSampleButton")

        self.actionButtonHorizontalLayout.addWidget(self.randomSampleButton)

        self.nextSampleButton = QPushButton(self.horizontalLayoutWidget_2)
        self.nextSampleButton.setObjectName(u"nextSampleButton")

        self.actionButtonHorizontalLayout.addWidget(self.nextSampleButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 610, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Eng app", None))
        self.wordZoneLabel.setText(QCoreApplication.translate("MainWindow", u"Word and translate", None))
        self.wordLineEdit.setText("")
        self.addSampleButton.setText(QCoreApplication.translate("MainWindow", u"Add Sample", None))
        self.editSampleButton.setText(QCoreApplication.translate("MainWindow", u"Edit Sample", None))
        self.deleteSampleButton.setText(QCoreApplication.translate("MainWindow", u"Delete Sample", None))
        self.exampleZoneLabel.setText(QCoreApplication.translate("MainWindow", u"Examples", None))
        self.textEdit.setPlaceholderText("")
        self.plainTextEdit.setPlaceholderText("")
        self.leftExampleButton.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.addExampleButton.setText(QCoreApplication.translate("MainWindow", u"Add Example", None))
        self.editExampleButton.setText(QCoreApplication.translate("MainWindow", u"Edit Example", None))
        self.deleteExampleButton.setText(QCoreApplication.translate("MainWindow", u"Delete example", None))
        self.rightExampleButton.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.previousSampleButton.setText(QCoreApplication.translate("MainWindow", u"Previous Sample", None))
        self.randomSampleButton.setText(QCoreApplication.translate("MainWindow", u"Random Sample", None))
        self.nextSampleButton.setText(QCoreApplication.translate("MainWindow", u"Next Sample", None))
    # retranslateUi

