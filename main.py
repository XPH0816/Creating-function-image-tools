# Import required modules from Pillow package
from PIL import Image, ImageDraw

# Creating an image with 600px * 600px and a white background
img = Image.new('RGBA', (600, 600), (255, 255, 255,255))

# Creating Draw Tools on the img
draw = ImageDraw.Draw(img)

# Get the img size
x,y = img.size

# Draw a line in the img (x1, y1, x2, y2) form
# x1 represent to start point in x 
# x2 represent to end point in x
# y1 represent to start point in y
# y2 represent to end point in y

draw.line((200, 100, 200, 200), fill=(0, 0, 0), width=3)

#Show image
img.show()

#Save image
#img.save("./image/test.png")