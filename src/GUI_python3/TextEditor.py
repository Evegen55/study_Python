'''
Created on Oct 31, 2016

@author: Evgenii_Lartcev
'''
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
from tkinter.ttk import *

root = Tk()

# define options for opening or saving a file by default
options = {}
options['defaultextension'] = '.txt'
options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
options['initialdir'] = '~/'
options['initialfile'] = 'myfile.txt'
options['parent'] = root
options['title'] = 'This is a title'


def Quit(ev):
    global root
    root.destroy()
    
def LoadFile(ev):
    # get filename
    filename = asksaveasfilename(**options) 
    file = open(filename, mode = 'r')
    if filename is None:
        return
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', open(file, 'r').read())
    
def SaveFile(ev):
    # get filename
    filename = asksaveasfilename(**options)     
    if filename is None:
        return
    file = open(filename, mode = 'w')   
    file.write(textbox.get('1.0', 'end'))
    file.close()


panelFrame = Frame(root, height = 60)
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

loadBtn = Button(panelFrame, text = 'Load')
saveBtn = Button(panelFrame, text = 'Save')
quitBtn = Button(panelFrame, text = 'Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 10, y = 10, width = 40, height = 40)
saveBtn.place(x = 60, y = 10, width = 40, height = 40)
quitBtn.place(x = 110, y = 10, width = 40, height = 40)

root.mainloop()