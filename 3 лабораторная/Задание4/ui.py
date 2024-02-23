# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 270, 81, 16))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 400, 239, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(680, 0, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 0, 171, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 520, 75, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 81, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(720, 530, 81, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        def hide_buttons():
            self.pushButton.setVisible(False)
            self.pushButton_2.setVisible(False)
            self.pushButton_3.setVisible(False)
            self.label_3.setText('')
            self.label_4.setText('')

        def computer_step():
            import random
            num = 3
            rock_num = self.label.text()
            rock = int(rock_num)
            if(rock == 2):
                num = 2
            elif(rock == 1):
                num = 1
            number = rock - num
            number = str(number)
            num = str(num)
            self.label.setText(number)
            self.label_3.setText(num)
            self.pushButton.setVisible(True)
            self.pushButton_2.setVisible(True)
            self.pushButton_3.setVisible(True)
            rock = int(number)
            self.label.setText('You Lose')
            self.label_4.setVisible(False)
            self.label_3.setVisible(False)


        def start_game():
            rock_num = self.lineEdit.text()
            self.pushButton.setVisible(True)
            self.pushButton_2.setVisible(True)
            self.pushButton_3.setVisible(True)
            self.pushButton_4.setVisible(False)
            self.label_2.setVisible(False)
            self.lineEdit.setVisible(False)
            self.label.setText(rock_num)

        def one_rock():
            rock_num = self.label.text()
            rock = int(rock_num)
            rock -= 1
            rock = str(rock)
            self.label_4.setText('1')
            self.label.setText(rock)
            self.pushButton.setVisible(False)
            self.pushButton_2.setVisible(False)
            self.pushButton_3.setVisible(False)
            rock = int(rock)
            if (rock <= 0):
                self.label.setText('You Win')
                self.label_4.setVisible(False)
                self.label_3.setVisible(False)
            if (rock > 0):
                computer_step()


        def two_rock():
            rock_num = self.label.text()
            rock = int(rock_num)
            rock -= 2
            rock = str(rock)
            self.label_4.setText('2')
            self.label.setText(rock)
            self.pushButton.setVisible(False)
            self.pushButton_2.setVisible(False)
            self.pushButton_3.setVisible(False)
            rock = int(rock)
            if (rock <= 0):
                self.label.setText('You Win')
                self.label_4.setVisible(False)
                self.label_3.setVisible(False)
            if (rock > 0):
                computer_step()

        def three_rock():
            rock_num = self.label.text()
            rock = int(rock_num)
            rock -= 3
            rock = str(rock)
            self.label_4.setText('3')
            self.label.setText(rock)
            self.pushButton.setVisible(False)
            self.pushButton_2.setVisible(False)
            self.pushButton_3.setVisible(False)
            rock = int(rock)
            if (rock <= 0):
                self.label.setText('You Win')
                self.label_4.setVisible(False)
                self.label_3.setVisible(False)
            if (rock > 0):
                computer_step()

        self.pushButton_4.clicked.connect(start_game)
        self.pushButton.clicked.connect(one_rock)
        self.pushButton_2.clicked.connect(two_rock)
        self.pushButton_3.clicked.connect(three_rock)

        self.retranslateUi(MainWindow)
        hide_buttons()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Камни"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.label_2.setText(_translate("MainWindow", "Колличество камней для игры"))
        self.pushButton_4.setText(_translate("MainWindow", "Выбрать"))
        self.label_3.setText(_translate("MainWindow", "Камни"))
        self.label_4.setText(_translate("MainWindow", "Камни"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
