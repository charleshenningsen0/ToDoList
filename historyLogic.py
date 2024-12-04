from PyQt6.QtWidgets import QApplication, QMainWindow
from guiHistory import Ui_History



class historyLogic(QMainWindow, Ui_History):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.backButton.clicked.connect(lambda : self.exit())


    def exit(self):
        from mainLogic import mainLogic
        self.close()




