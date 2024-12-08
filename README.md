Title: Basic Todo-List PyQt6
Description: Very simple To-do list created for Intro to Computer Science II(UNO CSCI1620) python project. Using PyCharm, PyQT6, and QtDesinger for .ui files.
Good Reference for simple tasks when using PyQt, for example: button conenction, pop-ups, exception handling, and .txt reading and writing. 
Features: Add, edit tasks, persistance, clear history, completed task counter
Possible Additional Features: Sounds, More tasks, Settings, History window - see previous completed tasks, better looking GUI.




<img width="400" alt="Screenshot 2024-12-08 at 12 55 59 PM" src="https://github.com/user-attachments/assets/2b0e3ef5-88f8-4961-abf5-6991b2122133">

How to use:
Clone repositiory and open code editor for python. (I used PyCharm Community Version - Free)
install Pyqt
```{r, engine='sh', count_lines}
pip install pyqt6
```


If you  need to change untitled.ui with QtDesigner, don't forget to regenerate gui.py file using this command:  
```{r, engine='sh', count_lines}
pyuic6 -x untitled.ui -o gui.py
```
