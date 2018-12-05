import atexit
import sys
import traceback

import serial
from PyQt5 import QtCore, QtWidgets

from Science_Project import Ui_MainWindow


class Main(QtWidgets.QMainWindow):
    ser = None

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.intialzeComponent()
        self.addButtonOperations()

    def intialzeComponent(self):
        self.ui.first_data_not_available_label.setVisible(False)
        self.ui.second_data_not_available_label.setVisible(False)
        self.ui.third_data_not_available_label.setVisible(False)
        self.ui.fourth_data_not_available_label.setVisible(False)
        self.ui.fifth_data_not_available_label.setVisible(False)

    def addButtonOperations(self):
        self.ui.read_pushButton.clicked.connect(self.read_pushButtonCheckedEvent)
        self.ui.stop_pushButton.clicked.connect(self.stop_pushButtonCheckedEvent)

    def read_pushButtonCheckedEvent(self):
        try:
            self.ui.read_pushButton.setEnabled(False)
            self.ui.stop_pushButton.setEnabled(True)
            self.ui.tabWidget.setCurrentWidget(self.ui.display_tab)
            self.setUpSerialPort()
            self.populateSerialData()
        except:
            traceback.print_exc()
            self.displayWarningPopUp(traceback.format_exc())

    def stop_pushButtonCheckedEvent(self):
        self.ui.read_pushButton.setEnabled(True)
        self.ui.stop_pushButton.setEnabled(False)

    def populateSerialData(self):
        # Id, Voltage, current, frequency, XY location in hex, A, B, C, D

        new_line = self.ser.readline().decode('utf-8').rstrip()
        print(new_line)
        '''line_array = new_line.split(',')

        if line_array[0] == 1:

            if self.ui.first_pushButton.isChecked():
                self.ui.first_current_lineEdit.setText()
                self.ui.first_a_lineEdit.setText()
                self.ui.first_b_lineEdit.setText()
                self.ui.first_c_lineEdit.setText()
                self.ui.first_d_lineEdit.setText()
            else:
                self.ui.first_data_not_available_label.setVisible(True)

        elif line_array[0] == 2:

            if self.ui.second_pushButton.isChecked():
                self.ui.second_current_lineEdit.setText()
                self.ui.second_a_lineEdit.setText()
                self.ui.second_b_lineEdit.setText()
                self.ui.second_c_lineEdit.setText()
                self.ui.second_d_lineEdit.setText()
            else:
                self.ui.second_data_not_available_label.setVisible(True)
'''
        if not self.ui.read_pushButton.isEnabled():
            QtCore.QTimer.singleShot(1, self.populateSerialData)

    def displayWarningPopUp(self, warningText="Warning !!"):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(warningText)
        msgbox.setWindowTitle("Warning !! ")
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.exec()

    def setUpSerialPort(self):
        baudrate = self.ui.baudrateComboBox.currentText()
        port = self.ui.portlineEdit.text()
        if self.ser is None:
            self.ser = serial.Serial(port, int(baudrate), timeout=None)
        else:
            return

    def releaseResource(self):
        print("Releasing Resources.... ")
        if self.ser is not None and self.ser.isOpen():
            self.ser.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    atexit.register(window.releaseResource)
    sys.exit(app.exec_())
