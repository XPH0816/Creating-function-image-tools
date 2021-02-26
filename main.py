from PIL import Image, ImageDraw, ImageFont
import json

class Picture:
    
    def __init__(self):
        
        # Creating an image with 600px * 600px and a white background
        self.img = Image.new('RGBA', (600, 600), (255, 255, 255, 255))
        
    def DrawPoint(self, num: int, link_order: list):
        # Get the img size
        x, y = self.img.size

        """ Set the position value """
        # Start point and the end point for the left line
        left_start_point = (50, 150)
        left_end_point = (200, 450)

        # Start point and the end point for the right line
        right_start_point = (x-left_end_point[0], left_start_point[1])
        right_end_point = (x-left_start_point[0], left_end_point[1])

        # First Point Left Point position
        left_first_start_x, left_first_start_y = (left_start_point[0]+70, left_start_point[1]+45)
        left_first_end_x, left_first_end_y = (left_start_point[0]+80, left_start_point[1]+55)

        # First Point Right Point position
        right_first_start_x, right_first_start_y = (right_start_point[0]+70, right_start_point[1]+45)
        right_first_end_x, right_first_end_y = (right_start_point[0]+80, right_start_point[1]+55)

        # Creating Draw Tools for the picture
        draw = ImageDraw.Draw(self.img)

        draw.ellipse((left_start_point, left_end_point), fill=(255, 255, 255), outline=(0, 0, 0), width=3)
        draw.ellipse((right_start_point, right_end_point), fill=(255, 255, 255), outline=(0, 0, 0), width=3)
        
        #Draw the point
        for x in range(num):
            CONST = 245 - 45 * num
            draw.ellipse((left_first_start_x, left_first_start_y+(CONST*x), left_first_end_x, left_first_end_y+(CONST*x)), fill=(0, 0, 0))
            draw.ellipse((right_first_start_x, right_first_start_y+(CONST*x), right_first_end_x, right_first_end_y+(CONST*x)), fill=(0, 0, 0))
        
        i = 1
        
        #Draw the line
        for x in link_order:
            
            # link_order in [[1,2],[3,4]] form
            # x in [1,2] form
            
            for y in x :
                self.DrawPointLine(num, i, y)
            
            i += 1

        
        
    def DrawFunction(self, function_type: int, function_name: str, number_point: int, point_domain: list, point_range: list, link_order: list):
        
        """Initialize the variable"""

        # Constant position to arrange the range point
        CONST = 0.25
        
        # Get the img size
        x , y = self.img.size
        
        """ Set the position value """
        # Start point and the end point for the left line
        left_x1 , left_y1 = (100,100)
        left_x2 , left_y2 = (100,550)
        
        # Start point and the end point for the right line
        right_x1 , right_y1 = ( x-left_x1, left_y1 )
        right_x2 , right_y2 = ( x-left_x2, left_y2 )
        
        # First Point Left Label position
        left_text_x = (left_x1-15)
        left_text_y = (left_y1-50)
        
        # First Point Right Label position
        right_text_x = (right_x1-15)
        right_text_y = (right_y1-50)
        
        # Function name Position
        function_x = (x/2)
        function_y = (left_y1-60)
        
        # First Domain Value Position
        domain_x = left_x1 - 40
        domain_y = (left_y1+left_y2)/(number_point+2)
        self.domain_y = domain_y
        
        # First Range Value Position
        range_x = right_x1+20
        range_y = (right_y1+right_y2)/(number_point+2)
        
        # Label Line Position Value
        label_line_x1, label_line_x2 = (domain_x+30, domain_x+50)
        label_line_x3, label_line_x4 = (range_x-30, range_x-10)
        
        # Get the Font
        fnt = ImageFont.truetype('font\FreeSerif.ttf', 44)
        fnt_i = ImageFont.truetype('font\FreeSerifItalic.ttf', 44)
        
        """ Start drawing all the picture """
        
        # Creating Draw Tools for the picture
        self.draw = ImageDraw.Draw(self.img)
        
        # Draw the line on the picture
        self.draw.line((left_x1, left_y1, left_x2, left_y2), fill=(0, 0, 0), width=3)
        self.draw.line((right_x1, right_y1, right_x2, right_y2), fill=(0, 0, 0), width=3)
        
        # Place the text
        if function_type == 0 :
            self.draw.text((left_text_x, left_text_y), "A", font=fnt, fill=(0, 0, 0, 255))
            self.draw.text((right_text_x, right_text_y), "B", font=fnt, fill=(0, 0, 0, 255))
            self.draw.text((function_x, function_y), "%s" % function_name, font=fnt_i, fill=(0, 0, 0, 255))
        if function_type == 1 :
            self.draw.text((left_text_x, left_text_y), "x", font=fnt_i, fill=(0, 0, 0, 255))
            self.draw.text((right_text_x, right_text_y), "%s(x)" % function_name, font=fnt_i, fill=(0, 0, 0, 255))
            self.draw.text((function_x, function_y), "%s" % function_name, font=fnt_i, fill=(0, 0, 0, 255))
        if function_type == 2 :
            self.draw.text((function_x, function_y), function_name, font=fnt_i, fill=(0, 0, 0, 255))
        
        
        # Creating Domain and Label Line
        
        for i, value in enumerate(point_domain, 1):
            # Get the digit
            j = len(str(value))
            
            if self.CheckInt(value):
                self.draw.text((domain_x-15*(j-1), domain_y*(i)), value, font=fnt, fill=(0, 0, 0, 255))
                self.draw.line((label_line_x1, domain_y*(i+CONST), label_line_x2, domain_y*(i+CONST)), fill=(0, 0, 0), width=2)
            else :
                self.draw.text((domain_x-15*(j-1), domain_y*(i)), value, font=fnt_i, fill=(0, 0, 0, 255))
                self.draw.line((label_line_x1, domain_y*(i+CONST), label_line_x2, domain_y*(i+CONST)), fill=(0, 0, 0), width=2)
        
        
        # Creating Range and Label Line
        
        for i, value in enumerate(point_range, 1):
            # Get the digit
            j = len(str(value))
            
            if self.CheckInt(value):
                if i <= 2:
                    self.draw.text((range_x+20*(j-1), range_y*(i+CONST/i)), value, font=fnt, fill=(0, 0, 0, 255))
                    self.draw.line((label_line_x3, range_y*(i+0.25+CONST/i), label_line_x4, range_y*(i+0.25+CONST/i)), fill=(0, 0, 0), width=2)
                elif i > 2:
                    self.draw.text((range_x+20*(j-1), range_y*(i-CONST/(5-i))), value, font=fnt, fill=(0, 0, 0, 255))
                    self.draw.line((label_line_x3, range_y*(i+0.25-CONST/(5-i)), label_line_x4, range_y*(i+0.25-CONST/(5-i))), fill=(0, 0, 0), width=2)
            else :
                if i <= 2:
                    self.draw.text((range_x+20*(j-1), range_y*(i+CONST/i)), value, font=fnt_i, fill=(0, 0, 0, 255))
                    self.draw.line((label_line_x3, range_y*(i+0.25+CONST/i), label_line_x4, range_y*(i+0.25+CONST/i)), fill=(0, 0, 0), width=2)
                elif i > 2:
                    self.draw.text((range_x+20*(j-1), range_y*(i-CONST/(5-i))), value, font=fnt_i, fill=(0, 0, 0, 255))
                    self.draw.line((label_line_x3, range_y*(i+0.25-CONST/(5-i)), label_line_x4, range_y*(i+0.25-CONST/(5-i))), fill=(0, 0, 0), width=2)
        
        
        # Draw the line
        for first, last in enumerate(link_order, 1):
            self.DrawLine(number_point, first, last)
    
    # To Check the value
    def CheckInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
        
    # Draw the point line
    def DrawPointLine(self, number_point: int, start: int, end: int):
        # Read the setting file
        with open("./data.json") as f:
            data = json.load(f)

        # Set the value
        size = data["image-size"]
        data = data["point"]["%s" % number_point]
        data = data["%s" % start]["%s" % end]
        
        #Create the Mapping Line
        img_arrow = Image.open(
            'image\line with middle arrow.png').convert('RGBA')
        img_arrow = img_arrow.rotate(data["angle"], expand=True)
        img_arrow = img_arrow.resize(
            (round(img_arrow.size[0]*data["image-size"]), round(img_arrow.size[1]*size)))
        self.img.paste(
            img_arrow, (data["position-x"], data["position-y"]), img_arrow)

    # Draw the line
    def DrawLine(self, number_point: int, start: int, end: int):
        # Read the setting file
        with open("./data.json") as f:
            data = json.load(f)
        
        # Set the value
        size = data["image-size"]
        data = data["%s" % number_point]
        data = data["%s" % start]["%s" % end]
        
        #Create the Mapping Line
        img_arrow = Image.open(
            'image\line with middle arrow.png').convert('RGBA')
        img_arrow = img_arrow.rotate(data["angle"], expand=True)
        img_arrow = img_arrow.resize(
            (round(img_arrow.size[0]*data["image-size"]), round(img_arrow.size[1]*size)))
        self.img.paste(
            img_arrow, (data["position-x"], int(self.domain_y*(data["position-y"]))), img_arrow)
    

if __name__ == '__main__':
    # Case 4 point
    img = Picture()
    #img.DrawFunction(0, "f", 4, ["1","2","3","4"], ["1","2","3","4"], [1,2,3,4])
    img.DrawPoint(4, [[1,2],[2,3],[1,3],[2,1]])
    img = img.img
    img.show()
