from PyQt6.QtWidgets import QApplication, QMainWindow

import sys

from gui import Ui_MainWindow

from guiHistory import Ui_Form


class Logic(QMainWindow, Ui_MainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit1.setVisible(False)
        self.textEdit2.setVisible(False)
        self.textEdit3.setVisible(False)
        self.textEdit4.setVisible(False)
        self.textEdit5.setVisible(False)
        self.textEdit6.setVisible(False)
        self.textEdit7.setVisible(False)
        self.textEdit8.setVisible(False)

        self.task1Label.setVisible(False)
        self.task2Label.setVisible(False)
        self.task3Label.setVisible(False)
        self.task4Label.setVisible(False)
        self.task5Label.setVisible(False)
        self.task6Label.setVisible(False)
        self.task7Label.setVisible(False)
        self.task8Label.setVisible(False)


        self.task1EditButton.setVisible(False)
        self.task2EditButton.setVisible(False)
        self.task3EditButton.setVisible(False)
        self.task4EditButton.setVisible(False)
        self.task5EditButton.setVisible(False)
        self.task6EditButton.setVisible(False)
        self.task7EditButton.setVisible(False)
        self.task8EditButton.setVisible(False)

        self.task1EditButton.clicked.connect(lambda : self.editTask())
        self.task2EditButton.clicked.connect(lambda: self.editTask())
        self.task3EditButton.clicked.connect(lambda: self.editTask())
        self.task4EditButton.clicked.connect(lambda: self.editTask())
        self.task5EditButton.clicked.connect(lambda: self.editTask())
        self.task6EditButton.clicked.connect(lambda: self.editTask())
        self.task7EditButton.clicked.connect(lambda: self.editTask())
        self.task8EditButton.clicked.connect(lambda: self.editTask())

        #If text == edit, show textentry and switch button text to save.
        # if text == save, save text entry to task, and clear and hide text entry and switch button
        # text to edit

        #CREAT NEW LABELS/buttons for the new tasks

        self.addTaskButton.clicked.connect(lambda : self.addTask())

        #Check boxes

        self.HistoryWindowButton.clicked.connect(lambda : self.openHistory())





        #for clear button have pop


    def openHistory(self):
        self.Ui_Form.setupUi(self.show())

    def editTask(self):
        pass

    def addTask(self):
        pass


