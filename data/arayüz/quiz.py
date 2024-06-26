# Form implementation generated from reading ui file 'quiz.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_quiz(object):
    def setupUi(self, quiz):
        quiz.setObjectName("quiz")
        quiz.resize(520, 434)
        quiz.setStyleSheet("background-color: rgb(37, 38, 39);")
        quiz.setWindowIcon(QtGui.QIcon("data/icon.ico"))
        self.centralwidget = QtWidgets.QWidget(parent=quiz)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.secim3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.secim3.setMinimumSize(QtCore.QSize(164, 117))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secim3.setFont(font)
        self.secim3.setStyleSheet("background-color: rgb(242, 239, 233);\n"
"color: rgb(0, 0, 0);")
        self.secim3.setText("")
        self.secim3.setObjectName("secim3")
        self.gridLayout_2.addWidget(self.secim3, 1, 0, 1, 1)
        self.secim1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.secim1.setMinimumSize(QtCore.QSize(164, 117))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secim1.setFont(font)
        self.secim1.setStyleSheet("background-color: rgb(242, 239, 233);\n"
"color: rgb(0, 0, 0);")
        self.secim1.setText("")
        self.secim1.setObjectName("secim1")
        self.gridLayout_2.addWidget(self.secim1, 0, 0, 1, 1)
        self.secim4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.secim4.setEnabled(True)
        self.secim4.setMinimumSize(QtCore.QSize(164, 117))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secim4.setFont(font)
        self.secim4.setStyleSheet("background-color: rgb(242, 239, 233);\n"
"color: rgb(0, 0, 0);")
        self.secim4.setText("")
        self.secim4.setCheckable(False)
        self.secim4.setAutoDefault(False)
        self.secim4.setDefault(False)
        self.secim4.setFlat(False)
        self.secim4.setObjectName("secim4")
        self.gridLayout_2.addWidget(self.secim4, 1, 1, 1, 1)
        self.secim2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.secim2.setMinimumSize(QtCore.QSize(164, 117))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secim2.setFont(font)
        self.secim2.setStyleSheet("background-color: rgb(242, 239, 233);\n"
"color: rgb(0, 0, 0);")
        self.secim2.setText("")
        self.secim2.setObjectName("secim2")
        self.gridLayout_2.addWidget(self.secim2, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 3, 0, 2, 3)
        self.label_sira = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_sira.setMaximumSize(QtCore.QSize(50, 50))
        self.label_sira.setStyleSheet("color: rgb(144, 78, 85);")
        self.label_sira.setObjectName("label_sira")
        self.gridLayout.addWidget(self.label_sira, 0, 2, 1, 1)
        self.soru = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.soru.setFont(font)
        self.soru.setStyleSheet("color: rgb(255, 0, 0);")
        self.soru.setText("")
        self.soru.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.soru.setObjectName("soru")
        self.gridLayout.addWidget(self.soru, 2, 0, 1, 3)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(191, 180, 143);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        quiz.setCentralWidget(self.centralwidget)

        self.retranslateUi(quiz)
        QtCore.QMetaObject.connectSlotsByName(quiz)

    def retranslateUi(self, quiz):
        _translate = QtCore.QCoreApplication.translate
        quiz.setWindowTitle(_translate("quiz", "Sözlük App"))
        self.label_sira.setText(_translate("quiz", "1/10"))
        self.label.setText(_translate("quiz", "Quiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quiz = QtWidgets.QMainWindow()
    ui = Ui_quiz()
    ui.setupUi(quiz)
    quiz.show()
    sys.exit(app.exec())
