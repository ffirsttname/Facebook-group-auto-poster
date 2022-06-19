# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'facebook_auto_post_UISAFffa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(671, 433)
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 671, 401))
        self.tabWidget.setMaximumSize(QSize(671, 401))
        font = QFont()
        font.setFamily(u"Noto Sans SC Medium")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.facebook_list = QWidget()
        self.facebook_list.setObjectName(u"facebook_list")
        self.group_table = QTableWidget(self.facebook_list)
        if (self.group_table.columnCount() < 3):
            self.group_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.group_table.setObjectName(u"group_table")
        self.group_table.setGeometry(QRect(0, 30, 671, 341))
        self.group_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.group_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.group_table.setTextElideMode(Qt.ElideMiddle)
        self.group_table.setColumnCount(3)
        self.group_table.horizontalHeader().setVisible(False)
        self.group_table.verticalHeader().setVisible(False)
        self.layoutWidget = QWidget(self.facebook_list)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 320, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.all_select = QPushButton(self.layoutWidget)
        self.all_select.setObjectName(u"all_select")

        self.horizontalLayout_2.addWidget(self.all_select)

        self.reverse_select = QPushButton(self.layoutWidget)
        self.reverse_select.setObjectName(u"reverse_select")

        self.horizontalLayout_2.addWidget(self.reverse_select)

        self.cancel_select = QPushButton(self.layoutWidget)
        self.cancel_select.setObjectName(u"cancel_select")

        self.horizontalLayout_2.addWidget(self.cancel_select)

        self.copy_group_id = QPushButton(self.layoutWidget)
        self.copy_group_id.setObjectName(u"copy_group_id")

        self.horizontalLayout_2.addWidget(self.copy_group_id)

        self.tabWidget.addTab(self.facebook_list, "")
        self.auto_group_posting = QWidget()
        self.auto_group_posting.setObjectName(u"auto_group_posting")
        self.layoutWidget1 = QWidget(self.auto_group_posting)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 661, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.group_id = QLineEdit(self.layoutWidget1)
        self.group_id.setObjectName(u"group_id")

        self.horizontalLayout_7.addWidget(self.group_id)

        self.layoutWidget2 = QWidget(self.auto_group_posting)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 30, 411, 331))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.posting_information = QTextEdit(self.layoutWidget2)
        self.posting_information.setObjectName(u"posting_information")

        self.verticalLayout_3.addWidget(self.posting_information)

        self.browser_location = QLineEdit(self.auto_group_posting)
        self.browser_location.setObjectName(u"browser_location")
        self.browser_location.setGeometry(QRect(430, 120, 167, 29))
        self.start_auto_post_group_button = QPushButton(self.auto_group_posting)
        self.start_auto_post_group_button.setObjectName(u"start_auto_post_group_button")
        self.start_auto_post_group_button.setGeometry(QRect(480, 220, 81, 41))
        self.chromedriver_location_choose = QLabel(self.auto_group_posting)
        self.chromedriver_location_choose.setObjectName(u"chromedriver_location_choose")
        self.chromedriver_location_choose.setGeometry(QRect(610, 180, 31, 31))
        self.chromedriver_location_choose.setPixmap(QPixmap(u":/123/folder.png"))
        self.chromedriver_location_choose.setScaledContents(True)
        self.chromedriver_location = QLineEdit(self.auto_group_posting)
        self.chromedriver_location.setObjectName(u"chromedriver_location")
        self.chromedriver_location.setGeometry(QRect(430, 180, 167, 29))
        self.current_posting = QLineEdit(self.auto_group_posting)
        self.current_posting.setObjectName(u"current_posting")
        self.current_posting.setGeometry(QRect(450, 280, 41, 41))
        self.current_posting.setAlignment(Qt.AlignCenter)
        self.label_18 = QLabel(self.auto_group_posting)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(500, 260, 121, 71))
        self.label_18.setWordWrap(True)
        self.layoutWidget3 = QWidget(self.auto_group_posting)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(440, 30, 151, 91))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.browser_box = QComboBox(self.layoutWidget3)
        self.browser_box.addItem("")
        self.browser_box.addItem("")
        self.browser_box.setObjectName(u"browser_box")

        self.verticalLayout_2.addWidget(self.browser_box)

        self.label_5 = QLabel(self.layoutWidget3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.browser_location_choose = QLabel(self.auto_group_posting)
        self.browser_location_choose.setObjectName(u"browser_location_choose")
        self.browser_location_choose.setGeometry(QRect(610, 120, 31, 31))
        self.browser_location_choose.setPixmap(QPixmap(u":/123/folder.png"))
        self.browser_location_choose.setScaledContents(True)
        self.layoutWidget4 = QWidget(self.auto_group_posting)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(430, 148, 226, 31))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_8)

        self.get_chromedriver_url = QLabel(self.layoutWidget4)
        self.get_chromedriver_url.setObjectName(u"get_chromedriver_url")
        self.get_chromedriver_url.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.get_chromedriver_url)

        self.tabWidget.addTab(self.auto_group_posting, "")
        self.setting = QWidget()
        self.setting.setObjectName(u"setting")
        self.layoutWidget5 = QWidget(self.setting)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(0, 40, 661, 31))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget5)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.tokens = QLineEdit(self.layoutWidget5)
        self.tokens.setObjectName(u"tokens")

        self.horizontalLayout.addWidget(self.tokens)

        self.get_tokens_url = QLabel(self.layoutWidget5)
        self.get_tokens_url.setObjectName(u"get_tokens_url")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.get_tokens_url.setPalette(palette)
        self.get_tokens_url.setFocusPolicy(Qt.NoFocus)
        self.get_tokens_url.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.get_tokens_url)

        self.language_switch = QComboBox(self.setting)
        self.language_switch.addItem("")
        self.language_switch.addItem("")
        self.language_switch.setObjectName(u"language_switch")
        self.language_switch.setGeometry(QRect(0, 5, 141, 29))
        self.layoutWidget6 = QWidget(self.setting)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(0, 70, 491, 71))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.label_6 = QLabel(self.layoutWidget6)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.facebook_email = QLineEdit(self.layoutWidget6)
        self.facebook_email.setObjectName(u"facebook_email")

        self.horizontalLayout_4.addWidget(self.facebook_email)

        self.remember_email = QCheckBox(self.layoutWidget6)
        self.remember_email.setObjectName(u"remember_email")

        self.horizontalLayout_4.addWidget(self.remember_email)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(64, -1, -1, -1)
        self.label_7 = QLabel(self.layoutWidget6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.facebook_pw = QLineEdit(self.layoutWidget6)
        self.facebook_pw.setObjectName(u"facebook_pw")
        self.facebook_pw.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.facebook_pw)

        self.remember_pw = QCheckBox(self.layoutWidget6)
        self.remember_pw.setObjectName(u"remember_pw")

        self.horizontalLayout_5.addWidget(self.remember_pw)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.layoutWidget7 = QWidget(self.setting)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(1, 140, 661, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget7)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.layoutWidget7)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_3.addWidget(self.label_19)

        self.end_post_none = QRadioButton(self.layoutWidget7)
        self.end_post_none.setObjectName(u"end_post_none")

        self.horizontalLayout_3.addWidget(self.end_post_none)

        self.end_post_close_browser = QRadioButton(self.layoutWidget7)
        self.end_post_close_browser.setObjectName(u"end_post_close_browser")

        self.horizontalLayout_3.addWidget(self.end_post_close_browser)

        self.end_post_open_url = QRadioButton(self.layoutWidget7)
        self.end_post_open_url.setObjectName(u"end_post_open_url")

        self.horizontalLayout_3.addWidget(self.end_post_open_url)

        self.end_post_url = QLineEdit(self.layoutWidget7)
        self.end_post_url.setObjectName(u"end_post_url")

        self.horizontalLayout_3.addWidget(self.end_post_url)

        self.label_9 = QLabel(self.setting)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 5, 131, 31))
        self.wait_overtime = QLineEdit(self.setting)
        self.wait_overtime.setObjectName(u"wait_overtime")
        self.wait_overtime.setGeometry(QRect(275, 5, 51, 31))
        self.wait_overtime.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.setting, "")
        self.log_bar = QLabel(self.centralwidget)
        self.log_bar.setObjectName(u"log_bar")
        self.log_bar.setGeometry(QRect(5, 400, 660, 31))
        self.log_bar.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 671, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"facebook\u81ea\u52d5\u767c\u5e16\u5de5\u5177", None))
        ___qtablewidgetitem = self.group_table.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.group_table.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"name", None));
        self.all_select.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9078", None))
        self.reverse_select.setText(QCoreApplication.translate("MainWindow", u"\u53cd\u9078", None))
        self.cancel_select.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88\u9078\u64c7", None))
        self.copy_group_id.setText(QCoreApplication.translate("MainWindow", u"\u8907\u88fdid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.facebook_list), QCoreApplication.translate("MainWindow", u"\u7fa4\u7d44", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Group_id\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5e16\u5b50\u5167\u5bb9\uff1a", None))
        self.start_auto_post_group_button.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb\u767c\u5e16", None))
        self.chromedriver_location_choose.setText("")
        self.current_posting.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6aa2\u67e5\u5927\u7d04\u5e7e\u500b\u5e16\u6587\uff0c\u5982\u66fe\u767c\u904e\u5e16\u6587\u4e0d\u6703\u767c\u6b64\u7fa4\u7d44</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u700f\u89bd\u5668\uff1a", None))
        self.browser_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Chrome[\u6a21\u5f0f\u4e00]", None))
        self.browser_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Chrome[\u6a21\u5f0f\u4e8c]", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u700f\u89bd\u5668\u4f4d\u7f6e\uff1a", None))
        self.browser_location_choose.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"chromedriver\u4f4d\u7f6e\uff1a", None))
        self.get_chromedriver_url.setText(QCoreApplication.translate("MainWindow", u"\uff08\u4e0b\u8f09\uff09", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.auto_group_posting), QCoreApplication.translate("MainWindow", u"\u7fa4\u7d44\u81ea\u52d5\u767c\u5e16", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"token \uff1a", None))
        self.get_tokens_url.setText(QCoreApplication.translate("MainWindow", u"\uff08\u7372\u53d6token\uff09", None))
        self.language_switch.setItemText(0, QCoreApplication.translate("MainWindow", u"facebook\u8a9e\u8a00\uff1a", None))
        self.language_switch.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e2d\u6587(\u9999\u6e2f)", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"facebook\u96fb\u5b50\u90f5\u4ef6\u5730\u5740\uff1a", None))
        self.remember_email.setText(QCoreApplication.translate("MainWindow", u"\u8a18\u4f4f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"facebook\u5bc6\u78bc\uff1a", None))
        self.remember_pw.setText(QCoreApplication.translate("MainWindow", u"\u8a18\u4f4f", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u767c\u5e16\u5b8c\u6210\u5f8c\u52d5\u4f5c\uff1a", None))
        self.end_post_none.setText(QCoreApplication.translate("MainWindow", u"\u7121\u52d5\u4f5c", None))
        self.end_post_close_browser.setText(QCoreApplication.translate("MainWindow", u"\u95dc\u9589\u700f\u89bd\u5668", None))
        self.end_post_open_url.setText(QCoreApplication.translate("MainWindow", u"\u6253\u958b\u7db2\u5740\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u5019\u8d85\u6642\uff08\u79d2\uff09\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting), QCoreApplication.translate("MainWindow", u"\u8a2d\u5b9a", None))
        self.log_bar.setText("")
    # retranslateUi

