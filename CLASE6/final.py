from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QSlider, QProgressBar
from PyQt6.QtCore import Qt
import paho.mqtt.client as mqtt
from PyQt6.QtCore import QTimer
import sys
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

        # Label
        self.label1 = QLabel("Valor1:  ",self)
        self.label1.move(100,100)
        self.label2 = QLabel("Valor2:  ",self)
        self.label2.move(100,150)
        # ProgessBar
        self.bar = QProgressBar(self)
        self.bar.setGeometry(200,150,200,30)
        # Slider
        s = QSlider(Qt.Orientation.Horizontal,self)
        s.setGeometry(200,100,200,30)
        s.setMaximum(100)
        s.setMinimum(0)
        s.valueChanged.connect(self.datos)
        # Configuracion del broker
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Conexion al broker
        self.client.connect("192.168.1.16", port=1883)
        self.client.loop_start()  # Inicia bucle en un hilo separado
        # Temporizador
        timer = QTimer(self)
        timer.timeout.connect(self.mysql_query)
        timer.start(10000)
        self.show()
    def datos(self,value):
        self.client.publish("canaly",value)
        self.bar.setValue(value)
        print(value)
    # Callback que se ejecutar al conectar al broker
    def on_connect(self, client, userdata, flags, rc):
        print("Conectado al broker MQTT")
        client.subscribe("canalx")
    def mysql_query(self):
        con = pymysql.connect(
        user="admin",
        password="Raspi@2022#1", 
        host="localhost", 
        database= "MONITOREO")
        cursor = con.cursor()
        query = "SELECT * FROM sensores ORDER BY id DESC LIMIT 1"
        cursor.execute(query)
        resultado = cursor.fetchone();
        #print(resultado,type(resultado))
        pot1 = resultado[2]
        pot2 = resultado[3]
        #print(pot1,pot2,type(pot1))
        self.label1.setText("Valor1:"+str(pot1))
        self.label1.adjustSize()
        self.label2.setText("Valor2:"+str(pot2))
        self.label2.adjustSize()
        cursor.close()
        con.close()
    def on_message(self, client, userdata, message):
        print("Mensaje recibido:", message.payload.decode())
        pot1 = message.payload.decode().split(",")[0]
        pot2 = message.payload.decode().split(",")[1]
        #self.label1.setText("Valor1: " + pot1)
        #self.label1.adjustSize()
        #self.label2.setText("Valor2: " + pot2)
        #self.label2.adjustSize()
        con = pymysql.connect(
        user="admin",
        password="Raspi@2022#1", 
        host="localhost", 
        database= "MONITOREO")
        cursor = con.cursor()
        insert_query = f"INSERT INTO sensores(id,tiempo,pot1,pot2) VALUES (NULL, current_timestamp(),{pot1},{pot2});"
        cursor.execute(insert_query)
        con.commit()
        cursor.close()
        con.close()
    def initUI(self):
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowTitle(self.titulo)


if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    sys.exit(app.exec())
