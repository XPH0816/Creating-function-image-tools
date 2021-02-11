# Import required modules from Pillow package
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PIL import Image, ImageDraw, ImageFont

# Creating an image with 600px * 600px and a white background
img = Image.new('RGBA', (600, 600), (255, 255, 255, 255))
img_arrow = Image.open('image\line with middle arrow.png').convert('RGBA')

# Creating Draw Tools on the img and img_text
draw = ImageDraw.Draw(img)

# Get the img size
x,y = img.size

# Constant position to arrange the range of the function
CONST = 0.25

# Set the position value
left_x1,left_y1 = (100,100)
left_x2,left_y2 = (100,550)

right_x1,right_y1 = (x-left_x1, left_y1)
right_x2,right_y2 = (x-left_x2, left_y2)

left_text_x = (left_x1-15)
left_text_y = (left_y1-50)

right_text_x = (right_x1-15)
right_text_y = (right_y1-50)

function_x = (x/2)
function_y = (left_y1-60)

domain_x = left_x1-40
domain_y = (left_y1+left_y2)/6

range_x = right_x1+20
range_y = (right_y1+right_y2)/6

mapping_line_x1, mapping_line_y1 = (domain_x+40, domain_y)
mapping_line_x2, mapping_line_y2 = (range_x-20, range_y)

label_line_x1, label_line_x2 = (mapping_line_x1-10, mapping_line_x1+10)
label_line_x3, label_line_x4 = (mapping_line_x2-10, mapping_line_x2+10)

# Get the font 
fnt = ImageFont.truetype('font\FreeSerif.ttf', 44)
fnt_i = ImageFont.truetype('font\FreeSerifItalic.ttf', 44)

# Draw a line in the img (x1, y1, x2, y2) form
# x1 represent to start point in x 
# x2 represent to end point in x
# y1 represent to start point in y
# y2 represent to end point in y

draw.line((left_x1, left_y1, left_x2, left_y2), fill=(0, 0, 0), width=3)
draw.line((right_x1, right_y1, right_x2, right_y2), fill=(0, 0, 0), width=3)

# Place the text
draw.text((left_text_x, left_text_y), "A", font=fnt, fill=(0, 0, 0, 255))
draw.text((right_text_x, right_text_y), "B", font=fnt, fill=(0, 0, 0, 255))
draw.text((function_x, function_y), "f", font=fnt_i, fill=(0, 0, 0, 255))

# Creating Domain
draw.text((domain_x, domain_y*(1)), "1", font=fnt, fill=(0, 0, 0, 255))
draw.text((domain_x, domain_y*(2)), "b", font=fnt_i, fill=(0, 0, 0, 255))
draw.text((domain_x, domain_y*(3)), "3", font=fnt, fill=(0, 0, 0, 255))
draw.text((domain_x, domain_y*(4)), "4", font=fnt, fill=(0, 0, 0, 255))

# Draw Domain Label Line 
draw.line((label_line_x1, domain_y*(1.25), label_line_x2, domain_y*(1.25)), fill=(0, 0, 0), width=2)
draw.line((label_line_x1, domain_y*(2.25), label_line_x2, domain_y*(2.25)), fill=(0, 0, 0), width=2)
draw.line((label_line_x1, domain_y*(3.25), label_line_x2, domain_y*(3.25)), fill=(0, 0, 0), width=2)
draw.line((label_line_x1, domain_y*(4.25), label_line_x2, domain_y*(4.25)), fill=(0, 0, 0), width=2)

# Creating Range
draw.text((range_x, range_y*(1+CONST)), "a", font=fnt_i, fill=(0, 0, 0, 255))
draw.text((range_x, range_y*(2+CONST/2)), "2", font=fnt, fill=(0, 0, 0, 255))
draw.text((range_x, range_y*(3-CONST/2)), "c", font=fnt_i, fill=(0, 0, 0, 255))
draw.text((range_x, range_y*(4-CONST)), "d", font=fnt_i, fill=(0, 0, 0, 255))

