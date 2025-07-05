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

def button_click():
    button = app.sender()
    text = button.text()
    
    if text == "=":
        symbol = text_label.text()
        try:
            res = eval(symbol)
            text_label.setText(str(res))
        except Exception as e:
            print("Error", e)
            
    elif text == "C":
        text_label.clear()
        
    elif text == "<-":
        currtnt_value = text_label.text()
        text_label.setText(currtnt_value[:-1])
        
    else:
        currtnt_value = text_label.text()
        text_label.setText(currtnt_value + text)

row = 0
col = 0

for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
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


clear.clicked.connect(button_click)
delete.clicked.connect(button_click)


mainWindow.show()
app.exec_()