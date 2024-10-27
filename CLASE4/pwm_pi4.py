import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
led = GPIO.PWM(21,500)
led.start(0)

while 1:
	dc = int(input("Ingrese un valor "))
	led.ChangeDutyCycle(dc)
