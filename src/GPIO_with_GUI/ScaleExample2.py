'''
Created on Jan 26, 2017

@author: Evgenii_Lartcev
'''
from Tkinter import *

#GUI definition
root = Tk()
var = DoubleVar()

def update(duty):
    print var.get()
    
w = Scale(root, from_= 0, to = 100, orient = HORIZONTAL, length = 300, width = 50, variable = var, command = update)

#Start GUI
w.pack()
root.mainloop()