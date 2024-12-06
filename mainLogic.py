from PyQt6.QtWidgets import QApplication, QMainWindow
import csv
import re
import os
from gui import Ui_TODOLIST
from guiHistory import *
from historyLogic import *
#TODO Type hinting!cand Docstrings!
import main

#https://www.google.com/search?client=safari&rls=en&q=how+to+use+custom+exceptions+in+python&ie=UTF-8&oe=UTF-8
class DuplicateError(Exception):
    def __init__(self,message):
        self.message = message


class mainLogic(QMainWindow, Ui_TODOLIST):
    mainIsOpen = True
    editButtons = []
    editLines = []
    tasks = []
    doneButtons = []
    tasksIndex = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #after visible or before, then set the labels to previous labels.If label doesnt exist, set to invisible
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



        #eddit buttons
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

        #adding buttons to list
        self.editButtons.append(self.task1EditButton)
        self.editButtons.append(self.task2EditButton)
        self.editButtons.append(self.task3EditButton)
        self.editButtons.append(self.task4EditButton)
        self.editButtons.append(self.task5EditButton)
        self.editButtons.append(self.task6EditButton)
        self.editButtons.append(self.task7EditButton)
        self.editButtons.append(self.task8EditButton)
        self.editButtons.append(self.task9EditButton)
        self.editButtons.append(self.task10EditButton)

        #edit lines
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

        #adding edit lines to list
        self.editLines.append(self.lineEdit1)
        self.editLines.append(self.lineEdit2)
        self.editLines.append(self.lineEdit3)
        self.editLines.append(self.lineEdit4)
        self.editLines.append(self.lineEdit5)
        self.editLines.append(self.lineEdit6)
        self.editLines.append(self.lineEdit7)
        self.editLines.append(self.lineEdit8)
        self.editLines.append(self.lineEdit9)
        self.editLines.append(self.lineEdit10)


        #see if you can merge pop up to main
        #if taskfile.txt exists
        #Open file, read lines, pop out compleded tasks, then if length of new lsit is > 10, for i in ragne(len(lines)-10, len(line): add task to task labels
        # else for len of new list, add to text labels #Swithc to csv

        if os.path.exists("tasksFile.txt"):
        # if True:
        #     print("exists")
            with open("tasksFile.txt", "r") as file:
                lines = file.readlines()
        # print(lines)
            uncompletedTasks = []
            RegExCompletedTask = "^.*True\n$"
            for line in lines:
                if not re.search(RegExCompletedTask, line):
                    uncompletedTasks.append(line)
            # print(uncompletedTasks)

            if len(uncompletedTasks) == 0:
                pass
            #nothing
            # print(len(lines))

            for i in range(len(uncompletedTasks)):
                    self.tasks[i].setVisible(True)
                    self.doneButtons[i].setVisible(True)
                    self.editButtons[i].setVisible(True)
                    text = uncompletedTasks[i].strip('###False\n')
                    # print(text)

                    self.tasks[i].setText(text)
                    self.tasksIndex = len(uncompletedTasks)


        self.task1EditButton.clicked.connect(lambda : self.editTask(0))
        self.task2EditButton.clicked.connect(lambda: self.editTask(1))
        self.task3EditButton.clicked.connect(lambda: self.editTask(2))
        self.task4EditButton.clicked.connect(lambda: self.editTask(3))
        self.task5EditButton.clicked.connect(lambda: self.editTask(4))
        self.task6EditButton.clicked.connect(lambda: self.editTask(5))
        self.task7EditButton.clicked.connect(lambda: self.editTask(6))
        self.task8EditButton.clicked.connect(lambda: self.editTask(7))
        self.task9EditButton.clicked.connect(lambda: self.editTask(8))
        self.task10EditButton.clicked.connect(lambda: self.editTask(9))


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

    #need to add completed task to completed task file for history
    #remove task from current tasks, appdend end,
    # nd in history display form bottom up so completed are at the top

    #Author: "Google AI"
    #Title: "Overview"
    #Date: 12/04/24
    #Location: https://www.google.com/search?q=how+to+remove+a+row+from+a+text+file+in+python+with+regex+in+a+loop&client=safari&sca_esv=fdf7728f28b59cda&rls=en&sxsrf=ADLYWILL1TOQsrtEtcCGjoPIB1TlEBccJw%3A1733342337619&ei=gbRQZ__DJez_ptQP8-3juQQ&ved=0ahUKEwi_iLuy846KAxXsv4kEHfP2OEcQ4dUDCA8&uact=5&oq=how+to+remove+a+row+from+a+text+file+in+python+with+regex+in+a+loop&gs_lp=Egxnd3Mtd2l6LXNlcnAiQ2hvdyB0byByZW1vdmUgYSByb3cgZnJvbSBhIHRleHQgZmlsZSBpbiBweXRob24gd2l0aCByZWdleCBpbiBhIGxvb3BI_zRQiBhYojNwAngBkAEBmAGfAaABuBGqAQQ5LjEzuAEDyAEA-AEBmAIPoAKODMICChAAGLADGNYEGEfCAgUQIRigAcICBRAhGKsCmAMAiAYBkAYIkgcENS4xMKAH3k0&sclient=gws-wiz-serp

    def completeTask(self, index):
        #maybe use task ID instead so you can habe the same name of task
        self.addTasklabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.addTasklabel.setText("Enter a task!")
        #look through tasks, find task completed, and modify completed to true
        with open("tasksFile.txt", "r") as file:
            lines = file.readlines()



        regExTask = f"^{self.tasks[index].text()}###"


        with open("tasksFile.txt", "w") as file:
            for line in lines:
                if not re.search(regExTask, line):
                    file.write(line)
            file.write(f"{self.tasks[index].text()}###{True}\n")

        if self.tasksIndex - 1 == index:
            self.tasks[index].setText("")
            self.doneButtons[index].setVisible(False)
            self.editButtons[index].setVisible(False)

        else:
            for i in range(index, self.tasksIndex - 1):
                self.tasks[i].setText(self.tasks[i + 1].text())

        self.tasks[self.tasksIndex - 1].setText("")
        self.doneButtons[self.tasksIndex - 1].setVisible(False)
        self.editButtons[self.tasksIndex- 1].setVisible(False)

        self.tasksIndex -= 1

    # for clear button have pop or cheering sound
    #Try to just have a popup for the history!
    #need to add current tasks file and when init, insert current task file,
    def openHistory(self):
        #need to retrieve the tasks in a file, when switching from history to home
        geometry = self.geometry()
        self.historyWindow = historyLogic()
        self.historyWindow.setGeometry(geometry)
        self.historyWindow.show()

    #Lets try two differtn things, exception handling separate,
    #TODO: Change in file!!! freeze other buttons
    def editTask(self, index):

        if self.editButtons[index].text() == "Edit":
            #disable other buttons .setEnabled(False)
            self.editLines[index].setVisible(True)
            self.editButtons[index].setText("Confirm")

            #Disable all other buttons
            self.addTaskButton.setEnabled(False)
            for i in range(9):
                self.doneButtons[i].setEnabled(False)

            for i in range(9):
                if i != index:
                    self.editButtons[i].setEnabled(False)






            #do the exceptopn handling, Maybe do while something try ???



        else:
            try:
                task = self.editLines[index].text()
                if task == '':
                    raise TypeError
                if os.path.exists("tasksFile.txt"):
                    with open('tasksFile.txt', 'r') as file:
                        lines = file.readlines()
                    for line in lines:
                        if re.search(f'^{task}###False', line):
                            raise DuplicateError("Cannot add duplicate task")
            except TypeError:
                self.editLines[index].setText("")
                self.addTasklabel.setText("Enter a valid task!")
                self.addTasklabel.setStyleSheet("color: rgb(255, 0, 0);")

            except DuplicateError as e:
                self.editLines[index].setText("")
                self.addTasklabel.setText(e.message)
                self.addTasklabel.setStyleSheet("color: rgb(255, 0, 0);")
            else:

                print(task)
                print(self.tasks[index].text())
            # self.addTask(task, True)
            #add the text to indexask line and to file!
                # editedLines = []
                with open("tasksFile.txt", "r") as file:
                    lines = file.readlines()
                # for line in lines:
                #     if re.search(f'^{self.tasks[index].text()}###False', line):
                #         editedLines.append([f"^{task}###False"])
                #     else:
                #         editedLines.append(line)
                # print(editedLines)
                print(lines)
                with open("tasksFile.txt", "w") as file:
                    for line in lines:
                        print(line)
                        if re.search(f'^{self.tasks[index].text()}###False', line):
                            print("found")
                            file.write(f"{task}###False\n")
                        else:
                            file.write(line)

                self.addTaskButton.setEnabled(True)
                for i in range(9):
                    self.doneButtons[i].setEnabled(True)

                for i in range(9):
                    if i != index:
                        self.editButtons[i].setEnabled(True)


                self.tasks[index].setText(task)
                self.editButtons[index].setText("Edit")
                self.editLines[index].setText("")
                self.editLines[index].setVisible(False)
                self.addTasklabel.setText("Enter a task!")
                self.addTasklabel.setStyleSheet("color: rgb(255, 255, 255);")

                #Enabling other buttons





    def addTask(self):
        try:
            task = self.addTasklineEdit.text()
            if task == '':
                raise TypeError

            if os.path.exists("tasksFile.txt"):
                with open('tasksFile.txt', 'r') as file:
                    lines = file.readlines()
                for line in lines:
                    if re.search(f'^{task}###False', line):
                        raise DuplicateError("Cannot add duplicate task")


            self.tasks[self.tasksIndex].setText(task)
            self.tasks[self.tasksIndex].setVisible(True)
            self.editButtons[self.tasksIndex].setVisible(True)
            self.doneButtons[self.tasksIndex].setVisible(True)


        except TypeError:
            self.addTasklabel.setText("Enter a valid task!")
            self.addTasklabel.setStyleSheet("color: rgb(255, 0, 0);")

        except IndexError:
            #Catches if there are 10 tasks already, tells user too many tasks
            self.addTasklabel.setText("You have to many tasks!")
            self.addTasklabel.setStyleSheet("color: rgb(255, 0, 0);")
            self.addTasklineEdit.setText("")


        except DuplicateError as e:
            self.addTasklabel.setText(e.message)
            self.addTasklabel.setStyleSheet("color: rgb(255, 0, 0);")
            self.addTasklineEdit.setText("")



        else:

            self.addTasklabel.setText("Enter a task!")
            self.addTasklabel.setStyleSheet("color: rgb(255, 255, 255);")
            with open('tasksFile.txt', "a") as taskFile:
                # csv_writer = csv.writer(taskFile)
                # csv_writer.writerow(task)
                #maybe add time completed, or time added to file/created

                taskFile.write(f"{task}###{False}\n")

            self.addTasklineEdit.setText("")
            self.tasksIndex += 1



