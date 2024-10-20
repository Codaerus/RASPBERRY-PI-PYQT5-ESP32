from gpiozero import Button 
import time 

boton = Button(21, pull_up = True)
while True:
	if boton.value == 1:
		print("Boton presionado")
		time.sleep(0.2)
