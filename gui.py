# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TODOLIST(object):
    def setupUi(self, TODOLIST):
        TODOLIST.setObjectName("TODOLIST")
        TODOLIST.resize(871, 760)
        TODOLIST.setMinimumSize(QtCore.QSize(800, 760))
        self.centralwidget = QtWidgets.QWidget(parent=TODOLIST)
        self.centralwidget.setObjectName("centralwidget")
        self.addTaskFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.addTaskFrame.setGeometry(QtCore.QRect(60, 10, 691, 61))
        self.addTaskFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.addTaskFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.addTaskFrame.setObjectName("addTaskFrame")
        self.addTaskButton = QtWidgets.QPushButton(parent=self.addTaskFrame)
        self.addTaskButton.setGeometry(QtCore.QRect(140, 10, 113, 32))
        self.addTaskButton.setObjectName("addTaskButton")
        self.addTasklabel = QtWidgets.QLabel(parent=self.addTaskFrame)
        self.addTasklabel.setGeometry(QtCore.QRect(500, 20, 151, 16))
        self.addTasklabel.setObjectName("addTasklabel")
        self.addTasklineEdit = QtWidgets.QLineEdit(parent=self.addTaskFrame)
        self.addTasklineEdit.setGeometry(QtCore.QRect(260, 10, 211, 31))
        self.addTasklineEdit.setObjectName("addTasklineEdit")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 90, 841, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.task5Label = QtWidgets.QLabel(parent=self.frame)
        self.task5Label.setGeometry(QtCore.QRect(100, 220, 400, 30))
        self.task5Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task5Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task5Label.setFont(font)
        self.task5Label.setLineWidth(13)
        self.task5Label.setObjectName("task5Label")
        self.task1EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task1EditButton.setGeometry(QtCore.QRect(500, 60, 71, 32))
        self.task1EditButton.setObjectName("task1EditButton")
        self.task1Label = QtWidgets.QLabel(parent=self.frame)
        self.task1Label.setGeometry(QtCore.QRect(100, 60, 400, 30))
        self.task1Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task1Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task1Label.setFont(font)
        self.task1Label.setLineWidth(13)
        self.task1Label.setObjectName("task1Label")
        self.task8Label = QtWidgets.QLabel(parent=self.frame)
        self.task8Label.setGeometry(QtCore.QRect(100, 340, 400, 30))
        self.task8Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task8Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task8Label.setFont(font)
        self.task8Label.setLineWidth(13)
        self.task8Label.setObjectName("task8Label")
        self.task4EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task4EditButton.setGeometry(QtCore.QRect(500, 180, 71, 32))
        self.task4EditButton.setObjectName("task4EditButton")
        self.task3EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task3EditButton.setGeometry(QtCore.QRect(500, 140, 71, 32))
        self.task3EditButton.setObjectName("task3EditButton")
        self.task8EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task8EditButton.setGeometry(QtCore.QRect(500, 340, 71, 32))
        self.task8EditButton.setObjectName("task8EditButton")
        self.task6Label = QtWidgets.QLabel(parent=self.frame)
        self.task6Label.setGeometry(QtCore.QRect(100, 260, 400, 30))
        self.task6Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task6Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task6Label.setFont(font)
        self.task6Label.setLineWidth(13)
        self.task6Label.setObjectName("task6Label")
        self.task6EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task6EditButton.setGeometry(QtCore.QRect(500, 260, 71, 32))
        self.task6EditButton.setObjectName("task6EditButton")
        self.task3Label = QtWidgets.QLabel(parent=self.frame)
        self.task3Label.setGeometry(QtCore.QRect(100, 140, 400, 30))
        self.task3Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task3Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task3Label.setFont(font)
        self.task3Label.setLineWidth(13)
        self.task3Label.setObjectName("task3Label")
        self.task4Label = QtWidgets.QLabel(parent=self.frame)
        self.task4Label.setGeometry(QtCore.QRect(100, 180, 400, 30))
        self.task4Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task4Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task4Label.setFont(font)
        self.task4Label.setLineWidth(13)
        self.task4Label.setObjectName("task4Label")
        self.task5EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task5EditButton.setGeometry(QtCore.QRect(500, 220, 71, 32))
        self.task5EditButton.setObjectName("task5EditButton")
        self.task7EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task7EditButton.setGeometry(QtCore.QRect(500, 300, 71, 32))
        self.task7EditButton.setObjectName("task7EditButton")
        self.task7Label = QtWidgets.QLabel(parent=self.frame)
        self.task7Label.setGeometry(QtCore.QRect(100, 300, 400, 30))
        self.task7Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task7Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task7Label.setFont(font)
        self.task7Label.setLineWidth(13)
        self.task7Label.setObjectName("task7Label")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("PT Mono")
        font.setPointSize(30)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.task2Label = QtWidgets.QLabel(parent=self.frame)
        self.task2Label.setGeometry(QtCore.QRect(100, 100, 400, 30))
        self.task2Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task2Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task2Label.setFont(font)
        self.task2Label.setLineWidth(13)
        self.task2Label.setObjectName("task2Label")
        self.task2EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task2EditButton.setGeometry(QtCore.QRect(500, 100, 71, 32))
        self.task2EditButton.setObjectName("task2EditButton")
        self.lineEdit1 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit1.setGeometry(QtCore.QRect(640, 60, 181, 31))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit3.setGeometry(QtCore.QRect(640, 100, 181, 31))
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit4.setGeometry(QtCore.QRect(640, 140, 181, 31))
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit5 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit5.setGeometry(QtCore.QRect(640, 180, 181, 31))
        self.lineEdit5.setObjectName("lineEdit5")
        self.lineEdit6 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit6.setGeometry(QtCore.QRect(640, 220, 181, 31))
        self.lineEdit6.setObjectName("lineEdit6")
        self.lineEdit7 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit7.setGeometry(QtCore.QRect(640, 260, 181, 31))
        self.lineEdit7.setObjectName("lineEdit7")
        self.lineEdit8 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit8.setGeometry(QtCore.QRect(640, 300, 181, 31))
        self.lineEdit8.setObjectName("lineEdit8")
        self.lineEdit9 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit9.setGeometry(QtCore.QRect(640, 340, 181, 31))
        self.lineEdit9.setObjectName("lineEdit9")
        self.lineEdit10 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit10.setGeometry(QtCore.QRect(640, 420, 181, 31))
        self.lineEdit10.setObjectName("lineEdit10")
        self.lineEdit2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit2.setGeometry(QtCore.QRect(640, 380, 181, 31))
        self.lineEdit2.setObjectName("lineEdit2")
        self.task10Label = QtWidgets.QLabel(parent=self.frame)
        self.task10Label.setGeometry(QtCore.QRect(100, 420, 400, 30))
        self.task10Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task10Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task10Label.setFont(font)
        self.task10Label.setLineWidth(13)
        self.task10Label.setObjectName("task10Label")
        self.task10EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task10EditButton.setGeometry(QtCore.QRect(500, 420, 71, 32))
        self.task10EditButton.setObjectName("task10EditButton")
        self.task9Label = QtWidgets.QLabel(parent=self.frame)
        self.task9Label.setGeometry(QtCore.QRect(100, 380, 400, 30))
        self.task9Label.setMinimumSize(QtCore.QSize(400, 30))
        self.task9Label.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.task9Label.setFont(font)
        self.task9Label.setLineWidth(13)
        self.task9Label.setObjectName("task9Label")
        self.task9EditButton = QtWidgets.QPushButton(parent=self.frame)
        self.task9EditButton.setGeometry(QtCore.QRect(500, 380, 71, 32))
        self.task9EditButton.setObjectName("task9EditButton")
        self.doneButton1 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton1.setGeometry(QtCore.QRect(10, 60, 81, 31))
        self.doneButton1.setObjectName("doneButton1")
        self.doneButton2 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton2.setGeometry(QtCore.QRect(10, 100, 81, 31))
        self.doneButton2.setObjectName("doneButton2")
        self.doneButton3 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton3.setGeometry(QtCore.QRect(10, 140, 81, 31))
        self.doneButton3.setObjectName("doneButton3")
        self.doneButton4 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton4.setGeometry(QtCore.QRect(10, 180, 81, 31))
        self.doneButton4.setObjectName("doneButton4")
        self.doneButton5 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton5.setGeometry(QtCore.QRect(10, 220, 81, 31))
        self.doneButton5.setObjectName("doneButton5")
        self.doneButton9 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton9.setGeometry(QtCore.QRect(10, 380, 81, 31))
        self.doneButton9.setObjectName("doneButton9")
        self.doneButton10 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton10.setGeometry(QtCore.QRect(10, 420, 81, 31))
        self.doneButton10.setObjectName("doneButton10")
        self.doneButton8 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton8.setGeometry(QtCore.QRect(10, 340, 81, 31))
        self.doneButton8.setObjectName("doneButton8")
        self.doneButton6 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton6.setGeometry(QtCore.QRect(10, 260, 81, 31))
        self.doneButton6.setObjectName("doneButton6")
        self.doneButton7 = QtWidgets.QPushButton(parent=self.frame)
        self.doneButton7.setGeometry(QtCore.QRect(10, 300, 81, 31))
        self.doneButton7.setObjectName("doneButton7")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 600, 561, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(110, 650, 151, 16))
        self.progressLabel.setObjectName("progressLabel")
        self.HistoryWindowButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.HistoryWindowButton.setGeometry(QtCore.QRect(720, 640, 113, 32))
        self.HistoryWindowButton.setObjectName("HistoryWindowButton")
        TODOLIST.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=TODOLIST)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 43))
        self.menubar.setObjectName("menubar")
        self.menuWelcome_to_Remindr = QtWidgets.QMenu(parent=self.menubar)
        self.menuWelcome_to_Remindr.setObjectName("menuWelcome_to_Remindr")
        TODOLIST.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=TODOLIST)
        self.statusbar.setObjectName("statusbar")
        TODOLIST.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuWelcome_to_Remindr.menuAction())

        self.retranslateUi(TODOLIST)
        QtCore.QMetaObject.connectSlotsByName(TODOLIST)

    def retranslateUi(self, TODOLIST):
        _translate = QtCore.QCoreApplication.translate
        TODOLIST.setWindowTitle(_translate("TODOLIST", "Home"))
        self.addTaskButton.setText(_translate("TODOLIST", "Add Task"))
        self.addTasklabel.setText(_translate("TODOLIST", "Enter a task!"))
        self.task5Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task1EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task1Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task8Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task4EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task3EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task8EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task6Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task6EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task3Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task4Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task5EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task7EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task7Label.setText(_translate("TODOLIST", "TextLabel"))
        self.label.setText(_translate("TODOLIST", "Tasks"))
        self.task2Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task2EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task10Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task10EditButton.setText(_translate("TODOLIST", "Edit"))
        self.task9Label.setText(_translate("TODOLIST", "TextLabel"))
        self.task9EditButton.setText(_translate("TODOLIST", "Edit"))
        self.doneButton1.setText(_translate("TODOLIST", "Done"))
        self.doneButton2.setText(_translate("TODOLIST", "Done"))
        self.doneButton3.setText(_translate("TODOLIST", "Done"))
        self.doneButton4.setText(_translate("TODOLIST", "Done"))
        self.doneButton5.setText(_translate("TODOLIST", "Done"))
        self.doneButton9.setText(_translate("TODOLIST", "Done"))
        self.doneButton10.setText(_translate("TODOLIST", "Done"))
        self.doneButton8.setText(_translate("TODOLIST", "Done"))
        self.doneButton6.setText(_translate("TODOLIST", "Done"))
        self.doneButton7.setText(_translate("TODOLIST", "Done"))
        self.progressLabel.setText(_translate("TODOLIST", "Progress"))
        self.HistoryWindowButton.setText(_translate("TODOLIST", "History"))
        self.menuWelcome_to_Remindr.setTitle(_translate("TODOLIST", "Welcome to Remindr"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TODOLIST = QtWidgets.QMainWindow()
    ui = Ui_TODOLIST()
    ui.setupUi(TODOLIST)
    TODOLIST.show()
    sys.exit(app.exec())
