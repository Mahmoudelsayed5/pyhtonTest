from tkinter import *
from datetime import datetime

date = datetime.now().year

def year_calculation() :
    x = int(entry1.get())
    output = int(date - X)
    

window = Tk()
window.title('My project')
window.config()
window.geometry('800x600')

label1 = Label(window, text='enter your age : ')
label1.place(x=100,y=100)

label2 = Label(window, text='output : ')
label2.place(x=100,y=200)

entry1 = Entry(window, width=30)
entry1.place(x=250, y=100)

button1 = Button(window, text='click to get the year of your birth', command=year_calculation)
button1.place(x=400, y=400)

window.mainloop()