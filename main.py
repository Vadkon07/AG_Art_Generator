from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QMainWindow, QMenuBar, QLabel, QGridLayout
from PyQt6.QtCore import Qt
import turtle
from random import randint
import sys

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AG Art Generator")
        self.setGeometry(100, 100, 80, 50)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(0)

        self.widget = QLabel()
        self.widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.widget)
        
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter Angle (from 1 to million)")
        self.main_layout.addWidget(self.line_edit)

        self.generate_button = QPushButton("GENERATE", self)
        self.generate_button.setFixedSize(200, 25)
        self.generate_button.clicked.connect(self.draw_art)
        self.main_layout.addWidget(self.generate_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.button_layout = QHBoxLayout()

        print('Setup...')
        turtle.title('AG')
        turtle.setup(640, 600)
        turtle.hideturtle()
        turtle.bgcolor('black')
        turtle.colormode(255)
        turtle.speed(10000)

    def draw_art(self):
        angle = int(self.line_edit.text())
        
        print(f'Start the drawing with angle ', angle)
        for i in range(0, 200):
            turtle.color(self.generate_random_colour())
            turtle.backward(i)
            turtle.right(angle)

        print('Done')
        turtle.done()

    def generate_random_colour(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
