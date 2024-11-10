from PyQt6.QtWidgets import QWidget, QApplication, QLabel
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
        self.label = QLabel("Valor:  ",self)
        self.label.move(100,100)
        
        # Configuracion del broker
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message

        # Conexion al broker
        client.connect("192.168.1.16", port=1883)
        client.loop_start()  # Inicia bucle en un hilo separado
        self.show()
    # Callback que se ejecutar al conectar al broker
    def on_connect(self, client, userdata, flags, rc):
        print("Conectado al broker MQTT")
        client.subscribe("canalx")

    def on_message(self, client, userdata, message):
        print("Mensaje recibido:", message.payload.decode())
        self.label.setText("Valor: " + message.payload.decode())
        self.label.adjustSize()
    def initUI(self):
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowTitle(self.titulo)


if __name__ == "__main__":
    app = QApplication([])
    ex = App()
    sys.exit(app.exec())
