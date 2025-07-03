# imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

# main window
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("First PyQt5 Application")
main_window.resize(400, 300)

# App components
title = QLabel("Hello, PyQt5!")

title1 = QLabel("?")
title2 = QLabel("?")
title3 = QLabel("?")

button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

my_words = ["Hello", "World", "PyQt5", "Application", "Example"]

# Design
masterLayout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)
row2.addWidget(title1, alignment=Qt.AlignCenter)
row2.addWidget(title2, alignment=Qt.AlignCenter)
row2.addWidget(title3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

masterLayout.addLayout(row1)
masterLayout.addLayout(row2)
masterLayout.addLayout(row3)

main_window.setLayout(masterLayout)

# Create Functions
def random_word1():
    word = choice(my_words)
    title1.setText(word)
    
def random_word2():
    word = choice(my_words)
    print("Button2",word)
    title2.setText(word)
    
def random_word3():
    word = choice(my_words)
    title3.setText(word)

# Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)


main_window.show()
app.exec_()