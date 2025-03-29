from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import paho.mqtt.client as mqtt
import pymysql
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
		self.label2.setText("Valor: "+pot2)
		self.label2.adjustSize()
		self.mysql_query(pot1,pot2)
		
	def mysql_query(self,p1,p2):
		con = pymysql.connect(
		user="admin",
		password="Raspi@2022#1",
		host="localhost"
		,database="MONITOREO")
		cursor = con.cursor()
		code = f"INSERT INTO sensores (id,tiempo,pot1,pot2) VALUES (NULL,current_timestamp(),{p1},{p2});"
		cursor.execute(code)
		con.commit()
		cursor.close()
		con.close()
	def initUI(self):
		self.setGeometry(self.x,self.y,self.w,self.h)
		self.setWindowTitle(self.titulo)
		#QLabel 
		self.label1 = QLabel("Valor:   ",self)
		self.label1.move(100,100)
		self.label2 = QLabel("Valor:   ", self)
		self.label2.move(250,100)
		#QPushButton
		b_e = QPushButton("Encender",self)
		b_e.move(100,200)
		b_e.clicked.connect(self.send_a)
		b_a = QPushButton("Apagar",self)
		b_a.move(250,200)
		b_a.clicked.connect(self.send_b)		
		#Configuracin del broker
		self.client = mqtt.Client()
		self.client.on_connect = self.on_connect
		self.client.on_message = self.on_message
		self.client.connect("192.168.1.14",port=1883)
		self.client.loop_start()
		self.show()
	def send_a(self):
		self.client.publish("canaly","a")
	def send_b(self):
		self.client.publish("canaly","b")

if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	app.exec_()
