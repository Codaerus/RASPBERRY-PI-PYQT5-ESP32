from gpiozero import PWMLED

led = PWMLED(21)

while 1:
	dc = float(input("Ingrese un valor de 0 a 1 "))
	led.value = dc
