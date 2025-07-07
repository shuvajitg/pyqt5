from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PyQt6")
        self.setGeometry(0, 0, 400, 400)
        
        with open("pyqt6-tutorial/car.png"):
            image_lable = QLabel(self)
            pixmap = QPixmap("pyqt6-tutorial/car.png")
            pixmap = pixmap.scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            image_lable.setPixmap(pixmap)
            image_lable.move(50, 0)
        
        # lable = QLabel(self)
        # lable.setText("Shuvajit")
        # lable.move(10,10)
        
        # with open("pyqt6-tutorial/work.jpg"):
        #     image_lable = QLabel(self)
        #     pixmap = QPixmap('pyqt6-tutorial/work.jpg')
        #     image_lable.setPixmap(pixmap)
        #     image_lable.move(20, 20)
        
            pass
        
        # Details
        name_lable = QLabel(self)
        name_lable.setText("My Car")
        name_lable.setFont(QFont("Arial", 20))
        name_lable.move(100, 120)
        
        # Engin
        engin_lable = QLabel(self)
        engin_lable.setText("Engin capacity: 15L TFSI")
        engin_lable.setFont(QFont("Mono", 14))
        engin_lable.move(10, 160)
        
        # Features
        features_lable = QLabel(self)
        features_lable.setText("Features: ABS, EBD, ADAS")
        features_lable.setFont(QFont("Mono", 14))
        features_lable.move(10, 185)
        
        # Models
        model_lable = QLabel(self)
        model_lable.setText("Models: 2.2 Petrol, 1.8 Diesel")
        model_lable.setFont(QFont("Mono", 14))
        model_lable.move(10, 210)
        
        # Priceing
        Priceing_lable = QLabel(self)
        Priceing_lable.setText("Price: $30,000")
        Priceing_lable.setFont(QFont("Mono", 14))
        Priceing_lable.move(10, 235)
        
        pass
    
    pass

app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())