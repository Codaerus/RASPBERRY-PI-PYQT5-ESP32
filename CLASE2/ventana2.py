from PyQt5.QtWidgets import QWidget,QApplication

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
		self.show()

if __name__ == "__main__":
	app = QApplication([])
	ex = App()
	app.exec_()
