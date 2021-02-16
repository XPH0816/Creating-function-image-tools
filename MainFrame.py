from os import link
from PreviewFrame import Preview_Window
from main_OOP import Picture
import sys

from PyQt5.QtWidgets import QApplication, QComboBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QRadioButton, QStackedLayout, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QStatusBar

# Create a subclass of QMainWindow to setup the calculator's GUI
class Window(QMainWindow):
    """GUI View"""
    def __init__(self):
        """View initializer."""
        super().__init__()
        self.number_point = 1
        self.function_type = 0
        
        # Set some main window's properties
        self.setWindowTitle('Function Image')
        self.setFixedSize(900, 600)
        
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        
        #Set the Grid Layout
        self.layout = QGridLayout()
        
        #Set the First Part Outer Layout
        self.sublayout_1 = QVBoxLayout()
        self.sublayout_1.setContentsMargins(10, 0, 50, 0)
        
        self.basic_groupbox = QGroupBox("Basic Configuration")
        self.basic_groupbox.setContentsMargins(40, 0, 0, 0)
        self.basic_groupbox.setLayout(self.sublayout_1)
        
        #Set the The First Part of Inner Layout
        self.leftlayout_1 = QHBoxLayout()
        
        self.function_type_group_box = QGroupBox("Function Type :")
        self.function_type_group_box.setFixedHeight(60)
        self.function_type_group_box.setContentsMargins(100, 0, 0, 0)
        self.function_type_group_box.setLayout(self.leftlayout_1)
        
        self.type_radiobutton_1 = QRadioButton("A/B")
        self.type_radiobutton_1.setChecked(True)
        self.type_radiobutton_2 = QRadioButton("x - f(x)")
        
        #Place the Radiobutton
        self.leftlayout_1.addWidget(self.type_radiobutton_1)
        self.leftlayout_1.addWidget(self.type_radiobutton_2)
        
        #Set the Second part of Inner Layout
        self.leftlayout_2 = QFormLayout()
        self.leftlayout_2.setHorizontalSpacing(20)
        
        self.function_info_group_box = QGroupBox("Function Info :")
        self.function_info_group_box.setFixedHeight(60)
        self.function_info_group_box.setContentsMargins(100, 10, 0, 0)
        self.function_info_group_box.setLayout(self.leftlayout_2)
        
        #Set and Place the Component for the form layout
        self.function_name = QLineEdit()
        self.function_name.setFixedWidth(200)
        self.leftlayout_2.addRow("Function Name:", self.function_name)
        
        #Set the Third Part of Inner Layout
        self.leftlayout_3 = QHBoxLayout()
        self.point_number = QGroupBox("Point Number :")
        self.point_number.setFixedHeight(60)
        self.point_number.setContentsMargins(100, 10, 0, 0)
        self.point_number.setLayout(self.leftlayout_3)
        
        self.number_1 = QRadioButton("1")
        self.number_2 = QRadioButton("2")
        self.number_3 = QRadioButton("3")
        self.number_4 = QRadioButton("4")
        
        self.number_1.setChecked(True)
        
        #Place the Radiobutton
        self.leftlayout_3.addWidget(self.number_1)
        self.leftlayout_3.addWidget(self.number_2)
        self.leftlayout_3.addWidget(self.number_3)
        self.leftlayout_3.addWidget(self.number_4)
        
        #Place all the Inner Layout for First Part of Outer Layout
        self.sublayout_1.addWidget(self.function_type_group_box)
        self.sublayout_1.addWidget(self.function_info_group_box)
        self.sublayout_1.addWidget(self.point_number)
        
        #Set the Second Part Outer Layout
        self.sublayout_2 = QHBoxLayout()
        self.advanced_groupbox = QGroupBox("Advanced Configuration")
        self.advanced_groupbox.setContentsMargins(40, 0, 0, 0)
        self.advanced_groupbox.setLayout(self.sublayout_2)
        
        #Create the stacked Layout
        self.stackedLayout = QStackedLayout()
        
        #Create the First Page
        self.page1 = QWidget()
        self.page1.setContentsMargins(0, 10, 0, 0)
        self.page1Layout = QFormLayout()
        self.page1Layout.setVerticalSpacing(10)
        self.firstpointvalue = QLineEdit()
        self.firstendpointvalue = QLineEdit()
        self.page1Layout.addRow("First Point Value :", self.firstpointvalue)
        self.page1Layout.addRow("First End Point Value :", self.firstendpointvalue)
        self.page1.setLayout(self.page1Layout)
        
        #Create the Second Page
        self.page2 = QWidget()
        self.page2.setContentsMargins(0, 10, 0, 0)
        self.page2Layout = QFormLayout()
        self.page2Layout.setVerticalSpacing(40)
        
        self.firstpointvalue2 = QLineEdit()
        self.firstendpointvalue2 = QLineEdit()
        self.secondpointvalue2 = QLineEdit()
        self.secondendpointvalue2 = QLineEdit()
        
        self.combolink2_1 = QComboBox()
        self.combolink2_1.addItems(["1st", "2nd"])
        
        self.combolink2_2 = QComboBox()
        self.combolink2_2.addItems(["1st", "2nd"])
        self.combolink2_2.setCurrentIndex(1)
        
        self.page2Layout.addRow("First Point Value :", self.firstpointvalue2)
        self.page2Layout.addRow("First End Point Value :", self.firstendpointvalue2)
        self.page2Layout.addRow("Second Point Value :", self.secondpointvalue2)
        self.page2Layout.addRow("Second End Point Value :", self.secondendpointvalue2)
        self.page2Layout.addRow("1st Point Link :", self.combolink2_1)
        self.page2Layout.addRow("2nd Point Link :", self.combolink2_2)
        self.page2.setLayout(self.page2Layout)
        
        #Create the Third Page
        self.page3 = QWidget()
        self.page3.setContentsMargins(0, 10, 0, 0)
        self.page3Layout = QFormLayout()
        self.page3Layout.setVerticalSpacing(20)
        
        self.firstpointvalue3 = QLineEdit()
        self.firstendpointvalue3 = QLineEdit()
        self.secondpointvalue3 = QLineEdit()
        self.secondendpointvalue3 = QLineEdit()
        self.thirdpointvalue3 = QLineEdit()
        self.thirdendpointvalue3 = QLineEdit()
        
        self.combolink3_1 = QComboBox()
        self.combolink3_1.addItems(["1st", "2nd", "3rd"])
        
        self.combolink3_2 = QComboBox()
        self.combolink3_2.addItems(["1st", "2nd", "3rd"])
        self.combolink3_2.setCurrentIndex(1)
        
        self.combolink3_3 = QComboBox()
        self.combolink3_3.addItems(["1st", "2nd", "3rd"])
        self.combolink3_3.setCurrentIndex(2)
        
        self.page3Layout.addRow("First Point Value :", self.firstpointvalue3)
        self.page3Layout.addRow("First End Point Value :", self.firstendpointvalue3)
        self.page3Layout.addRow("Second Point Value :", self.secondpointvalue3)
        self.page3Layout.addRow("Second End Point Value :", self.secondendpointvalue3)
        self.page3Layout.addRow("Third Point Value :", self.thirdpointvalue3)
        self.page3Layout.addRow("Third End Point Value :", self.thirdendpointvalue3)
        self.page3Layout.addRow("1st Point Link :", self.combolink3_1)
        self.page3Layout.addRow("2nd Point Link :", self.combolink3_2)
        self.page3Layout.addRow("3rd Point Link :", self.combolink3_3)
        self.page3.setLayout(self.page3Layout)
        
        #Create the Fourth Page
        self.page4 = QWidget()
        self.page4.setContentsMargins(0, 10, 0, 0)
        self.page4Layout = QFormLayout()
        self.page4Layout.setVerticalSpacing(18)
        
        self.firstpointvalue4 = QLineEdit()
        self.firstendpointvalue4 = QLineEdit()
        self.secondpointvalue4 = QLineEdit()
        self.secondendpointvalue4 = QLineEdit()
        self.thirdpointvalue4 = QLineEdit()
        self.thirdendpointvalue4 = QLineEdit()
        self.fourthpointvalue4 = QLineEdit()
        self.fourthendpointvalue4 = QLineEdit()
        
        self.combolink4_1 = QComboBox()
        self.combolink4_1.addItems(["1st", "2nd", "3rd", "4th"])
        
        self.combolink4_2 = QComboBox()
        self.combolink4_2.addItems(["1st", "2nd", "3rd", "4th"])
        self.combolink4_2.setCurrentIndex(1)
        
        self.combolink4_3 = QComboBox()
        self.combolink4_3.addItems(["1st", "2nd", "3rd", "4th"])
        self.combolink4_3.setCurrentIndex(2)
        
        self.combolink4_4 = QComboBox()
        self.combolink4_4.addItems(["1st", "2nd", "3rd", "4th"])
        self.combolink4_4.setCurrentIndex(3)
        
        self.page4Layout.addRow("First Point Value :", self.firstpointvalue4)
        self.page4Layout.addRow("First End Point Value :", self.firstendpointvalue4)
        self.page4Layout.addRow("Second Point Value :", self.secondpointvalue4)
        self.page4Layout.addRow("Second End Point Value :", self.secondendpointvalue4)
        self.page4Layout.addRow("Third Point Value :", self.thirdpointvalue4)
        self.page4Layout.addRow("Third End Point Value :", self.thirdendpointvalue4)
        self.page4Layout.addRow("Third Point Value :", self.fourthpointvalue4)
        self.page4Layout.addRow("Third End Point Value :", self.fourthendpointvalue4)
        self.page4Layout.addRow("1st Point Link :", self.combolink4_1)
        self.page4Layout.addRow("2nd Point Link :", self.combolink4_2)
        self.page4Layout.addRow("3rd Point Link :", self.combolink4_3)
        self.page4Layout.addRow("4th Point Link :", self.combolink4_4)
        self.page4.setLayout(self.page4Layout)
        
        #Place the Page to Stacked Layout
        self.stackedLayout.addWidget(self.page1)
        self.stackedLayout.addWidget(self.page2)
        self.stackedLayout.addWidget(self.page3)
        self.stackedLayout.addWidget(self.page4)
        
        #Place the Stacked Layout
        self.sublayout_2.addLayout(self.stackedLayout)
        
        #Set the Third Part Outer Layout
        self.sublayout_3 = QVBoxLayout()
        self.preview_button =  QPushButton('Preview')
        self.sublayout_3.addWidget(self.preview_button)
        
        #Place all the Outer Layout
        self.layout.addWidget(self.basic_groupbox, 0, 0, 3, 2)
        self.layout.addWidget(self.advanced_groupbox, 0, 2, 2, 1)
        self.layout.addLayout(self.sublayout_3, 2, 2, 1, 1)
        
        #Place the Grid layout to Central Widget
        self._centralWidget.setLayout(self.layout)
        
        #Connect all Function
        self.number_1.clicked.connect(lambda: self.switchPage(self.number_1))
        self.number_2.clicked.connect(lambda: self.switchPage(self.number_2))
        self.number_3.clicked.connect(lambda: self.switchPage(self.number_3))
        self.number_4.clicked.connect(lambda: self.switchPage(self.number_4))
        
        self.preview_button.clicked.connect(self.CreateImage)
        
        self.type_radiobutton_1.clicked.connect(self.setFunctionType)
        self.type_radiobutton_2.clicked.connect(self.setFunctionType)
        
        #Set the Status Bar
        status = QStatusBar()
        status.showMessage("Welcome to the Creating function image tool")
        self.setStatusBar(status)
        
    def switchPage(self, b):
        b = int(b.text())
        self.number_point = b
        self.stackedLayout.setCurrentIndex(b-1)
        
    def setFunctionType(self):
        if self.type_radiobutton_1.isChecked() :
            self.function_type = 0
        elif self.type_radiobutton_2.isChecked() :
            self.function_type = 1
        pass
    
    def CreateImage(self):
        # Initialize the value
        if self.number_point == 1:
            self.point_domain = [self.firstpointvalue.text()]
            self.point_range = [self.firstendpointvalue.text()]
            self.link_order = [1,1]
        elif self.number_point == 2 :
            self.point_domain = [self.firstpointvalue2.text(), self.secondpointvalue2.text()]
            self.point_range = [self.firstendpointvalue2.text(), self.secondendpointvalue2.text()]
            self.link_order = [self.combolink2_1.currentIndex()+1, self.combolink2_2.currentIndex()+1]
        elif self.number_point == 3:
            self.point_domain = [self.firstpointvalue3.text(), self.secondpointvalue3.text(), self.thirdpointvalue3.text()]
            self.point_range = [self.firstendpointvalue3.text(), self.secondendpointvalue3.text(), self.thirdendpointvalue3.text()]
            self.link_order = [self.combolink3_1.currentIndex()+1, self.combolink3_2.currentIndex()+1, self.combolink3_3.currentIndex()+1]
        elif self.number_point == 4 :
            self.point_domain = [self.firstpointvalue4.text(), self.secondpointvalue4.text(), self.thirdpointvalue4.text(), self.fourthpointvalue4.text()]
            self.point_range = [self.firstendpointvalue4.text(), self.secondendpointvalue4.text(), self.thirdendpointvalue4.text(), self.fourthendpointvalue4.text()]
            self.link_order = [self.combolink4_1.currentIndex()+1, self.combolink4_2.currentIndex()+1, self.combolink4_3.currentIndex()+1, self.combolink4_4.currentIndex()+1]
        
        
        #Create the Image
        img = Picture(self.function_type, self.function_name.text(), self.number_point, self.point_domain, self.point_range, self.link_order)
                
        # Create the Preview Frame
        Frame = Preview_Window(img.img)
        Frame.show()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
