#mvc , main, controler, view, logic, main, gui

from mainLogic import *
from historyLogic import *



def main():
    application = QApplication([])


    homeWindow = mainLogic()


    homeWindow.show()

    application.exec()

    # while True:
    #     if homeWindow.mainIsOpen == False:
    #         homeWindow.close()
    #         historyWindow.show()
    #     historyWindow.close()
    #     homeWindow.show()


        #if window = 1 then show next windown, hide previous,

        #else down equal one, show and hide
#MAYBE SWITCH TO LINE TEXT EDITS

#Add a button to show previoulsy completed tasks!! use files to store previous data!

if __name__ == '__main__':
    main()