'''
Minimal class which mimicks the Turtle class from the Python turtle library
https://docs.python.org/3.3/library/turtle.html.

This one does not use Tkinter but can write png images.

Author: Artturi Tilanterä <artturi.tilantera@iki.fi>
License: MIT
Created on 9 Aug 2018

'''

from minipng import Image

class Turtle(object):
    '''
    classdocs
    '''

    def speed(self, x):
        '''
        Dummy
        '''
        pass

    def forward(self, t):
        t = int(abs(t))
        dx = t * self.dxy[self.direction][0]
        dy = t * self.dxy[self.direction][1]

        self.image.line(self.x, self.y, self.x + dx, self.y + dy,
            (0, 0, 0))
        self.x += dx
        self.y += dy

    def left(self, a):
        a = int(a)
        if (a % 90 != 0):
            raise Exception('Only 90, 180 or 270 degree turns are allowed')
        self.direction = (self.direction - a // 90) % 4

    def right(self, a):
        self.left(-a)

    def get_image(self):
        return self.image

    def __init__(self):
        '''
        Constructor
        '''
        self.x = 400
        self.y = 400
        self.image = Image(800, 800);
        self.image.rectangle(0, 0, 799, 799, (255, 255, 255))

        # 0 = up
        # 1 = right
        # 2 = down
        # 3 = left
        self.direction = 1
        self.dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]
