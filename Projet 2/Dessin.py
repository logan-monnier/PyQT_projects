import sys

from CanvasDessin import CanvasDessin

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Dessin(QMainWindow):
  def __init__(self):
    super().__init__()
    self.canvas = CanvasDessin()
    self.iconColor = self.canvas.penColor
    self.setCentralWidget(self.canvas)
    self.menu()

  def menu(self):
    toolbar = self.addToolBar("toolbar")

    pix = QPixmap(32, 32)
    pix.fill(self.iconColor)
    
    colorAct = QAction(QIcon(pix), "Choose color...", self )
    colorAct.setShortcut("Win+Shift+C")
    colorAct.setToolTip(self.tr("Choose Color"))
    colorAct.setStatusTip(self.tr("Choose Color"))

    slider = QSlider(Qt.Orientation.Horizontal, self)
    slider.setRange(1,100)
    slider.setValue(3)
    slider.setSingleStep(1)
    slider.setPageStep(10)

    clear = QPushButton("Clear")

    toolbar.addAction(colorAct)
    toolbar.addWidget(slider)
    toolbar.addWidget(clear)

    colorAct.triggered.connect(self.canvas.chooseColor)
    slider.valueChanged.connect(self.canvas.chooseWidth)
    clear.clicked.connect(self.canvas.clear)

def main(args):
  app = QApplication(args)
  win = Dessin()
  win.show()
  app.exec_()

if __name__ == '__main__':
  main(sys.argv)