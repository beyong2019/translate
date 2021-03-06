# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/translate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtWidgets
from controller.translator import translator


class UiMainWindow(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("小冰翻译")
        main_window.resize(800, 600)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(340, 20, 120, 34))
        self.label.setStyleSheet("background-color: rgb(170, 255, 0);")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.central_widget)
        self.widget.setGeometry(QtCore.QRect(40, 60, 741, 431))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 4, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 4, 0, 1, 3)
        main_window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.translation_connect)

        self.renew_translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translation_connect(self):
        content = self.textEdit.toPlainText()
        st = translator(content)
        self.textEdit_2.setText(st['trans_result'][0]['dst'])

    def renew_translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" "
                                                    "font-size:18pt;\">小冰翻译</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "              翻译结果"))
        self.pushButton.setText(_translate("MainWindow", "点击翻译"))
        self.label_2.setText(_translate("MainWindow", "输入翻译内容（自动检测语言）"))
        self.label_4.setText(_translate("MainWindow", " 英汉互译"))