# Draw Range Label Line 
draw.line((label_line_x3, range_y*(1.25+CONST), label_line_x4, range_y*(1.25+CONST)), fill=(0, 0, 0), width=2)
draw.line((label_line_x3, range_y*(2.25+CONST/2), label_line_x4, range_y*(2.25+CONST/2)), fill=(0, 0, 0), width=2)
draw.line((label_line_x3, range_y*(3.25-CONST/2), label_line_x4, range_y*(3.25-CONST/2)), fill=(0, 0, 0), width=2)
draw.line((label_line_x3, range_y*(4.25-CONST), label_line_x4, range_y*(4.25-CONST)), fill=(0, 0, 0), width=2)

# Draw the arrow to the line
# 1 to 1
#img_arrow = img_arrow.rotate(-4.5, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.85), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (90, int(domain_y*(1.15))), img_arrow)

# 1 to 2
#img_arrow = img_arrow.rotate(-20, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.9), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (90, int(domain_y*(1.15))), img_arrow)

# 1 to 3
#img_arrow = img_arrow.rotate(-35.5, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*1.05), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (90, int(domain_y*(1.15))), img_arrow)

# 1 to 4
#img_arrow = img_arrow.rotate(-57, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*1.55), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (80, int(domain_y*(1.2))), img_arrow)

# 2 to 1
#img_arrow = img_arrow.rotate(13.2, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.88), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (95, int(domain_y*(1.39))), img_arrow)

# 2 to 2
#img_arrow = img_arrow.rotate(-2.2, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.88), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (95, int(domain_y*(2.15))), img_arrow)

# 2 to 3
#img_arrow = img_arrow.rotate(-15.4, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.88), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (95, int(domain_y*(2.15))), img_arrow)

# 2 to 4
#img_arrow = img_arrow.rotate(-32.2, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*1), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (90, int(domain_y*(2.17))), img_arrow)

# 3 to 1
#img_arrow = img_arrow.rotate(32.0, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*1), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (90, int(domain_y*(1.42))), img_arrow)

# 3 to 2
#img_arrow = img_arrow.rotate(15.5, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.88), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (95, int(domain_y*(2.27))), img_arrow)

# 3 to 3
#img_arrow = img_arrow.rotate(1.95, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.84), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (100, int(domain_y*(3.03))), img_arrow)

# 3 to 4
#img_arrow = img_arrow.rotate(-13.5, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.87), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (95, int(domain_y*(3.15))), img_arrow)

# 4 to 1
#img_arrow = img_arrow.rotate(56.3, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*1.5), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (82, int(domain_y*(1.44))), img_arrow)

# 4 to 2
#img_arrow = img_arrow.rotate(34.5, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*1.03), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (90, int(domain_y*(2.28))), img_arrow)

# 4 to 3
#img_arrow = img_arrow.rotate(19.8, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.89), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (95, int(domain_y*(3.03))), img_arrow)

# 4 to 4
#img_arrow = img_arrow.rotate(4.1, expand=True)
#img_arrow = img_arrow.resize((round(img_arrow.size[0]*0.84), round(img_arrow.size[1]*0.75)))
#img.paste(img_arrow, (100, int(domain_y*(3.9))), img_arrow)


# Show image
#img.show()

# Save image
#img.save("./image/test.png")


class App(QWidget):

    def __init__(self, img):
        self.img = img
        super().__init__()
        self.title = 'PyQt5 image'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget
        label = QLabel(self)
        self.preview = self.img.resize((round(self.img.size[0]*0.5), round(self.img.size[1]*0.5)))
        self.data = self.preview.tobytes("raw", "RGBA")
        self.img = QtGui.QImage(self.data, self.preview.size[0], self.preview.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QPixmap(self.img)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App(img)
    sys.exit(app.exec_())
