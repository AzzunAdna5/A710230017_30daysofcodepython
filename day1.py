import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from typing import Callable

class Greeter:
    def __init__(self, language='english'):
        self.language = language
    
    def set_language(self, language):
        self.language = language
    
    def greet(self):
        if self.language == 'english':
            return 'Hello!'
        elif self.language == 'spanish':
            return '¡Hola!'
        elif self.language == 'french':
            return 'Bonjour!'
        else:
            return 'Language not supported.'

class GreetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Greeter App')
        self.setGeometry(200, 200, 300, 150)
        
        self.greeter = Greeter()
        
        self.label = QLabel('Welcome!', self)
        self.label.setAlignment(Qt.AlignCenter)
        
        self.button_english = QPushButton('English', self)
        self.button_spanish = QPushButton('Spanish', self)
        self.button_french = QPushButton('French', self)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_english)
        layout.addWidget(self.button_spanish)
        layout.addWidget(self.button_french)
        
        self.setLayout(layout)
        
        self.button_english.clicked.connect(lambda: self.update_greeting('english'))
        self.button_spanish.clicked.connect(lambda: self.update_greeting('spanish'))
        self.button_french.clicked.connect(lambda: self.update_greeting('french'))
    
    def update_greeting(self, language):
        self.greeter.set_language(language)
        greeting = self.greeter.greet()
        self.label.setText(greeting)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    greet_app = GreetApp()
    greet_app.show()
    sys.exit(app.exec_())
