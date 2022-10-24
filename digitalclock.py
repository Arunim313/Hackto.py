
from tkinter import *
from tkinter.ttk import *


from time import strftime


root = Tk()
root.title('DigitalClock')


def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)


lbl = Label(root, font = ('Arial', 32, 'bold'),
			background = 'blue',
			foreground = 'white')


lbl.pack(anchor = 'center')
time()

mainloop()
