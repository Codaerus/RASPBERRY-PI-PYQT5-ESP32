from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSlider
from PyQt5.QtCore import Qt
import RPi.GPIO as GPIO
class App(QWidget):
	def __init__(self):
		super().__init__()
		self.w = 600
		self.h = 300
		self.x = 100
		self.y = 100
		self.titulo = "MONITOREO"
		self.initUI()
		self.initPWM()
	def initPWM(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(21,GPIO.OUT)
		self.led = GPIO.PWM(21, 100)
		self.led.start(0)
	def initUI(self):
		self.setGeometry(self.x,self.y,self.w,self.h)
		self.setWindowTitle(self.titulo)
		#LABEL
		self.label1 = QLabel("ESPERANDO",self)
		p = "font-size:20px; font-weight: bold"
		self.label1.setStyleSheet(p)
		self.label1.move(100,100)
		#Slider
		slider1 = QSlider(Qt.Horizontal,self)
		slider1.setGeometry(100,160,200,30)
		slider1.valueChanged.connect(self.pwm)
		slider1.setMaximum(100)
		slider1.setMinimum(0)
		self.show()
	def pwm(self,data):
		print(data)
		self.label1.setText(str(data))
		self.led.ChangeDutyCycle(data)
if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	app.exec_()
