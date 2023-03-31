import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("audioussy")

        button = QPushButton("press for gay sex")
        button.setCheckable(True)

        button.clicked.connect(self.the_button_was_clicked)

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("not yet ;)")




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
