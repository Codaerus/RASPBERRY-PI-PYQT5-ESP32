from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from gpiozero import LED
import time
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
		#Led
		self.led = LED(21)
		
	def initUI(self):
		self.setGeometry(self.x,self.y,self.w,self.h)
		self.setWindowTitle(self.titulo)
		#boton
		led_on = QPushButton("Encender",self)
		led_on.move(100,100)
		led_on.clicked.connect(self.encender)
		led_off = QPushButton("Apagar",self)
		led_off.move(200,100)
		led_off.clicked.connect(self.apagar)
		self.show()
	def encender(self):
		self.led.on()
	def apagar(self):
		self.led.off()
if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	sys.exit(app.exec_())
