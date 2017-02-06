'''
Created on Jan 31, 2017

@author: Evgenii_Lartcev
'''
from Tkinter import *
from stepper_L293_bipolar import *

# GUI definition
root = Tk()
w = 600 # width for the Tk root
h = 300 # height for the Tk root
varDelay = StringVar()

def center_window_with_dimensions(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def updateAndPrintValues(duty):
    # print varDelay.get() #for test purpose
    return

# for 1 step to left or right if button fired once
# for many steps if button fired longer time
# get delay from the scale
# delay in steps as the same as delay between firing button
def rotate_left():
    delay_in_millisecs_as_string = varDelay.get()
    delay_in_secs_as_float = float (varDelay.get()) /1000    
    button_rotate_left.configure(repeatinterval = delay_in_millisecs_as_string)
    backwards(delay_in_secs_as_float, 1)
    print 'left ' , varDelay.get(), delay_in_millisecs_as_string, delay_in_secs_as_float #for test purpose

def rotate_right():
    delay_in_millisecs_as_string = varDelay.get()
    delay_in_secs_as_float = float (varDelay.get()) /1000
    
    button_rotate_right.configure(repeatinterval = delay_in_millisecs_as_string)
    forward(delay_in_secs_as_float, 1)
    print 'right ' , varDelay.get(), delay_in_millisecs_as_string, delay_in_secs_as_float #for test purpose

#TODO instead of two previous functions
def rotateTo(direction):
    delay_in_millisecs_as_string = varDelay.get()
    delay_in_secs_as_float = float (varDelay.get()) /1000
    if direction == 'left':
        button_rotate_left.configure(repeatinterval = delay_in_millisecs_as_string)
        backwards(delay_in_secs_as_float, 1)
        #print 'left ' , varDelay.get(), delay_in_millisecs_as_string, delay_in_secs_as_float #for test purpose
    elif direction == 'right':
        button_rotate_right.configure(repeatinterval = delay_in_millisecs_as_string)
        forward(delay_in_secs_as_float, 1)  
        #print 'right ' , varDelay.get(), delay_in_millisecs_as_string, delay_in_secs_as_float #for test purpose
    
# Buttons
button_rotate_left = Button(root, text="Turn motor left", width=20,height=5, bg="green",fg="black",
                             command = rotate_left, repeatdelay="500", repeatinterval = "1000")

button_rotate_right = Button(root, text="Turn motor right", width=20,height=5, bg="blue",fg="black",
                             command = rotate_right, repeatdelay="500", repeatinterval = "1000")

# Scales   
scaleDelay = Scale(root, from_= 1, to = 100, orient = HORIZONTAL, length = 300, width = 50, bg="cyan",fg="black",
                    variable = varDelay, command = updateAndPrintValues)

# add stuff to the main board
button_rotate_left.pack(side = 'left')
button_rotate_right.pack(side = 'right')
scaleDelay.pack(side = 'bottom')

# start GUI
center_window_with_dimensions(w, h)
root.mainloop()
clearGPIO() # cleanup all GPIO using incapsulating function from RoboticArm.stepper_L293_bipolar
