'''
Created on 28.12.2016
'''
import RPi.GPIO as GPIO
import time

# Pin Definiton:
ledPin1 = 16 # P1 pin 16 (Broadcom pin 23)
ledPin2 = 18 # P1 pin 18 (Broadcom pin 24)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)

# Initial state for LEDs:
GPIO.output(ledPin1, GPIO.LOW)
GPIO.output(ledPin2, GPIO.HIGH)
print("Here we go! Press CTRL+C to exit")
try:
    while True:
        GPIO.output(ledPin2, False)
        GPIO.output(ledPin1, True)
        time.sleep(1)
        GPIO.output(ledPin2, True)
        GPIO.output(ledPin1, False)
        time.sleep(1)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
