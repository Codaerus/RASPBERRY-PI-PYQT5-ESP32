class Humano: #clase padre (base)
	def __init__(self,nombre):
		self.nombre = nombre
	def hablar(self):
		print("Hola soy",self.nombre)

class Estudiante(Humano): #clase hija (subclase)
	def __init__(self,carrera,nombre):
		super().__init__(nombre)
		self.carrera = carrera
		#self.presentarse()
	def presentarse(self):
		print("Soy un estudiante de", self.carrera)

juan = Estudiante("Ingenieria","Juan")
juan.hablar()
juan.presentarse()
print(juan.carrera)
