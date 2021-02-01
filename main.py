# Import required modules from Pillow package
from PIL import Image, ImageDraw, ImageFont

# Creating an image with 600px * 600px and a white background
img = Image.new('RGBA', (600, 600), (255, 255, 255,255))

# Make a blank image for the text, initialized to transparent text color
img_text = Image.new('RGBA', img.size, (255, 255, 255, 0))

# Creating Draw Tools on the img and img_text
draw = ImageDraw.Draw(img)
txt = ImageDraw.Draw(img_text)

# Get the img size
x,y = img.size

# Set the position value
left_x1,left_y1 = (100,100)
left_x2,left_y2 = (100,550)

right_x1,right_y1 = (x-left_x1, left_y1)
right_x2,right_y2 = (x-left_x2, left_y2)

# Get the font 
fnt = ImageFont.truetype('./font/cambriai.ttc', 44)

# Draw a line in the img (x1, y1, x2, y2) form
# x1 represent to start point in x 
# x2 represent to end point in x
# y1 represent to start point in y
# y2 represent to end point in y

draw.line((left_x1, left_y1, left_x2, left_y2), fill=(0, 0, 0), width=3)
draw.line((right_x1, right_y1, right_x2, right_y2), fill=(0, 0, 0), width=3)

# Place the text
draw.text((left_x1-15, left_y1-50), "f(x)", font=fnt, fill=(0, 0, 0, 255))

#Show image
img.show()

#Save image
#img.save("./image/test.png")
