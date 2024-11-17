from PyQt6.QtWidgets import QWidget,QApplication,QPushButton
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
		
	def initUI(self):
		self.setGeometry(self.x,self.y,self.w,self.h)
		self.setWindowTitle(self.titulo)

		#Boton
		b1 = QPushButton("Insertar",self)
		b1.setGeometry(100,100,80,30)
		b1.clicked.connect(self.mysql_query)
		self.show()
	def mysql_query(self):
		con = pymysql.connect(
		user="admin",
		password="Raspi@2022#1", 
		host="localhost", 
		database= "MONITOREO")
		cursor = con.cursor()
		insert_query = f"INSERT INTO sensores(id,tiempo,pot1,pot2) VALUES (NULL, current_timestamp(),26,32);"
		cursor.execute(insert_query)
		con.commit()
		cursor.close()
		con.close()
		
if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	sys.exit(app.exec())
