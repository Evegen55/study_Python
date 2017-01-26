'''
Created on Jan 16, 2017

@author: MagPI52
'''
from gpiozero import LED
from time import sleep
red = LED(25)
amber = LED(8)
green = LED(7)
green.on()
amber.off()
red.off()
while True:
    sleep(10)
    green.off()
    amber.on()
    sleep(1)
    amber.off()
    red.on()
    sleep(10)
    amber.on()
    sleep(1)
    green.on()
    amber.off()
    red.off()