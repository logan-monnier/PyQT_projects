from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ButtonModel(QWidget):
  idle = 0
  hover = 1
  pressIn = 2
  pressOut = 3
  def __init__(self):
    super().__init__()
    self.state = self.idle
  
  def enter(self):
    if self.state == self.idle:
      self.state = self.hover
    if self.state == self.pressOut:
      self.state = self.pressIn

  def leave(self):
    if self.state == self.hover:
      self.state = self.idle
    if self.state == self.pressIn:
      self.state = self.pressOut

  def press(self):
    if self.state == self.hover:
      self.state = self.pressIn
  
  def release(self):
    if self.state == self.pressOut:
      self.state = self.idle
    if self.state == self.pressIn:
      self.action()
      self.state = self.hover

  def action(self):
    print("action")