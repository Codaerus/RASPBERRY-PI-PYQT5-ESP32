from PyQt5.QtWidgets import QWidget,QApplication,QSlider,QProgressBar
from PyQt5.QtCore import Qt
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.w = 600
		self.h = 300
		self.x = 100
		self.y = 100
		self.titulo = "MONITOREO"
		self.initUI()
		
	def initUI(self):
		self.setGeometry(self.x,self.y,self.w,self.h)
		self.setWindowTitle(self.titulo)
		#ProgressBar
		self.bar = QProgressBar(self)
		self.bar.setGeometry(100,50,200,30)
		self.bar.setValue(0)
		#Slider
		slider = QSlider(Qt.Horizontal,self)
		slider.setGeometry(100,100,200,30)
		slider.setMinimum(0)
		slider.setMaximum(100)
		slider.valueChanged.connect(self.datos)
		self.show()
	def datos(self,value):
		print(value)
		self.bar.setValue(value)
if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	sys.exit(app.exec_())
