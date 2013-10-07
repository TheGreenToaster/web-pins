import sys
import RPi.GPIO as GPIO

help = sys.argv

pin = [11, 12, 13, 15, 16, 18, 22, 7]

pinIn = help[2]
mode = help[1]

if int(mode) == 1:
	GPIO.setup(pin[int(pinIn)] , GPIO.OUT)
	GPIO.output(pin[int(pinIn)] , True)
	

if int(mode) == 0:
	GPIO.setup(pin[int(pinIn)] , GPIO.OUT)
	GPIO.output(pin[int(pinIn)] , False)
	