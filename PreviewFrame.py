import sys
from PIL import Image
from PyQt5 import QtGui
from PyQt5.QtGui import QClipboard, QIcon, QImage, QPixmap
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QLabel, QPushButton, QWidget

# Create a subclass of QMainWindow to setup the calculator's GUI
class Preview_Window(QWidget):
    """GUI View"""
    def __init__(self, img):
        """View initializer."""
        super().__init__()
        
        # Set some main window's properties
        self.setWindowTitle('Function Image')
        self.setWindowIcon(QtGui.QIcon('Draw.ico'))
        self.setFixedSize(600, 600)
        
        #Set the Grid Layout
        self.layout = QGridLayout()
        
        #Set the First Part Outer Layout
        self.sublayout_1 = QHBoxLayout()
        self.sublayout_1.setContentsMargins(40, 30, 0, 0)
        
        #Create the Photopage
        self.photopage = QWidget()
        self.photo = QLabel(self.photopage)
        self.img = img
        self.preview = self.img.resize((round(self.img.size[0]*0.8), round(self.img.size[1]*0.8)))
        self.data = self.preview.tobytes("raw", "RGBA")
        self.img = QtGui.QImage(self.data, self.preview.size[0], self.preview.size[1], QtGui.QImage.Format_ARGB32)
        self.pixmap = QPixmap(self.img)
        self.photo.setPixmap(self.pixmap)
        
        #Place the Photopage
        self.sublayout_1.addWidget(self.photopage)
        
        #Set the Second Part Outer Layout
        self.sublayout_2 = QHBoxLayout()
        self.sublayout_2.setContentsMargins(25, 0, 25, 0)
        self.sublayout_2.setSpacing(30)
        self.copybutton = QPushButton("Copy to Clipbord")
        self.copybutton.setFixedWidth(150)
        self.savebutton = QPushButton("Save the Picture")
        self.savebutton.setFixedWidth(150)
        self.cancelbutton = QPushButton("Cancel")
        self.cancelbutton.setFixedWidth(150)
        
        #Place the component 
        self.sublayout_2.addWidget(self.copybutton)
        self.sublayout_2.addWidget(self.savebutton)
        self.sublayout_2.addWidget(self.cancelbutton)
        
        #Place all the Outer Layout
        self.layout.addLayout(self.sublayout_1, 0, 0)
        self.layout.addLayout(self.sublayout_2, 1, 0)
        self.layout.setRowStretch(0, 2)
        self.layout.setRowStretch(1, 1)
        
        #Place the Grid layout to Central Widget
        self.setLayout(self.layout)
        
        #Connect all Function
        self.copybutton.clicked.connect(lambda:self.copy(self.img))
        self.cancelbutton.clicked.connect(lambda:self.close())
        
    def copy(self, picture):
        QApplication.clipboard().setImage(picture)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Preview_Window()
    win.show()
    sys.exit(app.exec_())
