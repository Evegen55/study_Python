'''
Created on Jan 26, 2017

@author: Evgenii_Lartcev
'''
from Tkinter import *

root = Tk()
var = DoubleVar()

w = Scale(root, from_= 0, to = 100, orient = HORIZONTAL, length = 300, width = 50, variable = var)
print var.get()

w.pack()
root.mainloop()