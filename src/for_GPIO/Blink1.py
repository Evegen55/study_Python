'''
Created on 28.12.2016
'''
import RPi.GPIO as GPIO
import time

# Pin Definiton:
ledPin = 16 # P1 pin 16 (Broadcom pin 23)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
print("Here we go! Press CTRL+C to exit")
try:
    while True:
        GPIO.output(ledPin, True)
        time.sleep(1)
        GPIO.output(ledPin, True)
        time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
