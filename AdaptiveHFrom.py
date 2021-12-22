from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 589)
        font = QtGui.QFont()
        font.setPointSize(14)
        Form.setFont(font)
        Form.setStyleSheet("color: white;\n"
"background-color: rgb(245, 245, 245)")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(450, 440, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 35px;\n"
"font-family: Helvetica;\n"
"font-size: 20px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 160, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStatusTip("")
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 35px;\n"
"font-family: Helvetica;\n"
"font-size: 20px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 280, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(-1)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 35px;\n"
"font-family: Helvetica;\n"
"font-size: 20px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 440, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(-1)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(232, 232, 232);\n"
"border-radius: 35px;\n"
"font-family: Helvetica;\n"
"font-size: 20px")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 831, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("text-align: center;\n"
"color: rgb(239, 239, 239);\n"
"background-color: rgb(47, 47, 47);\n"
"font-family: Helvetica;")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Адаптивный алгоритм Хаффмана"))
        self.pushButton.setText(_translate("Form", "Разжатие"))
        self.pushButton_2.setText(_translate("Form", "Файлы"))
        self.pushButton_3.setText(_translate("Form", "Каталог для результата"))
        self.pushButton_4.setText(_translate("Form", "Сжатие"))
        self.label_2.setText(_translate("Form", "                       Сжатие данных адаптивным алгоритмом Хаффмана"))

