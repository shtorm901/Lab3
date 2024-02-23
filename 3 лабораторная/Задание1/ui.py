from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(310, 50, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 10, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 100, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_2.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(540, 190, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_7 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_3)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_3.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_3)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_3.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(parent=self.verticalLayoutWidget_3)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout_3.addWidget(self.radioButton_9)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 410, 75, 24))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def paint():
            if self.radioButton.isChecked():
                color = 1
                Label1Red()
            elif self.radioButton_2.isChecked():
                color = 2
                Label1Green()
            elif self.radioButton_3.isChecked():
                color = 3
                Label1Blue()

            if self.radioButton_4.isChecked():
                color2 = 1
                Label2Red()
            elif self.radioButton_5.isChecked():
                color2 = 2
                Label2Green()
            elif self.radioButton_6.isChecked():
                color2 = 3
                Label2Blue()

            if self.radioButton_7.isChecked():
                color3 = 1
                Label3Red()
            elif self.radioButton_8.isChecked():
                color3 = 2
                Label3Green()
            elif self.radioButton_9.isChecked():
                color3 = 3
                Label3Blue()

        def Label1Red():
            self.label_2.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 0, 0)\n"
"}")

        def Label1Blue():
            self.label_2.setStyleSheet("QLabel{\n"
"background-color:rgb(0, 0, 255)\n"
"}")

        def Label1Green():
            self.label_2.setStyleSheet("QLabel{\n"
"background-color:rgb(0, 255, 0)\n"
"}")

        def Label2Red():
            self.label.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 0, 0)\n"
"}")

        def Label2Blue():
            self.label.setStyleSheet("QLabel{\n"
"background-color:rgb(0, 0, 255)\n"
"}")

        def Label2Green():
            self.label.setStyleSheet("QLabel{\n"
"background-color:rgb(0, 255, 0)\n"
"}")

        def Label3Red():
            self.label_3.setStyleSheet("QLabel{\n"
"background-color:rgb(255, 0, 0)\n"
"}")

        def Label3Blue():
            self.label_3.setStyleSheet("QLabel{\n"
"background-color:rgb(0, 0, 255)\n"
"}")

        def Label3Green():
            self.label_3.setStyleSheet("QLabel{\n"
"background-color:rgb(0, 255, 0)\n"
"}")


        self.pushButton.clicked.connect(paint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Red1"))
        self.radioButton_2.setText(_translate("MainWindow", "Green1"))
        self.radioButton_3.setText(_translate("MainWindow", "Blue1"))
        self.radioButton_4.setText(_translate("MainWindow", "Red2"))
        self.radioButton_5.setText(_translate("MainWindow", "Green2"))
        self.radioButton_6.setText(_translate("MainWindow", "Blue2"))
        self.radioButton_7.setText(_translate("MainWindow", "Red3"))
        self.radioButton_8.setText(_translate("MainWindow", "Green3"))
        self.radioButton_9.setText(_translate("MainWindow", "Blue3"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
