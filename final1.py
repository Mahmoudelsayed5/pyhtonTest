from tkinter import *
import final2


def check() :
    user_text = entry1.get().capitalize()
    with open( r'C:\Users\mahmo_pfubzz6\Downloads\Boycott Brands.txt', 'r') as file :
        content = file.read()

        if user_text in content :
            label2['text'] = 'Output : The brand you entered is a boycott'

        else :
            window.destroy()
            final2.second_page()
            

def close():
    window.destroy()
    
def main_page():
    global window
    global entry1
    global label2
    window = Tk()
    window.title('My project')
    window.config(bg='LightSteelBlue3')
    window.geometry('600x400')

    label1 = Label(window, text='Enter name : ', bg='LightSteelBlue3', font=('SansSerif',15))
    label1.place(x=50,y=50)

    label2 = Label(window, text='Output : ', bg='LightSteelBlue3', font=('SansSerif',15))
    label2.place(x=50,y=100)

    entry1 = Entry(window, width=30)
    entry1.place(x=200, y=55)
    # entry1.pack(ipady=7)

    button1 = Button(window, text='Check if the brand exists', command=check, bg='LightSteelBlue3', font=('SansSerif',15))
    button1.place(x=300, y=300)

    button2 = Button(window, text='Close', command=close, bg='LightSteelBlue3', font=('SansSerif',15))
    button2.place(x=380, y=350)

    window.mainloop()

if __name__ == "__main__" :
    main_page()