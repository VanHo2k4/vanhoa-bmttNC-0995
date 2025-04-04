# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_btn_encrypt(object):
    def setupUi(self, btn_encrypt):
        btn_encrypt.setObjectName("btn_encrypt")
        btn_encrypt.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(btn_encrypt)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(110, 100, 621, 91))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txt_key = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(110, 230, 621, 41))
        self.txt_key.setObjectName("txt_key")
        self.txt_cipher_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cipher_text.setGeometry(QtCore.QRect(110, 310, 621, 101))
        self.txt_cipher_text.setObjectName("txt_cipher_text")
        self.btn_encrypt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt_2.setGeometry(QtCore.QRect(220, 450, 91, 51))
        self.btn_encrypt_2.setObjectName("btn_encrypt_2")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(510, 450, 91, 51))
        self.btn_decrypt.setObjectName("btn_decrypt")
        btn_encrypt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(btn_encrypt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        btn_encrypt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(btn_encrypt)
        self.statusbar.setObjectName("statusbar")
        btn_encrypt.setStatusBar(self.statusbar)

        self.retranslateUi(btn_encrypt)
        QtCore.QMetaObject.connectSlotsByName(btn_encrypt)

    def retranslateUi(self, btn_encrypt):
        _translate = QtCore.QCoreApplication.translate
        btn_encrypt.setWindowTitle(_translate("btn_encrypt", "MainWindow"))
        self.label.setText(_translate("btn_encrypt", "CAESAR CIPHER"))
        self.label_2.setText(_translate("btn_encrypt", "Plain Text:"))
        self.label_3.setText(_translate("btn_encrypt", "Key:"))
        self.label_4.setText(_translate("btn_encrypt", "CipherText:"))
        self.btn_encrypt_2.setText(_translate("btn_encrypt", "Encrypt"))
        self.btn_decrypt.setText(_translate("btn_encrypt", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    btn_encrypt = QtWidgets.QMainWindow()
    ui = Ui_btn_encrypt()
    ui.setupUi(btn_encrypt)
    btn_encrypt.show()
    sys.exit(app.exec_())
