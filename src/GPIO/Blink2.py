'''
Created on 28 дек. 2016 г.

@author: Evegen
'''
import Rpi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
while True:
    GPIO.output(13, True)
    time.sleep(1)
    GPIO.output(13, True)
    time.sleep(1)