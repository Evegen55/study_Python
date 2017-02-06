'''
Created on Feb 6, 2017
@author: Evgenii_Lartcev
This breakout board for Allegro’s A4988 microstepping bipolar stepper motor driver features adjustable current limiting,
over-current and over-temperature protection, and five different microstep resolutions (down to 1/16-step).
It operates from 8 V to 35 V and can deliver up to approximately 1 A per phase without a heat sink or forced air flow
(it is rated for 2 A per coil with sufficient additional cooling).
https://www.pololu.com/product/1182
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Pin Definitons:
Microstep_MS1 = 11
Microstep_MS2 = 13
Microstep_MS3 = 15

"""
MS1	    MS2	    MS3	    Microstep Resolution
Low	    Low	    Low	    Full step
High	Low	    Low	    Half step
Low	    High	Low	    Quarter step
High	High	Low	    Eighth step
High	High	High	Sixteenth step
"""

# Pin Setup:
GPIO.setup(Microstep_MS1, GPIO.OUT)
GPIO.setup(Microstep_MS2, GPIO.OUT)
GPIO.setup(Microstep_MS3, GPIO.OUT)

def setResolution(resolution):
    if resolution == 'full':
        GPIO.output(Microstep_MS1, 0)
        GPIO.output(Microstep_MS2, 0)
        GPIO.output(Microstep_MS3, 0)
    if resolution == 'half':
        GPIO.output(Microstep_MS1, 1)
        GPIO.output(Microstep_MS2, 0)
        GPIO.output(Microstep_MS3, 0)
    if resolution == 'quarter':
        GPIO.output(Microstep_MS1, 0)
        GPIO.output(Microstep_MS2, 1)
        GPIO.output(Microstep_MS3, 0)
    if resolution == 'eighth':
        GPIO.output(Microstep_MS1, 1)
        GPIO.output(Microstep_MS2, 1)
        GPIO.output(Microstep_MS3, 0)
    if resolution == 'sixteenth':
        GPIO.output(Microstep_MS1, 1)
        GPIO.output(Microstep_MS2, 1)
        GPIO.output(Microstep_MS3, 1)