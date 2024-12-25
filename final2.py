from tkinter import *
import final1


def check_and_write() :
    user_text = entry1.get().capitalize()
    try :
            with open(r'C:\Users\mahmo_pfubzz6\Downloads\Boycott Brands.txt', 'r') as file :
                lines = file.readlines()
                if user_text + "\n" in lines :
                    label2['text'] = 'Output : The brand you entered already exists'
                    return
    except FileNotFoundError:
        pass
    with open(r'C:\Users\mahmo_pfubzz6\Downloads\Boycott Brands.txt', 'a') as file :
        file.write(user_text + "\n")
    label2['text'] = 'Output : Added successfully, go back to check it'

def Back():
    window.destroy()
    final1.main_page()
    
def second_page() :
    global window
    global label1
    global label2
    global entry1
    window = Tk()
    window.title('My project')
    window.config(bg='LightSteelBlue3')
    window.geometry('600x400')

    label1 = Label(window, text='The brand you entered is not a boycott..enter it here', bg='LightSteelBlue3', font=('SansSerif',15))
    label1.place(x=50,y=50)

    label2 = Label(window, text='Output : ', bg='LightSteelBlue3', font=('SansSerif',15))
    label2.place(x=50,y=200)

    entry1 = Entry(window, width=30)
    entry1.place(x=50, y=100)
    # entry1.pack(ipady=7)

    button1 = Button(window, text='Add the Brand', command=check_and_write, bg='LightSteelBlue3', font=('SansSerif',15))
    button1.place(x=300, y=300)

    button2 = Button(window, text='Back', command=Back, bg='LightSteelBlue3', font=('SansSerif',15))
    button2.place(x=380, y=350)

    window.mainloop()