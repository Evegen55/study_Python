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
Control inputs
Each pulse to the STEP input corresponds to one microstep of the stepper motor in the direction selected by the DIR pin.
Note that the STEP and DIR pins are not pulled to any particular voltage internally, so you should not
leave either of these pins floating in your application. If you just want rotation in a single direction,
you can tie DIR directly to VCC or GND. The chip has three different inputs for controlling its many power states:
RST, SLP, and EN. For details about these power states, see the datasheet. Please note that the RST pin is floating;
if you are not using the pin, you can connect it to the adjacent SLP pin on the PCB to bring it high and enable the board.
"""
Enable_pin = 16
Step_pin = 18
Direction_pin = 22

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
GPIO.setup(Enable_pin, GPIO.OUT)
GPIO.setup(Step_pin, GPIO.OUT)
GPIO.setup(Direction_pin, GPIO.OUT)

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

def setDirection(direction):
    if direction == 'clockwise':
        GPIO.output(Direction_pin, 0)
    if direction == 'counterclock-wise':
        GPIO.output(Direction_pin, 1)

def doStepWithDelay(delay):
    GPIO.output(Step_pin, 1)
    time.sleep(delay)
    GPIO.output(Step_pin, 0)

def enableDriver():
    GPIO.output(Enable_pin, 1)

def disableDriver():
    GPIO.output(Enable_pin, 0)