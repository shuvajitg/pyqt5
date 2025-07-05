from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtGui import QFont


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(300, 300)

        self.text_label = QLineEdit()
        self.text_label.setFont(QFont("Helvetica", 32))
        
        
        self.grid = QGridLayout()
        self.buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        
        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px}")
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("C")
        self.delete = QPushButton("<-")
        self.clear.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px}")
        self.delete.setStyleSheet("QPushButton {font: 25pt Comic Sans MS; padding: 10px}")
        
        masterLayout = QVBoxLayout()
        masterLayout.addWidget(self.text_label)
        masterLayout.addLayout(self.grid)
        
        buttonRow = QHBoxLayout()
        buttonRow.addWidget(self.clear)
        buttonRow.addWidget(self.delete)
        masterLayout.addLayout(buttonRow)
        masterLayout.setContentsMargins(25,25,25,25)
        
        self.setLayout(masterLayout)
        
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    def button_click(self):
        button = app.sender()
        text = button.text()
        
        if text == "=":
            symbol = self.text_label.text()
            try:
                res = eval(symbol)
                self.text_label.setText(str(res))
            except Exception as e:
                print("Error", e)
                
        elif text == "C":
            self.text_label.clear()
            
        elif text == "<-":
            currtnt_value = self.text_label.text()
            self.text_label.setText(currtnt_value[:-1])
            
        else:
            currtnt_value = self.text_label.text()
            self.text_label.setText(currtnt_value + text)




if __name__ in "__main__":
    app = QApplication([])
    mainWindow = CalculatorApp()
    mainWindow.setStyleSheet("QWidget { background-color: #123 }")
    mainWindow.show()
    app.exec_()