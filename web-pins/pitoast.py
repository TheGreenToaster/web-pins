import sys
import RPi.GPIO as GPIO

help = sys.argv

pin = [11, 12, 13, 15, 16, 18, 22, 7]

channel = int(help[1])

GPIO.setup(pin[channel], GPIO.IN)
	
if GPIO.input(pin[channel]):
	print "1"
else:
	print "0"