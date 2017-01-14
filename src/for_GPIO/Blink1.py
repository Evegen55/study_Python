'''
Created on 28.12.2016
'''
import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

# Pin Definiton:
ledPin = 16 # P1 pin 16 (Broadcom pin 23)

GPIO.setup(ledPin, GPIO.OUT)
# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
while True:
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(1)