from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout

app = QApplication([])
mainWindow = QWidget()
mainWindow.setWindowTitle("Calculator")
mainWindow.resize(100, 300)


text_label = QLineEdit()
grid = QGridLayout()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

clear = QPushButton("C")
delete = QPushButton("<-")

row = 0
col = 0

for text in buttons:
    button = QPushButton(text)
    #
    grid.addWidget(button, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1

masterLayout = QVBoxLayout()
masterLayout.addWidget(text_label)
masterLayout.addLayout(grid)

buttonRow = QHBoxLayout()
buttonRow.addWidget(clear)
buttonRow.addWidget(delete)


masterLayout.addLayout(buttonRow)

mainWindow.setLayout(masterLayout)



mainWindow.show()
app.exec_()