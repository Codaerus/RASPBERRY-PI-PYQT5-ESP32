from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import paho.mqtt.client as mqtt
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

        # Label
        self.label1 = QLabel("Valor1:  ",self)
        self.label1.move(100,100)
        self.label2 = QLabel("Valor2:  ",self)
        self.label2.move(100,150)
        #botones
        b_e = QPushButton("Encender",self)
        b_e.move(200,100)
        b_e.clicked.connect(self.send_a)
        
        b_a = QPushButton("Apagar",self)
        b_a.move(200,150)
        b_a.clicked.connect(self.send_b)
        # Configuracion del broker
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        # Conexion al broker
        self.client.connect("192.168.1.16", port=1883)
        self.client.loop_start()  # Inicia bucle en un hilo separado
        self.show()
    def send_a(self):
        self.client.publish("canaly", "a")
    def send_b(self):
        self.client.publish("canaly", "b")
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
    def initUI(self):
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowTitle(self.titulo)


if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    sys.exit(app.exec())
