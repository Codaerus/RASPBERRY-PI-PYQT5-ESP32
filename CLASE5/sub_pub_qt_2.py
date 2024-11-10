from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QSlider
from PyQt6.QtCore import Qt
import paho.mqtt.client as mqtt
import sys
from datetime import datetime

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
        self.show()
    def datos(self,value):
        self.client.publish("canaly",value)
        print(value)
    # Callback que se ejecutar al conectar al broker
    def on_connect(self, client, userdata, flags, rc):
        print("Conectado al broker MQTT")
        client.subscribe("canalx")

    def on_message(self, client, userdata, message):
        print("Mensaje recibido:", message.payload.decode())
        self.label1.setText("Valor1: " + message.payload.decode().split(",")[0])
        self.label1.adjustSize()
        self.label2.setText("Valor2: " + message.payload.decode().split(",")[1])
        self.label2.adjustSize()
        timestamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        with open("datos.txt","a") as file:
            file.write(message.payload.decode() + " "+ timestamp + "\n")
    def initUI(self):
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowTitle(self.titulo)


if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    sys.exit(app.exec())
