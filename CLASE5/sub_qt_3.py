from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import paho.mqtt.client as mqtt

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.w = 600
		self.h = 300
		self.x = 100
		self.y = 100
		self.titulo = "MONITOREO"
		self.initUI()
	def on_connect(self,client,userdata,flags,rc):
		print("Conectado al broker MQTT")
		client.subscribe("canalx")
	def on_message(self,client,userdata,message):
		pot1 = message.payload.decode().split(",")[0]
		pot2 = message.payload.decode().split(",")[1]
		self.label1.setText("Valor: "+pot1)
		self.label1.adjustSize()
		self.label2.setText("Valor:"+pot2)
		self.label2.adjustSize()
	def initUI(self):
		self.setGeometry(self.x,self.y,self.w,self.h)
		self.setWindowTitle(self.titulo)
		#QLabel 
		self.label1 = QLabel("Valor:   ",self)
		self.label1.move(100,100)
		
		self.label2 = QLabel("Valor:   ", self)
		self.label2.move(250,100)
		#Configuracin del broker
		client = mqtt.Client()
		client.on_connect = self.on_connect
		client.on_message = self.on_message
		client.connect("192.168.1.14",port=1883)
		client.loop_start()
		self.show()

if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	app.exec_()
