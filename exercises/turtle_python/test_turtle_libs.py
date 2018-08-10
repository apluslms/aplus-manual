'''
Created on 9 Aug 2018

@author: atilante
'''

import random
from minipng import Image
from simpleturtle import Turtle

def line_test_valid():
    img = Image(800, 800)
    
    # Inside drawing area
    
    # Light green: horizontal, left to right
    img.line(10, 30, 50, 30, (0, 255, 0))
    
    # Light yellow: horizonal, right to left
    img.line(50, 60, 10, 60, (255, 255, 0))
    
    # Dark green: vertical, top to down
    img.line(100, 30, 100, 80, (0, 128, 0))
    
    # Dark yellow: vertical, bottom to top
    img.line(120, 80, 120, 30, (128, 128, 0))
    
    # One pixel, white, at center
    img.line(400, 400, 400, 400, (255, 255, 255))
    
    # Horizontally cropped, cyan
    img.line(-1, 500, 800, 500, (0, 255, 255))

    # Vertically cropped, blue
    img.line(500, -1, 500, 800, (0, 0, 255))

    # Horizontally cropped, right to left, red 
    img.line(800, 550, -1, 550, (255, 0, 0))
    
     # Vertically cropped, bottom to top, orange
    img.line(550, 800, 550, -1, (255, 128, 0))

    
    img.write_to_file('test_line.png')
    

    

def line_test_invalid():    
    img = Image(800, 800)
    
    # Invalid lines. Test image should remain completely black.
    
    # Horizontal, y coordinate negative, red
    img.line(10, -1, 100, -1, (255, 0, 0))
    
    # Horizontal, y coordinate >=800, orange
    img.line(10, 800, 100, 800, (255, 128, 0))
    
    # Vertical,  x coordinate negative, dark red
    img.line(-1, 40, -1, 100, (255, 0, 0))

    # Vertical,  x coordinate >=800, dark orange
    img.line(800, 40, 800, 100, (128, 64, 0))
    
    # Not vertical or horizontal, blue
    img.line(50, 60, 110, 180, (0, 0, 255))
    
    # Another not vertical or horizontal, dark blue
    img.line(75, 95, 125, 15, (0, 0, 128))

    
    img.write_to_file('test_line_invalid.png')

def random_test():
    t = Turtle()
    for i in range(1000):
        if (random.randint(1,2) == 1):
            t.left(90)
        else:
            t.right(90)
        t.forward(30)
    t.get_image().write_to_file('test_turtle_libs.png')

if __name__ == '__main__':
    line_test_valid()
    line_test_invalid()
    random_test()