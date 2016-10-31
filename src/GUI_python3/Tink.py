from tkinter import *
root = Tk()
root.geometry('800x600')
#c = Canvas(root, width=800, height=600)
#c.pack()
#r = c.create_rectangle(0, 0, 50, 50, fill='red', outline='red')
def Hello(event):
    print("Yet another hello world")

btn = Button(root,                  #родительское окно
             text="Click me",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                          #расположить кнопку на главном окне
root.mainloop()
