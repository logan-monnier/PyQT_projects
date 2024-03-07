import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.quit = QMessageBox.No
		self.menus()
		self.textedit = QTextEdit(self)
		self.setCentralWidget(self.textedit)
		self.statusBar()

	def closeEvent(self, event):
		self.quitApp()
		if self.quit == QMessageBox.No:
			event.ignore()

	def menus(self):
		bar = self.menuBar()
		fileMenu = bar.addMenu( "File" )
		openAct = QAction(QIcon("./open.png"), "Open...", self )
		openAct.setShortcut("Ctrl+O")
		openAct.setToolTip(self.tr("Open File"))
		openAct.setStatusTip(self.tr("Open File"))

		saveAct = QAction(QIcon("./save.png"), "Save...", self )
		saveAct.setShortcut("Ctrl+S")
		saveAct.setToolTip(self.tr("Save File"))
		saveAct.setStatusTip(self.tr("Save File"))

		copyAct = QAction(QIcon("./copy.png"), "Copy...", self )
		copyAct.setShortcut("Ctrl+C")
		copyAct.setToolTip(self.tr("Copy"))
		copyAct.setStatusTip(self.tr("Copy"))

		quitAct = QAction(QIcon("./quit.png"), "Quit...", self )
		quitAct.setShortcut("Alt+F4")
		quitAct.setToolTip(self.tr("Quit"))
		quitAct.setStatusTip(self.tr("Quit"))

		fileMenu.addAction(openAct)
		fileMenu.addAction(saveAct)
		fileMenu.addAction(copyAct)
		fileMenu.addAction(quitAct)

		openAct.triggered.connect(self.openfile)
		saveAct.triggered.connect(self.savefile)
		quitAct.triggered.connect(self.quitApp)
	
	def openfile(self):
		dialog = QFileDialog(self)
		filename = dialog.getOpenFileName(self, "Open file")
		file = QFile(filename[0])	
		file.open(QIODevice.ReadOnly)
		input = QTextStream(file)
		line = input.readAll()
		self.textedit.setHtml(line)

	def savefile(self):
		dialog = QFileDialog(self)
		filename = dialog.getSaveFileName(self, "Save file")
		file = open(filename[0],'w')
		text = self.textedit.toPlainText()
		file.write(text)
		file.close()
	
	def quitApp(self):
		self.quit = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if self.quit == QMessageBox.Yes:
			sys.exit(0)

def main(args):
	app = QApplication(args)
	win = MainWindow()
	win.show()
	app.exec_()

if __name__ == "__main__":
	main(sys.argv)