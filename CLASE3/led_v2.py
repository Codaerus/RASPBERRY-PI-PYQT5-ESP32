from gpiozero import LED
import time 

led = LED(21)

while True:
	led.on()
	time.sleep(1)
	led.off()
	time.sleep(1)
	
