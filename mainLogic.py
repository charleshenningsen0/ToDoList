from PyQt6.QtWidgets import QApplication, QMainWindow
import csv


from gui import Ui_TODOLIST

from guiHistory import *

from historyLogic import *

import main
class mainLogic(QMainWindow, Ui_TODOLIST):
    mainIsOpen = True
    tasks = []
    doneButtons = []
    tasksIndex = 0
    def __init__(self):

        super().__init__()
        self.setupUi(self)


        #Task Label
        self.task1Label.setVisible(False)
        self.task2Label.setVisible(False)
        self.task3Label.setVisible(False)
        self.task4Label.setVisible(False)
        self.task5Label.setVisible(False)
        self.task6Label.setVisible(False)
        self.task7Label.setVisible(False)
        self.task8Label.setVisible(False)
        self.task9Label.setVisible(False)
        self.task10Label.setVisible(False)

        # adding taskLabels to list
        self.tasks.append(self.task1Label)
        self.tasks.append(self.task2Label)
        self.tasks.append(self.task3Label)
        self.tasks.append(self.task4Label)
        self.tasks.append(self.task5Label)
        self.tasks.append(self.task6Label)
        self.tasks.append(self.task7Label)
        self.tasks.append(self.task8Label)
        self.tasks.append(self.task9Label)
        self.tasks.append(self.task10Label)


        #done buttons
        self.doneButton1.setVisible(False)
        self.doneButton2.setVisible(False)
        self.doneButton3.setVisible(False)
        self.doneButton4.setVisible(False)
        self.doneButton5.setVisible(False)
        self.doneButton6.setVisible(False)
        self.doneButton7.setVisible(False)
        self.doneButton8.setVisible(False)
        self.doneButton9.setVisible(False)
        self.doneButton10.setVisible(False)

        #adding done buttons to list
        self.doneButtons.append(self.doneButton1)
        self.doneButtons.append(self.doneButton2)
        self.doneButtons.append(self.doneButton3)
        self.doneButtons.append(self.doneButton4)
        self.doneButtons.append(self.doneButton5)
        self.doneButtons.append(self.doneButton6)
        self.doneButtons.append(self.doneButton7)
        self.doneButtons.append(self.doneButton8)
        self.doneButtons.append(self.doneButton9)
        self.doneButtons.append(self.doneButton10)







        #eddit buttons might remove
        self.task1EditButton.setVisible(False)
        self.task2EditButton.setVisible(False)
        self.task3EditButton.setVisible(False)
        self.task4EditButton.setVisible(False)
        self.task5EditButton.setVisible(False)
        self.task6EditButton.setVisible(False)
        self.task7EditButton.setVisible(False)
        self.task8EditButton.setVisible(False)
        self.task9EditButton.setVisible(False)
        self.task10EditButton.setVisible(False)
        self.lineEdit1.setVisible(False)
        self.lineEdit2.setVisible(False)
        self.lineEdit3.setVisible(False)
        self.lineEdit4.setVisible(False)
        self.lineEdit5.setVisible(False)
        self.lineEdit6.setVisible(False)
        self.lineEdit7.setVisible(False)
        self.lineEdit8.setVisible(False)
        self.lineEdit9.setVisible(False)
        self.lineEdit10.setVisible(False)

        self.task1EditButton.clicked.connect(lambda : self.editTask())
        self.task2EditButton.clicked.connect(lambda: self.editTask())
        self.task3EditButton.clicked.connect(lambda: self.editTask())
        self.task4EditButton.clicked.connect(lambda: self.editTask())
        self.task5EditButton.clicked.connect(lambda: self.editTask())
        self.task6EditButton.clicked.connect(lambda: self.editTask())
        self.task7EditButton.clicked.connect(lambda: self.editTask())
        self.task8EditButton.clicked.connect(lambda: self.editTask())
        self.task9EditButton.clicked.connect(lambda: self.editTask())
        self.task10EditButton.clicked.connect(lambda: self.editTask())


        self.doneButton1.clicked.connect(lambda: self.completeTask(0))
        self.doneButton2.clicked.connect(lambda: self.completeTask(1))
        self.doneButton3.clicked.connect(lambda: self.completeTask(2))
        self.doneButton4.clicked.connect(lambda: self.completeTask(3))
        self.doneButton5.clicked.connect(lambda: self.completeTask(4))
        self.doneButton6.clicked.connect(lambda: self.completeTask(5))
        self.doneButton7.clicked.connect(lambda: self.completeTask(6))
        self.doneButton8.clicked.connect(lambda: self.completeTask(7))
        self.doneButton9.clicked.connect(lambda: self.completeTask(8))
        self.doneButton10.clicked.connect(lambda: self.completeTask(9))


        self.addTaskButton.clicked.connect(lambda : self.addTask())


        self.HistoryWindowButton.clicked.connect(lambda : self.openHistory())


#creating a complete task event for each done button!!!


    def completeTask(self, index):
        self.addTasklabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.addTasklabel.setText("Enter a task!")

        if self.tasksIndex - 1 == index:
            self.tasks[index].setText("")
            self.doneButtons[index].setVisible(False)
        else:
            for i in range(index, self.tasksIndex - 1):
                self.tasks[i].setText(self.tasks[i + 1].text())

        self.tasks[self.tasksIndex - 1].setText("")
        self.doneButtons[self.tasksIndex - 1].setVisible(False)

        self.tasksIndex -= 1

    # for clear button have pop or cheering sound


    def openHistory(self):

        geometry = self.geometry()

        self.historyWindow = historyLogic()
        self.historyWindow.setGeometry(geometry)
        self.historyWindow.show()
        self.close()

    def editTask(self):
        pass
        #Maybe actually pass on this, focus on checking off tasks and adding multiple tasks

    def addTask(self):

        try:
            task = self.addTasklineEdit.text()
            if task == '':
                raise TypeError
            self.tasks[self.tasksIndex].setText(task)
            self.tasks[self.tasksIndex].setVisible(True)
            self.doneButtons[self.tasksIndex].setVisible(True)
        except TypeError:
            self.addTasklabel.setText("Enter a valid task!")
        except IndexError:
            #Catches if there are 10 tasks already, tells user too many tasks
            self.addTasklabel.setText("You have to many tasks!")
            self.addTasklabel.setStyleSheet("color: rgb(255, 0, 0);")
            self.addTasklineEdit.setText("")
        else:
            ######

            with open('tasksFile.txt', "a") as taskFile:
                # csv_writer = csv.writer(taskFile)
                # csv_writer.writerow(task)
                #maybe add time completed, or time added to file/created
                taskFile.write(task + '\n')

            self.addTasklineEdit.setText("")
            self.tasksIndex += 1
            print(self.tasksIndex)









