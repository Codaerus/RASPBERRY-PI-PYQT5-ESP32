from PyQt5.QtWidgets import QWidget,QApplication,QLabel
from PyQt5.QtCore import QTimer
from gpiozero import Button 
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
		#entrada
		self.boton = Button(21, pull_up = True)
		#label
		self.label1 = QLabel(" ",self)
		self.label1.move(100,100)
		#temporizador
		timer = QTimer(self)
		timer.timeout.connect(self.imprimir)
		timer.start(200)
		self.show()
	def imprimir(self):
		#print("Mensaje impreso cada segundo")
		if self.boton.value == 1:
			print("Boton presionado")
			self.label1.setText("Boton presionado")
			self.label1.adjustSize()
		else:
			self.label1.setText("Boton no presionado")
			self.label1.adjustSize()
if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	sys.exit(app.exec_())
