import sys

from ButtonModel import ButtonModel

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CanvasButton(QWidget):
  defaultCol = QColor(175,175,175,255)
  hoverCol = QColor(100,200,200,255)
  pressCol = QColor(0,0,255,255)
  def __init__(self):
    super().__init__()
    self.bbox = QRect(50,50,300,150)
    self.setMouseTracking(True)
    self.cursorOver = False
    self.modelBtn = ButtonModel()

  def mouseMoveEvent(self, evt):
    self.cursorOver = self.cursorOnEllipse(evt.pos())
    if self.cursorOver:
      self.modelBtn.enter()
    else:
      self.modelBtn.leave()
    self.update()

  def mousePressEvent(self, evt):
    self.modelBtn.press()
    self.update()
  
  def mouseReleaseEvent(self, evt):
    self.modelBtn.release()
    self.update()

  def paintEvent(self, evt):
    painter = QPainter(self)

    painter.setBrush(self.defaultCol)
    if self.modelBtn.state == self.modelBtn.hover:
      painter.setBrush(self.hoverCol)
    elif self.modelBtn.state == self.modelBtn.pressIn:
      painter.setBrush(self.pressCol)

    painter.drawEllipse(self.bbox)

  def cursorOnEllipse(self, point):
    ellipse = QRegion(self.bbox,QRegion.Ellipse) # défini une region elliptique
    if ellipse.contains(point): # test la position
      return True
    return False

def main(args):
  app = QApplication(args)
  win = QMainWindow()
  btn = CanvasButton()
  win.setCentralWidget(btn)
  win.resize(400,250)
  win.show()
  app.exec_()

if __name__ == '__main__':
  main(sys.argv)