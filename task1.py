from tkinter import *

window = Tk()
window.title('My project')
window.config()
window.geometry('800x600')

label1 = Label(window, text='enter your age : ', bg='red')
label1.place(x=100,y=100)

window.mainloop()