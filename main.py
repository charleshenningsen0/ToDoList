from mainLogic import *
from PyQt6.QtWidgets import QApplication

def main() -> None:
    '''
    Creates mainLogic and application
    '''
    application = QApplication([])
    homeWindow = mainLogic()
    homeWindow.show()
    application.exec()


if __name__ == '__main__':
    main()