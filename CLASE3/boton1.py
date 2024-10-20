import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN,pull_up_down = GPIO.PUD_UP)

while True:
	if GPIO.input(21) == 0:
		print("Pulsador presionado")
		GPIO.sleep(0.1)
