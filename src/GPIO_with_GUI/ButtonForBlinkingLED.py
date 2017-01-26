'''
Created on Jan 26, 2017

@author: Evgenii_Lartcev
'''
from Tkinter import *
import RPi.GPIO as GPIO
import time

# GUI definition
root = Tk()
var = DoubleVar()
# Pin Definitons:
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency

def update(duty):
    pwm.ChangeDutyCycle(float(duty))
    
w = Scale(root, from_= 0, to = 100, orient = HORIZONTAL, length = 300, width = 50, variable = var, command = update)

w.pack()
root.mainloop()