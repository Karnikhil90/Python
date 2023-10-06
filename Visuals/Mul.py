from tkinter import *
from tkinter import font

TITLE : str = "Multiple Page"

win = Tk()

sty = font.Font=('Georgia', 14, 'bold')
sty1 = font.Font=('Italic', 14, )


win.geometry('380x500')
# win.resizable(False,False)
win.title(TITLE)
win.config(bg='black')

page1 = Frame(win)
page2 = Frame(win)
page3 = Frame(win)


page1.grid(row=0, column=0,sticky="nsew") 
page2.grid(row=0, column=0,sticky="nsew")
page3.grid(row=0, column=0,sticky="nsew")

lb1 = Label(page1, 
            text="Im the main page",
            font=sty,
            fg='#F4D03F',
            bg='#E74C3C',
            )
lb1.pack(pady=0)

lb2 = Label(page2, 
            text="Im the Setting page",
            font=sty,
            fg='#F4D03F',
            bg='#E74C3C',
            )
lb2.pack(padx=0,pady=0)

lb3 = Label(page3, 
            text="Im the #3 page",
            font=sty,
            fg='#F4D03F',
            bg='#E74C3C',
            compound=BOTTOM
            )
lb3.pack(pady=0)

page1.tkraise()


bt1 = Button(page1,
             command=lambda: page2.tkraise(),
             text="To Setting",
             font=sty1)
bt1.pack()

bt2 = Button(page2,
             command=lambda: page3.tkraise(),
             text="To Third",
             font=sty1)
bt2.pack()

bt3 = Button(page2,
             command=lambda: page1.tkraise(),
             text="To Main",
             font=sty1)
bt3.pack()

bt4 = Button(page3,
             command=lambda: page1.tkraise(),
             text="To main",
             font=sty1)
bt4.pack()

win.mainloop()