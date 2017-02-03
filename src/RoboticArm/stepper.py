'''
Created on Jan 18, 2017

@author: Evgenii_Lartcev
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin Definitons:
enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

# Pin Setup:
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.output(enable_pin, 1)

def forward(delay, steps):  
    for i in range(0, steps):
        setStep(1, 0, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(1, 0, 0, 1)
        time.sleep(delay)

def backwards(delay, steps):  
    for i in range(0, steps):
        setStep(1, 0, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 0, 1)
        time.sleep(delay)
        setStep(0, 1, 1, 0)
        time.sleep(delay)
        setStep(1, 0, 1, 0)
        time.sleep(delay)
  
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def clearGPIO():
    GPIO.cleanup()

def turn_stepper_from_CLI():
    print("Here we go! Press CTRL+C to exit")
    try:
        while True:
            delay = raw_input("Delay between steps (milliseconds)?")
            steps = raw_input("How many steps forward? ")
            forward(int(delay) / 1000.0, int(steps))
            steps = raw_input("How many steps backwards? ")
            backwards(int(delay) / 1000.0, int(steps))
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPIO
        
#do it from command line interface:
#turn_stepper_from_CLI()