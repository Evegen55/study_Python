#    http://pyinmyeye.blogspot.ru/2012/08/tkinter-spinbox-demo.html
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//spinbox.html
#    http://www.tcl.tk/man/tcl8.5/TkCmd/spinbox.htm
from tkinter import *
from tkinter import ttk
 
from demopanels import MsgPanel, SeeDismissPanel
 
class SpinboxDemo(ttk.Frame):
     
    def __init__(self, isapp=True, name='spinboxdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Spinbox Demo')
        self.isapp = isapp
        self._create_widgets()
         
    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self,
                     ["Three different spin-boxes are displayed below. ",
                      "The first, which is 'read only', displays a different ",
                      "background colour.\n",
                      "Select a value using the up/down arrowhead keys ",
                      "or keyboard up/down arrow keys."])
             
            SeeDismissPanel(self)
         
        self._create_demo_panel()
         
    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)
             
        # create spinboxes (not implemented in ttk)
        sb1 = Spinbox(from_=1, to=10, width=10, state='readonly',
                      readonlybackground='yellow')
        sb2 = Spinbox(from_=0, to=3, increment=.5, format='%05.2f',
                      width=10)
         
        cities = ('Toronto', 'Ottawa', 'Montreal', 'Vancouver', 'St. John')
        sb3 = Spinbox(values=sorted(cities), width=len(max(cities))+2)
         
        # position and display
        sb1.pack(in_=demoPanel, side=TOP, pady=5, padx=10)
        sb2.pack(in_=demoPanel, side=TOP, pady=5, padx=10)
        sb3.pack(in_=demoPanel, side=TOP, pady=5, padx=10)
 
if __name__ == '__main__':
    SpinboxDemo().mainloop()
