import re
import os
from gui import Ui_TODOLIST
from PyQt6.QtWidgets import QMainWindow, QMessageBox
# to do add sounds


#Citing code
# Author: "Google AI"
# Title: "Overview"
# Date: 12/04/24
# Location:https://www.google.com/search?client=safari&rls=en&q=how+to+use+custom+exceptions+in+python&ie=UTF-8&oe=UTF-8
class DuplicateError(Exception):
    '''
    Custom Exception Class
    '''

    def __init__(self, message) -> None:
        '''
        Initializes the DuplicateError Object
        :param message: string of message sent if error
        '''
        self.message: str = message
    #end cited code


class mainLogic(QMainWindow, Ui_TODOLIST):
    '''
    Main Window Class
    '''

    editButtons: list = []
    editLines: list = []
    tasks: list = []
    doneButtons: list = []
    tasksIndex: int = 0

    def __init__(self) -> None:
        '''
        Initializes the main Window,
        contains persistence logic,
        adds Widgets to lists,
        connects buttons to functions
        '''

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



        #Persistance, keeps the uncompleted tasks displayed even when app is closed.
        if os.path.exists("tasksFile.txt"):
            with open("tasksFile.txt", "r") as file:
                lines = file.readlines()

            uncompletedTasks = []
            RegExCompletedTask = "^.*False\n$"
            for line in lines:
                #If uncompleted, then added to uncompleted tasks
                if re.search(RegExCompletedTask, line):
                    uncompletedTasks.append(line)

            #Updates GUI and variables accordingly
            for i in range(len(uncompletedTasks)):
                    self.tasks[i].setVisible(True)
                    text = uncompletedTasks[i].strip('###False\n')
                    self.tasks[i].setText(text)

                    self.doneButtons[i].setVisible(True)
                    self.editButtons[i].setVisible(True)

                    self.tasksIndex = len(uncompletedTasks)

        #Connecting buttons to actions
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


        self.clearHistoryButton.clicked.connect(lambda : self.showPopup())


    #Citing
    # Author: "Tech with Time"
    # Title: "PyQt5 Tutorial - QMessageBox and Popup Windows"
    # Date: 07/16/19
    # Location: https://www.techwithtim.net/tutorials/python-module-walk-throughs/pyqt5-tutorial/messageboxes
    def showPopup(self) -> None:
        '''
        Creates and shows the confirmation Window (QMessageBox) for clearing History,
        connects to clearHistory function
        '''
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirm")
        msgBox.setText("Are you sure you want to Clear History?")
        # msgBox.setIcon(QMessageBox
        msgBox.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Yes)

        msgBox.buttonClicked.connect(self.clearHistory)
        ret = msgBox.exec()
    #End cited code

    def clearHistory(self, widgetClicked) -> None:
        '''
        If user selected Yes, tasksFile.txt is deleted and GUI is updated
        :param widgetClicked: Yes or Cancel, if user wants to clear data or not
        '''
        if widgetClicked.text() == "&Yes":
            for i in range(self.tasksIndex):
                self.completeTask(1)

            os.remove("tasksFile.txt")
            self.tasksCompleted.setText("0")


    def completeTask(self, index) -> None:
        '''
        Done button pressed, removes task from GUI, changes true value in list to completed
        :param index: index of doneButton pressed in list
        :return:
        '''

        self.addTasklabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.addTasklabel.setText("Enter a task!")


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
        self.tasksCompleted.setText(str(int(self.tasksCompleted.text())+ 1))


    def editTask(self, index) -> None:
        '''
        Edit and Confirm Mode, edit exception handling and edits task,
        :param index: index of editButton pressed
        '''

        #Edit mode
        if self.editButtons[index].text() == "Edit":

            self.editLines[index].setVisible(True)
            self.editLines[index].setText(self.tasks[index].text())
            self.editButtons[index].setText("Confirm")

            #Disable all other buttons
            self.addTaskButton.setEnabled(False)
            for i in range(10):
                self.doneButtons[i].setEnabled(False)

            for i in range(10):
                if i != index:
                    self.editButtons[i].setEnabled(False)
            self.clearHistoryButton.setEnabled(False)

        #Confirm Edit Mode
        else:
            #Validating edited task
            try:
                task = self.editLines[index].text()
                if task == '':
                    raise TypeError
                if os.path.exists("tasksFile.txt"):
                    with open('tasksFile.txt', 'r') as file:
                        lines = file.readlines()
                    for line in lines:
                        if re.search(f'^{task}###False', line):
                            #if edited task is duplicated elsewhere
                            if task != self.tasks[index].text():
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
            #Adds edited task to file
                with open("tasksFile.txt", "r") as file:
                    lines = file.readlines()

                with open("tasksFile.txt", "w") as file:
                    for line in lines:

                        if re.search(f'^{self.tasks[index].text()}###False', line):
                            file.write(f"{task}###False\n")
                        else:
                            file.write(line)


                #Enable all other buttons
                self.addTaskButton.setEnabled(True)
                for i in range(10):
                    self.doneButtons[i].setEnabled(True)

                for i in range(10):
                    if i != index:
                        self.editButtons[i].setEnabled(True)
                self.clearHistoryButton.setEnabled(True)

                #Changes GUI
                self.tasks[index].setText(task)
                self.editButtons[index].setText("Edit")
                self.editLines[index].setText("")
                self.editLines[index].setVisible(False)
                self.addTasklabel.setText("Enter a task!")
                self.addTasklabel.setStyleSheet("color: rgb(255, 255, 255);")


    def addTask(self) -> None:
        '''
        Exception handling, adds task to GUI and to tasksFile.txt if valid task
        '''
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

            #Raises error if 10 tasks already in GUI
            self.tasks[self.tasksIndex].setText(task)
            self.tasks[self.tasksIndex].setVisible(True)
            self.editButtons[self.tasksIndex].setVisible(True)
            self.doneButtons[self.tasksIndex].setVisible(True)


        except TypeError:
            self.addTasklabel.setText("Enter a valid task!")
            self.addTasklabel.setStyleSheet("color: rgb(255, 0, 0);")

        except IndexError:
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
                taskFile.write(f"{task}###{False}\n")

            self.addTasklineEdit.setText("")
            self.tasksIndex += 1



