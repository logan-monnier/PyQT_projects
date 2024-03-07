from Trace import Trace

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CanvasDessin(QWidget):
  def __init__(self):
    super().__init__()
    self.setMinimumSize(600, 300)
    self.setMouseTracking(True)
    self.traces = []
    self.penColor = QColor(0, 0, 255, 255)
    self.penWidth = 3

  def chooseColor(self):
    self.penColor = QColorDialog.getColor()
    action = self.sender()
    pix = QPixmap(32, 32)
    pix.fill(self.penColor)
    action.setIcon(QIcon(pix))

  def chooseWidth(self, width):
    self.penWidth = width

  def clear(self):
    self.traces = []
    self.update()

  def paintEvent(self, evt):    
    for i in range(len(self.traces)):
      painter = QPainter(self)
      path = QPainterPath()
      pen = QPen()
      pen.setColor(self.traces[i].color)
      pen.setWidth(self.traces[i].width)
      painter.setPen(pen)

      points = self.traces[i].points
      path.moveTo(points[0])
      
      for j in points[1:]:
        path.lineTo(j)
      
      painter.drawPath(path)

      painter.end()

  def mouseMoveEvent(self, evt):
    if self.traces and (self.traces[-1].state == self.traces[-1].dragging):
      self.traces[-1].drag(evt.pos())
      self.update()

  def mousePressEvent(self, evt):
    self.traces.append(Trace(self.penWidth, self.penColor))
    self.traces[-1].press(evt.pos())
    self.update()
  
  def mouseReleaseEvent(self, evt):
    self.traces[-1].release(evt.pos())
    self.update()