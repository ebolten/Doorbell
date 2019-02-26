import sys
from PyQt5.QtWidgets import *
app = QApplication([])
button = QPushButton('Doorbell')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You rang the doorbell!')
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
