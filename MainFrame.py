from PreviewFrame import Preview_Window
from main import Picture
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, QMainWindow, QStackedLayout, QVBoxLayout 
from PyQt5.QtWidgets import QLineEdit, QComboBox, QPushButton, QRadioButton, QWidget, QStatusBar

class Window(QMainWindow):
    """GUI View"""
    def __init__(self):
        """View initializer."""
        super().__init__()
        
        self.number_point = 1
        self.function_mode = 0
        self.function_type = 0
        self.firstpointvalue = ""
        self.secondpointvalue = "" 
        self.thirdpointvalue = "" 
        self.fourthpointvalue = ""
        self.firstendpointvalue = ""
        self.secondendpointvalue = "" 
        self.thirdendpointvalue = "" 
        self.fourthendpointvalue = ""
        self.first_link = 1
        self.second_link = 2
        self.third_link = 3
        self.fourth_link = 4
        
        # Set some main window's properties
        self.setWindowTitle('Function Image')
        self.setWindowIcon(QtGui.QIcon('Draw.ico'))
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
        
        #Set the The Before First Part of Inner Layout
        self.leftlayout_0 = QHBoxLayout()
        
        self.mode_group_box = QGroupBox("Function Mode :")
        self.mode_group_box.setFixedHeight(60)
        self.mode_group_box.setContentsMargins(100, 0, 0, 0)
        self.mode_group_box.setLayout(self.leftlayout_0)
        
        self.mode_radiobutton_1 = QRadioButton("Line")
        self.mode_radiobutton_1.setChecked(True)
        self.mode_radiobutton_2 = QRadioButton("Circle")
        
        #Place the Radiobutton
        self.leftlayout_0.addWidget(self.mode_radiobutton_1)
        self.leftlayout_0.addWidget(self.mode_radiobutton_2)

        #Set the The First Part of Inner Layout
        self.leftlayout_1 = QHBoxLayout()
        
        self.function_type_group_box = QGroupBox("Function Type :")
        self.function_type_group_box.setFixedHeight(60)
        self.function_type_group_box.setContentsMargins(100, 0, 0, 0)
        self.function_type_group_box.setLayout(self.leftlayout_1)
        
        self.type_radiobutton_1 = QRadioButton("A/B")
        self.type_radiobutton_1.setChecked(True)
        self.type_radiobutton_2 = QRadioButton("x - f(x)")
        self.type_radiobutton_3 = QRadioButton("None")
        
        #Place the Radiobutton
        self.leftlayout_1.addWidget(self.type_radiobutton_1)
        self.leftlayout_1.addWidget(self.type_radiobutton_2)
        self.leftlayout_1.addWidget(self.type_radiobutton_3)
        
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
        self.sublayout_1.addWidget(self.mode_group_box)
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
        
        #Place the Page to Stacked Layout
        self.stackedLayout.addWidget(self.Page1())
        self.stackedLayout.addWidget(self.Page2())
        self.stackedLayout.addWidget(self.Page3())
        self.stackedLayout.addWidget(self.Page4())
        
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
        self.number_1.clicked.connect(lambda: self.switchPage(self.number_1, self.stackedLayout))
        self.number_2.clicked.connect(lambda: self.switchPage(self.number_2, self.stackedLayout))
        self.number_3.clicked.connect(lambda: self.switchPage(self.number_3, self.stackedLayout))
        self.number_4.clicked.connect(lambda: self.switchPage(self.number_4, self.stackedLayout))
        
        self.preview_button.clicked.connect(self.CreateImage)
        
        self.type_radiobutton_1.clicked.connect(self.setFunctionType)
        self.type_radiobutton_2.clicked.connect(self.setFunctionType)
        self.type_radiobutton_3.clicked.connect(self.setFunctionType)

        self.mode_radiobutton_1.clicked.connect(self.setFunctionMode)
        self.mode_radiobutton_2.clicked.connect(self.setFunctionMode)
        
        #Set the Status Bar
        status = QStatusBar()
        status.showMessage("Welcome to the Creating function image tool")
        self.setStatusBar(status)
        
    def Page1(self):
        #Create the First Page
        page1 = QWidget()
        page1.setContentsMargins(0, 10, 0, 0)
        page1Layout = QFormLayout()
        page1Layout.setVerticalSpacing(10)
        firstpointvalue = QLineEdit()
        firstendpointvalue = QLineEdit()
        page1Layout.addRow("First Point Value :", firstpointvalue)
        page1Layout.addRow("First End Point Value :", firstendpointvalue)
        page1.setLayout(page1Layout)
        
        firstpointvalue.textChanged.connect(lambda: self.textChange(firstpointvalue.text(), 1))
        firstendpointvalue.textChanged.connect(lambda: self.textEndChange(firstendpointvalue.text(), 1))
        
        return page1
    
    def Page2(self):
        #Create the Second Page
        page2 = QWidget()
        page2.setContentsMargins(0, 10, 0, 0)
        page2Layout = QFormLayout()
        page2Layout.setVerticalSpacing(40)
        
        firstpointvalue = QLineEdit()
        firstendpointvalue = QLineEdit()
        secondpointvalue = QLineEdit()
        secondendpointvalue = QLineEdit()
        
        combolink1 = QComboBox()
        combolink1.addItems(["1st", "2nd"])
        combolink1.setCurrentIndex(self.first_link-1)
        
        combolink2 = QComboBox()
        combolink2.addItems(["1st", "2nd"])
        combolink2.setCurrentIndex(self.second_link-1)
        
        page2Layout.addRow("First Point Value :", firstpointvalue)
        page2Layout.addRow("First End Point Value :", firstendpointvalue)
        page2Layout.addRow("Second Point Value :", secondpointvalue)
        page2Layout.addRow("Second End Point Value :", secondendpointvalue)
        page2Layout.addRow("1st Point Link :", combolink1)
        page2Layout.addRow("2nd Point Link :", combolink2)
        page2.setLayout(page2Layout)
        
        firstpointvalue.textChanged.connect(lambda: self.textChange(firstpointvalue.text(), 1))
        firstendpointvalue.textChanged.connect(lambda: self.textEndChange(firstendpointvalue.text(), 1))
        secondpointvalue.textChanged.connect(lambda: self.textChange(secondpointvalue.text(), 2))
        secondendpointvalue.textChanged.connect(lambda: self.textEndChange(secondendpointvalue.text(), 2))
        
        combolink1.currentIndexChanged.connect(lambda: self.selectionChange(combolink1, 1))
        combolink2.currentIndexChanged.connect(lambda: self.selectionChange(combolink2, 2))
        
        self.number_2.toggled.connect(lambda: self.checkChange([1,2], combolink1,combolink2))
        
        return page2
    
    def Page3(self):
        #Create the Third Page
        page3 = QWidget()
        page3.setContentsMargins(0, 10, 0, 0)
        page3Layout = QFormLayout()
        page3Layout.setVerticalSpacing(20)
        
        firstpointvalue = QLineEdit()
        firstendpointvalue = QLineEdit()
        secondpointvalue = QLineEdit()
        secondendpointvalue = QLineEdit()
        thirdpointvalue = QLineEdit()
        thirdendpointvalue = QLineEdit()
        
        combolink1 = QComboBox()
        combolink1.addItems(["1st", "2nd", "3rd"])
        combolink1.setCurrentIndex(self.first_link-1)
        
        combolink2 = QComboBox()
        combolink2.addItems(["1st", "2nd", "3rd"])
        combolink2.setCurrentIndex(self.second_link-1)
        
        combolink3 = QComboBox()
        combolink3.addItems(["1st", "2nd", "3rd"])
        combolink3.setCurrentIndex(self.third_link-1)
        
        page3Layout.addRow("First Point Value :", firstpointvalue)
        page3Layout.addRow("First End Point Value :", firstendpointvalue)
        page3Layout.addRow("Second Point Value :", secondpointvalue)
        page3Layout.addRow("Second End Point Value :", secondendpointvalue)
        page3Layout.addRow("Third Point Value :", thirdpointvalue)
        page3Layout.addRow("Third End Point Value :", thirdendpointvalue)
        page3Layout.addRow("1st Point Link :", combolink1)
        page3Layout.addRow("2nd Point Link :", combolink2)
        page3Layout.addRow("3rd Point Link :", combolink3)
        page3.setLayout(page3Layout)
        
        firstpointvalue.textChanged.connect(lambda: self.textChange(firstpointvalue.text(), 1))
        firstendpointvalue.textChanged.connect(lambda: self.textEndChange(firstendpointvalue.text(), 1))
        secondpointvalue.textChanged.connect(lambda: self.textChange(secondpointvalue.text(), 2))
        secondendpointvalue.textChanged.connect(lambda: self.textEndChange(secondendpointvalue.text(), 2))
        thirdpointvalue.textChanged.connect(lambda: self.textChange(thirdpointvalue.text(), 3))
        thirdendpointvalue.textChanged.connect(lambda: self.textEndChange(thirdendpointvalue.text(), 3))
        
        combolink1.currentIndexChanged.connect(lambda: self.selectionChange(combolink1, 1))
        combolink2.currentIndexChanged.connect(lambda: self.selectionChange(combolink2, 2))
        combolink3.currentIndexChanged.connect(lambda: self.selectionChange(combolink3, 3))
        
        self.number_3.toggled.connect(lambda: self.checkChange([1,2,3], combolink1,combolink2,combolink3))
        
        return page3
    
    def Page4(self):
        #Create the Fourth Page
        page4 = QWidget()
        page4.setContentsMargins(0, 10, 0, 0)
        page4Layout = QFormLayout()
        page4Layout.setVerticalSpacing(18)
        
        firstpointvalue = QLineEdit()
        firstendpointvalue = QLineEdit()
        secondpointvalue = QLineEdit()
        secondendpointvalue = QLineEdit()
        thirdpointvalue = QLineEdit()
        thirdendpointvalue = QLineEdit()
        fourthpointvalue = QLineEdit()
        fourthendpointvalue = QLineEdit()
        
        combolink1 = QComboBox()
        combolink1.addItems(["1st", "2nd", "3rd", "4th"])
        combolink1.setCurrentIndex(self.first_link-1)
        
        combolink2 = QComboBox()
        combolink2.addItems(["1st", "2nd", "3rd", "4th"])
        combolink2.setCurrentIndex(self.second_link-1)
        
        combolink3 = QComboBox()
        combolink3.addItems(["1st", "2nd", "3rd", "4th"])
        combolink3.setCurrentIndex(self.third_link-1)
        
        combolink4 = QComboBox()
        combolink4.addItems(["1st", "2nd", "3rd", "4th"])
        combolink4.setCurrentIndex(self.fourth_link-1)
        
        page4Layout.addRow("First Point Value :", firstpointvalue)
        page4Layout.addRow("First End Point Value :", firstendpointvalue)
        page4Layout.addRow("Second Point Value :", secondpointvalue)
        page4Layout.addRow("Second End Point Value :", secondendpointvalue)
        page4Layout.addRow("Third Point Value :", thirdpointvalue)
        page4Layout.addRow("Third End Point Value :", thirdendpointvalue)
        page4Layout.addRow("Fourth Point Value :", fourthpointvalue)
        page4Layout.addRow("Fourth End Point Value :", fourthendpointvalue)
        page4Layout.addRow("1st Point Link :", combolink1)
        page4Layout.addRow("2nd Point Link :", combolink2)
        page4Layout.addRow("3rd Point Link :", combolink3)
        page4Layout.addRow("4th Point Link :", combolink4)
        page4.setLayout(page4Layout)
        
        firstpointvalue.textChanged.connect(lambda: self.textChange(firstpointvalue.text(), 1))
        firstendpointvalue.textChanged.connect(lambda: self.textEndChange(firstendpointvalue.text(), 1))
        secondpointvalue.textChanged.connect(lambda: self.textChange(secondpointvalue.text(), 2))
        secondendpointvalue.textChanged.connect(lambda: self.textEndChange(secondendpointvalue.text(), 2))
        thirdpointvalue.textChanged.connect(lambda: self.textChange(thirdpointvalue.text(), 3))
        thirdendpointvalue.textChanged.connect(lambda: self.textEndChange(thirdendpointvalue.text(), 3))
        fourthpointvalue.textChanged.connect(lambda: self.textChange(fourthpointvalue.text(), 4))
        fourthendpointvalue.textChanged.connect(lambda: self.textEndChange(fourthendpointvalue.text(), 4))
        
        combolink1.currentIndexChanged.connect(lambda: self.selectionChange(combolink1, 1))
        combolink2.currentIndexChanged.connect(lambda: self.selectionChange(combolink2, 2))
        combolink3.currentIndexChanged.connect(lambda: self.selectionChange(combolink3, 3))
        combolink4.currentIndexChanged.connect(lambda: self.selectionChange(combolink4, 4))
        
        self.number_4.toggled.connect(lambda: self.checkChange([1,2,3,4], combolink1,combolink2,combolink3,combolink4))
        
        return page4
        
    def switchPage(self, button: QRadioButton, stackedLayout: QStackedLayout):
        if button.isChecked():
            num = int(button.text())
        
            # Set the point number
            self.number_point = num
        
            stackedLayout.setCurrentIndex(num-1)
        
    def selectionChange(self, combobox: QComboBox, num: int):
        if num == 1 :
            self.first_link = combobox.currentIndex()+1
        if num == 2 :
            self.second_link = combobox.currentIndex()+1
        if num == 3 :
            self.third_link = combobox.currentIndex()+1
        if num == 4 : 
            self.fourth_link = combobox.currentIndex()+1
            
    def checkChange(self, num: list, *combobox: QComboBox):
        for i in num :
            if i == 1:
                combobox[i-1].setCurrentIndex(self.first_link-1)
            if i == 2:
                combobox[i-1].setCurrentIndex(self.second_link-1)
            if i == 3:
                combobox[i-1].setCurrentIndex(self.third_link-1)
            if i == 4:
                combobox[i-1].setCurrentIndex(self.fourth_link-1)
            
    def textChange(self, text: str, num: int):
        if num == 1:
            self.firstpointvalue = text
        if num == 2:
            self.secondpointvalue = text
        if num == 3:
            self.thirdpointvalue = text
        if num == 4:
            self.fourthpointvalue = text
        
    def textEndChange(self, text: str, num: int):
        if num == 1 :
            self.firstendpointvalue = text
        if num == 2 :
            self.secondendpointvalue = text
        if num == 3 :
            self.thirdendpointvalue = text
        if num == 4 :
            self.fourthendpointvalue = text
        
    def setFunctionType(self):
        if self.type_radiobutton_1.isChecked() :
            self.function_type = 0
        elif self.type_radiobutton_2.isChecked() :
            self.function_type = 1
        elif self.type_radiobutton_3.isChecked() :
            self.function_type = 2
        pass

    def setFunctionMode(self):
        if self.mode_radiobutton_1.isChecked() :
            self.function_mode = 0
            self.number_1.show()
            self.number_1.click()
        elif self.mode_radiobutton_2.isChecked() :
            self.function_mode = 1
            self.number_1.hide()
            self.number_2.click()
        pass
    
    
    def CreateImage(self):
        # Initialize the value
        if self.number_point == 1:
            self.point_domain = [self.firstpointvalue]
            self.point_range = [self.firstendpointvalue]
            self.link_order = [1]
        elif self.number_point == 2 :
            self.point_domain = [self.firstpointvalue, self.secondpointvalue]
            self.point_range = [self.firstendpointvalue, self.secondendpointvalue]
            self.link_order = [self.first_link, self.second_link]
        elif self.number_point == 3:
            self.point_domain = [self.firstpointvalue, self.secondpointvalue, self.thirdpointvalue]
            self.point_range = [self.firstendpointvalue, self.secondendpointvalue, self.thirdendpointvalue]
            self.link_order = [self.first_link, self.second_link, self.third_link]
        elif self.number_point == 4 :
            self.point_domain = [self.firstpointvalue, self.secondpointvalue, self.thirdpointvalue, self.fourthpointvalue]
            self.point_range = [self.firstendpointvalue, self.secondendpointvalue, self.thirdendpointvalue, self.fourthendpointvalue]
            self.link_order = [self.first_link, self.second_link, self.third_link, self.fourth_link]
        
        
        #Create the Image
        img = Picture()
        if self.function_mode == 0:
            img.DrawFunction(self.function_type, self.function_name.text(), self.number_point, self.point_domain, self.point_range, self.link_order)
        if self.function_mode == 1:
            img.DrawPoint(self.function_type, self.function_name.text(), self.number_point, self.point_domain, self.point_range, [self.link_order])

        # Create the Preview Frame
        Frame = Preview_Window(img.img)
        Frame.show()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
