'''
Created on Jan 31, 2017

@author: Evgenii_Lartcev
'''
from Tkinter import *
from GPIO.stepper import *

#GUI definition
root = Tk()
w = 600 # width for the Tk root
h = 400 # height for the Tk root
#varDelay = DoubleVar()
varDelay = IntVar()

def center_window_with_dimensions(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def updateAndPritValues(duty):
    #print varDelay.get() #for test purpose
    return

#for 1 step with delay from scale    
def rotate_left():
    #print varDelay.get() #for test purpose
    v = int(varDelay.get()) / 100.0
    backwards(v, 1)
    
#for 1 step with delay from scale 
def rotate_right():
    #print varDelay.get() #for test purpose
    v = int(varDelay.get()) / 100.0
    forward(v, 1)

#Buttons
button_rotate_left = Button(root, text="Turn stepper motor left", width=30,height=5, bg="white",fg="black", command = rotate_left)
button_rotate_right = Button(root, text="Turn stepper motor right", width=30,height=5, bg="white",fg="black", command = rotate_right)
 
#Scales   
scaleDelay = Scale(root, from_= 0, to = 50, orient = HORIZONTAL, length = 300, width = 50, variable = varDelay, command = updateAndPritValues)

# add stuff to the main board
button_rotate_left.pack(side = 'left')
button_rotate_right.pack(side = 'right')
scaleDelay.pack(side = 'bottom')
# start GUI
center_window_with_dimensions(w, h)
root.mainloop()
clearGPIO() # cleanup all GPIO using incapsulating function from GPIO.stepper
