# Science Project

This module is used to display the Current, Voltage of different device in GUI.

The User interface is written using QT. We have used the QT designer to create the ui layout. 


####To convert qt.ui file to python.py file please follow these below instructions.

* Step 1: Go to \Scripts folder in C:\ProgramData\Anaconda3

        example: cd C:\ProgramData\Anaconda3\Scripts

* Step 2: If you not find the pyuic5.exe file then please install PyQT5 using pip.

        example: pip install PyQT5==5.9

* Step 3: Execute: pyuic5.exe -x <<filename.ui>> -o <<ouputfilename.py>>

        example: pyuic5 "C:\Users\NUCER\Google Drive\HiWi\Science_Project\Science_Project.ui" -o "C:\Users\NUCER\Google Drive\HiWi\Science_Project\Science_Project.py"


####Steps to create executables:

* Step 1: Install  pyinstaller using pip.

        example: pip install pyinstaller

* Step 2: Generate executable using following command. pyinstaller << filename.py >> where filename.py should contain entry point(in general term main() method)

        example: pyinstaller main.py