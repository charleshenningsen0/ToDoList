#mvc , main, controler, view, logic, main, gui


from logic import *
def main():
    application = QApplication([])

    window = Logic()
    window.show()
    application.exec()
#MAYBE SWITCH TO LINE TEXT EDITS

#Add a button to show previoulsy completed tasks!! use files to store previous data!

if __name__ == '__main__':
    main()