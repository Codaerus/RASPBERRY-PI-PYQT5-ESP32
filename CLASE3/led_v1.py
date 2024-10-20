import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

while True:
	GPIO.output(21,1)
	GPIO.sleep(1)
	GPIO.output(21,0)
	GPIO.sleep(1)
