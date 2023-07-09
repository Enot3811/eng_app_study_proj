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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(610, 530)
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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 591, 471))
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.verticalLayoutWidget = QWidget(self.mainPage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 591, 181))
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
        self.toAddSampleButton = QPushButton(self.verticalLayoutWidget)
        self.toAddSampleButton.setObjectName(u"toAddSampleButton")

        self.sampleEditingButtonHorizontalLayout.addWidget(self.toAddSampleButton)

        self.editSampleButton = QPushButton(self.verticalLayoutWidget)
        self.editSampleButton.setObjectName(u"editSampleButton")

        self.sampleEditingButtonHorizontalLayout.addWidget(self.editSampleButton)

        self.deleteSampleButton = QPushButton(self.verticalLayoutWidget)
        self.deleteSampleButton.setObjectName(u"deleteSampleButton")

        self.sampleEditingButtonHorizontalLayout.addWidget(self.deleteSampleButton)


        self.wordVerticalLayout.addLayout(self.sampleEditingButtonHorizontalLayout)

        self.translateTextEdit.raise_()
        self.wordZoneLabel.raise_()
        self.wordLineEdit.raise_()
        self.verticalLayoutWidget_2 = QWidget(self.mainPage)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 200, 591, 223))
        self.examplesVerticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.examplesVerticalLayout.setSpacing(10)
        self.examplesVerticalLayout.setObjectName(u"examplesVerticalLayout")
        self.examplesVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.exampleZoneLabel = QLabel(self.verticalLayoutWidget_2)
        self.exampleZoneLabel.setObjectName(u"exampleZoneLabel")
        self.exampleZoneLabel.setFont(font1)

        self.examplesVerticalLayout.addWidget(self.exampleZoneLabel)

        self.engExampleTextEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.engExampleTextEdit.setObjectName(u"engExampleTextEdit")
        self.engExampleTextEdit.setEnabled(True)
        self.engExampleTextEdit.setReadOnly(True)

        self.examplesVerticalLayout.addWidget(self.engExampleTextEdit)

        self.rusExampleTextEdit = QTextEdit(self.verticalLayoutWidget_2)
        self.rusExampleTextEdit.setObjectName(u"rusExampleTextEdit")
        self.rusExampleTextEdit.setEnabled(True)
        self.rusExampleTextEdit.setReadOnly(True)

        self.examplesVerticalLayout.addWidget(self.rusExampleTextEdit)

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

        self.horizontalLayoutWidget_2 = QWidget(self.mainPage)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 440, 591, 29))
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

        self.stackedWidget.addWidget(self.mainPage)
        self.sampleAddPage = QWidget()
        self.sampleAddPage.setObjectName(u"sampleAddPage")
        self.saveNewSampleButton = QPushButton(self.sampleAddPage)
        self.saveNewSampleButton.setObjectName(u"saveNewSampleButton")
        self.saveNewSampleButton.setGeometry(QRect(180, 0, 161, 25))
        self.wordZoneTitleLabel = QLabel(self.sampleAddPage)
        self.wordZoneTitleLabel.setObjectName(u"wordZoneTitleLabel")
        self.wordZoneTitleLabel.setGeometry(QRect(1, 1, 165, 22))
        self.wordZoneTitleLabel.setFont(font1)
        self.layoutWidget = QWidget(self.sampleAddPage)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 30, 591, 347))
        self.sampleAddAreaFormLayout = QFormLayout(self.layoutWidget)
        self.sampleAddAreaFormLayout.setObjectName(u"sampleAddAreaFormLayout")
        self.sampleAddAreaFormLayout.setHorizontalSpacing(10)
        self.sampleAddAreaFormLayout.setVerticalSpacing(10)
        self.sampleAddAreaFormLayout.setContentsMargins(0, 10, 0, 10)
        self.newWordLineEdit = QLineEdit(self.layoutWidget)
        self.newWordLineEdit.setObjectName(u"newWordLineEdit")
        self.newWordLineEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.newWordLineEdit.sizePolicy().hasHeightForWidth())
        self.newWordLineEdit.setSizePolicy(sizePolicy1)
        self.newWordLineEdit.setMinimumSize(QSize(350, 0))
        self.newWordLineEdit.setReadOnly(False)

        self.sampleAddAreaFormLayout.setWidget(0, QFormLayout.LabelRole, self.newWordLineEdit)

        self.newWordMsgLabel = QLabel(self.layoutWidget)
        self.newWordMsgLabel.setObjectName(u"newWordMsgLabel")

        self.sampleAddAreaFormLayout.setWidget(0, QFormLayout.FieldRole, self.newWordMsgLabel)

        self.newWordTranslateTextEdit = QTextEdit(self.layoutWidget)
        self.newWordTranslateTextEdit.setObjectName(u"newWordTranslateTextEdit")
        self.newWordTranslateTextEdit.setEnabled(True)
        self.newWordTranslateTextEdit.setMinimumSize(QSize(350, 60))
        self.newWordTranslateTextEdit.setReadOnly(False)

        self.sampleAddAreaFormLayout.setWidget(1, QFormLayout.LabelRole, self.newWordTranslateTextEdit)

        self.newWordTranslateMsgLabel = QLabel(self.layoutWidget)
        self.newWordTranslateMsgLabel.setObjectName(u"newWordTranslateMsgLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.newWordTranslateMsgLabel.sizePolicy().hasHeightForWidth())
        self.newWordTranslateMsgLabel.setSizePolicy(sizePolicy2)

        self.sampleAddAreaFormLayout.setWidget(1, QFormLayout.FieldRole, self.newWordTranslateMsgLabel)

        self.newWordExampleEngTextEdit = QTextEdit(self.layoutWidget)
        self.newWordExampleEngTextEdit.setObjectName(u"newWordExampleEngTextEdit")
        self.newWordExampleEngTextEdit.setEnabled(True)
        self.newWordExampleEngTextEdit.setMinimumSize(QSize(350, 100))
        self.newWordExampleEngTextEdit.setReadOnly(False)

        self.sampleAddAreaFormLayout.setWidget(2, QFormLayout.LabelRole, self.newWordExampleEngTextEdit)

        self.newWordExampleRusTextEdit = QTextEdit(self.layoutWidget)
        self.newWordExampleRusTextEdit.setObjectName(u"newWordExampleRusTextEdit")
        self.newWordExampleRusTextEdit.setEnabled(True)
        self.newWordExampleRusTextEdit.setMinimumSize(QSize(350, 100))
        self.newWordExampleRusTextEdit.setReadOnly(False)

        self.sampleAddAreaFormLayout.setWidget(3, QFormLayout.LabelRole, self.newWordExampleRusTextEdit)

        self.newWordExampleRusMsgLabel = QLabel(self.layoutWidget)
        self.newWordExampleRusMsgLabel.setObjectName(u"newWordExampleRusMsgLabel")
        sizePolicy2.setHeightForWidth(self.newWordExampleRusMsgLabel.sizePolicy().hasHeightForWidth())
        self.newWordExampleRusMsgLabel.setSizePolicy(sizePolicy2)

        self.sampleAddAreaFormLayout.setWidget(3, QFormLayout.FieldRole, self.newWordExampleRusMsgLabel)

        self.newWordExampleEngMsgLabel = QLabel(self.layoutWidget)
        self.newWordExampleEngMsgLabel.setObjectName(u"newWordExampleEngMsgLabel")
        sizePolicy2.setHeightForWidth(self.newWordExampleEngMsgLabel.sizePolicy().hasHeightForWidth())
        self.newWordExampleEngMsgLabel.setSizePolicy(sizePolicy2)

        self.sampleAddAreaFormLayout.setWidget(2, QFormLayout.FieldRole, self.newWordExampleEngMsgLabel)

        self.fromAddToMainPushButton = QPushButton(self.sampleAddPage)
        self.fromAddToMainPushButton.setObjectName(u"fromAddToMainPushButton")
        self.fromAddToMainPushButton.setGeometry(QRect(220, 390, 151, 25))
        self.stackedWidget.addWidget(self.sampleAddPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 610, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Eng app", None))
        self.wordZoneLabel.setText(QCoreApplication.translate("MainWindow", u"Word and translate", None))
        self.wordLineEdit.setText("")
        self.toAddSampleButton.setText(QCoreApplication.translate("MainWindow", u"Add Sample", None))
        self.editSampleButton.setText(QCoreApplication.translate("MainWindow", u"Edit Sample", None))
        self.deleteSampleButton.setText(QCoreApplication.translate("MainWindow", u"Delete Sample", None))
        self.exampleZoneLabel.setText(QCoreApplication.translate("MainWindow", u"Examples", None))
        self.engExampleTextEdit.setPlaceholderText("")
        self.rusExampleTextEdit.setPlaceholderText("")
        self.leftExampleButton.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.addExampleButton.setText(QCoreApplication.translate("MainWindow", u"Add Example", None))
        self.editExampleButton.setText(QCoreApplication.translate("MainWindow", u"Edit Example", None))
        self.deleteExampleButton.setText(QCoreApplication.translate("MainWindow", u"Delete example", None))
        self.rightExampleButton.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.previousSampleButton.setText(QCoreApplication.translate("MainWindow", u"Previous Sample", None))
        self.randomSampleButton.setText(QCoreApplication.translate("MainWindow", u"Random Sample", None))
        self.nextSampleButton.setText(QCoreApplication.translate("MainWindow", u"Next Sample", None))
        self.saveNewSampleButton.setText(QCoreApplication.translate("MainWindow", u"Add to dictionary", None))
        self.wordZoneTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Word and translate", None))
#if QT_CONFIG(tooltip)
        self.newWordLineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.newWordLineEdit.setText("")
        self.newWordMsgLabel.setText(QCoreApplication.translate("MainWindow", u"Type a new word", None))
        self.newWordTranslateTextEdit.setDocumentTitle("")
        self.newWordTranslateMsgLabel.setText(QCoreApplication.translate("MainWindow", u"Type the word's translates", None))
        self.newWordExampleRusMsgLabel.setText(QCoreApplication.translate("MainWindow", u"Type a translate of\n"
"the example sentance", None))
        self.newWordExampleEngMsgLabel.setText(QCoreApplication.translate("MainWindow", u"Type an example sentance\n"
"that contains the word", None))
        self.fromAddToMainPushButton.setText(QCoreApplication.translate("MainWindow", u"Back to dictionary", None))
    # retranslateUi

