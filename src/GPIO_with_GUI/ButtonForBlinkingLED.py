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
GPIO.setup(pwmPin, GPIO.OUT)
#PWM setup
pwm = GPIO.PWM(pwmPin, 1)  # Initialize PWM on pwmPin 1Hz frequency
pwm.start(90) #start pwm with duty 90

#update pwm for blinking LED
def update(duty):
    pwm.ChangeDutyCycle(float(duty))
    pwm.ChangeFrequency(float(duty)/10)   
   
w = Scale(root, from_= 0, to = 100, orient = HORIZONTAL, length = 300, width = 50, variable = var, command = update)
w.pack()
root.mainloop()

GPIO.cleanup() # cleanup all GPIO after close Scale
