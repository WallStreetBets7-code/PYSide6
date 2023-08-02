from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QSpinBox
from PySide6.QtWidgets import QMessageBox, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QColor, QPalette, QFont
import random, string

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        p = QPalette()
        p.setColor(QPalette.Window, QColor(210,210,210,255))   
        self.setWindowTitle("Password Generator")
        self.setMinimumSize(450,300)
        self.setPalette(p)

        BarFont = QFont("Times", 14, QFont.Thin, italic = True)
        ButtonFont = QFont("Times", 14, QFont.Thin)
        ButtonFont1 = QFont("Times", 13, QFont.Thin)

        #Button creation
        MainButton = QPushButton("Generate")
        MainButton.setMinimumSize(250,80)
        MainButton.setFont(ButtonFont)
        
        #Search bar/display creation
        self.MainBar = QLineEdit()
        self.MainBar.setMaximumHeight(70)
        self.MainBar.setMinimumWidth(250)
        self.MainBar.setFont(BarFont)

        #Spinbox creation
        self.MainSpin = QSpinBox()
        self.MainSpin.setMinimumSize(249,50)
        self.MainSpin.setFont(ButtonFont1)
        
        MainLabel = QLabel("Amount of Characters")
        MainLabel.setFont(ButtonFont1)

        layout1 = QHBoxLayout()
        layout1.addWidget(MainLabel)
        layout1.addWidget(self.MainSpin)

        layout2 = QVBoxLayout()
        layout2.addWidget(MainButton)
        layout2.addWidget(self.MainBar)

        layout3 = QVBoxLayout()
        layout3.addLayout(layout2)
        layout3.addLayout(layout1)

        self.setLayout(layout3)

        #Connections
        MainButton.clicked.connect(self.passGen) 
        self.MainSpin.valueChanged.connect(self.messageBox)

    def passGen(self):
        #Allows the value to be set by a spinbox
        value = self.MainSpin.value()
        length = value  

        characters = string.ascii_letters + string.digits + string.punctuation
        separator = ""
        password1 = separator.join(random.choice(characters) for x in range(length))

        password = password1

        #displays Password to QSpinbox
        self.MainBar.setText(password)

    def messageBox(self):
        #Will reject any input over 20 characters
        if self.MainSpin.value() > 20: 
            msgBox = QMessageBox.information(self, "Warning", "Maximum Character Limit:  20")
            self.MainSpin.setValue(0)




       

        




 

        
       

    
        
    

