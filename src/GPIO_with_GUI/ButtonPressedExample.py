from Tkinter import * 
running = False
root = Tk()
jobid = None

def start_motor(direction):
    print("starting motor...(%s)" % direction)
    move(direction)

def stop_motor():
    global jobid
    root.after_cancel(jobid)
    print("stopping motor...")

def move(direction):
    global jobid
    print("Moving (%s)" % direction)
    jobid = root.after(1000, move, direction)

for direction in ("forward", "backward"):
    button = Button(root, text=direction)
    button.pack(side=LEFT)
    button.bind('<ButtonPress-1>', lambda event, direction=direction: start_motor(direction))
    button.bind('<ButtonRelease-1>', lambda event: stop_motor())

root.mainloop()