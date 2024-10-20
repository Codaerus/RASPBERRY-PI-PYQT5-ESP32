from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QPushButton,QSlider
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
		#Creamos etiqueta
		self.label1 = QLabel("IOT",self)
		self.label1.move(100,100);
		#Creamos boton
		boton1 = QPushButton("Activar",self)
		boton1.move(150,100)
		boton1.clicked.connect(self.presionado)
		p = "font-size:20px;color:#1ce5ef"
		self.label1.setStyleSheet(p)
		#Creamos slider
		slider = QSlider(Qt.Horizontal,self)
		slider.setMinimum(0)
		slider.setMaximum(100)
		slider.setGeometry(250,100,300,30)
		slider.valueChanged.connect(self.datos)
		self.show()
	def datos(self,value):
		print(value)
		self.label1.setText(str(value))
		self.label1.adjustSize()
	def presionado(self):
		print("Se presiono el boton")

if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	sys.exit(app.exec_())
