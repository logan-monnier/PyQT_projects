from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Trace():
    idle = 0
    dragging = 1
    def __init__(self, width, color):
        self.state = self.idle
        self.points = []
        self.width = width
        self.color = color
  
    def press(self, point):
        if self.state == self.idle:
            self.state = self.dragging
        self.points.append(point)

    def drag(self, point):
        self.points.append(point)
    
    def release(self, point):
        if self.state == self.dragging:
            self.state = self.idle
        self.points.append(point)