import tkinter as tk
from index import *
from PIL import Image,ImageTk

class LoginApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.configure(bg='#0C134F')
        self.window.geometry('380x500')
        self.window.title('Login Display')
        self.window.resizable(False,False,)

       # Open and resize the image using PIL
        image = Image.open('GUI_PYTHON\\click_me.png')
        image = image.resize((100, 100)) 
        self.icon = ImageTk.PhotoImage(image)

        self.window.iconphoto(True, self.icon)

        self.setup_ui()

    def setup_ui(self):
        display_heading = tk.Label(self.window,
                                   text="SignInXpert",
                                   font=('Arial', 25, 'bold'),
                                   fg='#D4ADFC',
                                   bg='#1D267D',
                                   relief='raised',
                                   bd=12,
                                   padx=100,
                                   pady=0,
                                   compound='bottom'
                                   )
        display_heading.pack()

        line1 = tk.Label(self.window,
                         text='user name',
                         font=('Georgia', 14, 'bold'),
                         fg='#F4D03F',
                         bg='#E74C3C',
                         compound='left'
                         )
        line1.pack()

        self.user_input = tk.Entry(self.window,
                                   width=5 * 3,
                                   bd=5,
                                   font=('Calibri', 20))
        self.user_input.pack()

        line2 = tk.Label(self.window,
                         text='user password',
                         font=('Georgia', 14, 'bold'),
                         fg='#F4D03F',
                         bg='#E74C3C',
                         compound='left'
                         )
        line2.pack()

        self.user_input2 = tk.Entry(self.window,
                                    width=15,
                                    bd=5,
                                    font=('Calibri', 20),
                                    show="*")
        self.user_input2.pack()

        submit_user_input = tk.Button(self.window,
                                      font=('Trebuchet MS', 18),
                                      image=self.icon,
                                      fg='blue',
                                      bg='#0C134F',
                                      activebackground='#E74C3C',
                                      activeforeground='#0C134F',
                                      command=self.submit)
        submit_user_input.pack()

        # Bind events
        self.window.bind('<Return>', self.enter_key)
        self.window.bind('<End>', self.close_window)

    def submit(self):
        username_input = self.user_input.get()
        userpass_input = self.user_input2.get()

        if login(username_input, userpass_input):
            z = "Login Successfully"
        else:
            z = "Login Failed"

        self.print_on_display(z)
        self.user_input.delete(0, tk.END)
        self.user_input2.delete(0, tk.END)

    @staticmethod
    def new_window():
        # Your new_window() function code here
        pass

    def new_window_calling_button(self):
        self.new_window()

    def enter_key(self, event):
        self.submit()

    def close_window(self, event):
        self.window.destroy()

    def print_on_display(self, x):
        
        after_click = tk.Label(self.window,
                               text=x,
                               font=('Trebuchet MS', 14, 'bold'),
                               fg='#E74C3C',
                               bg='#F7DC6F',
                               compound='left'
                               )
        after_click.place(x=130,y=280)

        # Schedule the label to be destroyed after a certain time (e.g., 2000 milliseconds = 2 seconds)
        self.window.after(1500, after_click.destroy)

    def run(self):
        print('Start')
        self.window.mainloop()
        print('End')

if __name__ == "__main__":
    app = LoginApp()
    app.run()
