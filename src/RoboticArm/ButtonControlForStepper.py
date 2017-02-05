'''
Created on Jan 31, 2017

@author: Evgenii_Lartcev
'''
from Tkinter import *
#from stepper import *

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

# for 1 step with delay from scale    
def rotate_left():
    #v = getDelay()
    print 'left ' , varDelay.get() #for test purpose
    button_rotate_left.configure(repeatinterval = varDelay.get())
    #backwards(v, 1)
    
# for 1 step with delay from scale 
def rotate_right():
    #v = getDelay()
    print 'right ' , varDelay.get() #for test purpose
    button_rotate_right.configure(repeatinterval = varDelay.get())
    #forward(v, 1)
    
def getDelay():
    return varDelay.get() / 100

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
#clearGPIO() # cleanup all GPIO using incapsulating function from RoboticArm.stepper
