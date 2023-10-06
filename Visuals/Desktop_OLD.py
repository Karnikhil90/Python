from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

class Desktop:
    def __init__(self):
        # Universal background color
                # All Constant 
        self.button_color = '#D1F2EB'
        self.baground_Border_color = '#2C3E50'
        self.colors = [
            '#E6BE8A', '#20B2AA', '#C5E17A', '#20B2AA', '#87CEEB',
            '#E59866', '#F9E79F', '#A2D9CE', '#D2B4DE', '#73C6B6',
            '#138D75', '#1F618D', '#00FF00', '#D35400', '#F39C12'
        ]
        self.bg_color = self.colors[0]
        self.current_color_index = 0

        self.USER_NAME = 'User' # NOT a constant IF can be changed by user

        TITLE = self.USER_NAME +" -v0.1.5" 
        self.window = Tk()
        self.window.configure(bg=self.bg_color)
        self.window.geometry('640x420')
        self.window.title(TITLE)
        self.window.resizable(False, False)
        self.styles1 = font.Font(family='Georgia', size=14, weight='bold')
        self.styles2 = font.Font(size=20)
        self.styles3 = font.Font(family='Trebuchet MS', size=14, weight='bold')

        # Create the Delta_BG frame here
        self.Delta_BG = Frame(self.window, bg=self.bg_color)

        self.default_page = Frame(self.window, bg=self.bg_color)
        self.default_page.grid(row=0, column=0, sticky="nsew")

        self.Def_page = Label(self.default_page, text="Main Page", font=self.styles1, bg=self.bg_color)
        self.Def_page.pack()

        self.Settings()
        self.default_page.tkraise()
        self.cal_icon()

    def HOME_BUTTON(self, frame):
        home_button = Button(frame,
                             text="HOME",
                             command=self.Default_Main,
                             font=self.styles1,
                             bg=self.button_color
                             )
        home_button.pack(pady=10)

    def Settings(self):
        self.settings_page = Frame(self.window, bg=self.bg_color)
        self.settings_page.grid(row=0, column=0, sticky="nsew")

        settings_label = Label(self.settings_page, text="Setting Page",
                            font=self.styles1, bg=self.bg_color,
                            bd=5, borderwidth=5)
        settings_label.pack()
        self.HOME_BUTTON(self.settings_page) # Back To Main page 

        settings_button = Button(self.settings_page,
                               text="Background color",
                               command=self.change_background_color,
                               font=self.styles1,
                               bg=self.button_color
                               )
        settings_button.pack(pady=10)

        Setting_About_Butn = Button(self.settings_page,
                               text="About",
                               command=self.Setting_About_Fea,
                               font=self.styles1,
                               bg=self.button_color
                               )
        Setting_About_Butn.pack(pady=10)

    def change_background_color(self):
        self.color_page = Frame(self.window, bg=self.bg_color)
        self.color_page.grid(row=0, column=0, sticky="nsew")

        self.color_label = Label(self.color_page, text="Change Background Color",
                        font=self.styles1, bg=self.bg_color,
                        bd=5, borderwidth=5)
        self.color_label.pack()

        change_color_button = Button(self.color_page,
                                text="Next",
                                command=self.change_next_background_color,
                                font=self.styles1,
                                bg=self.button_color
                                )
        change_color_button.pack(pady=10)

        self.HOME_BUTTON(self.color_page)

        back_color_button = Button(self.color_page,
                                   text="Back",
                                   command=self.change_previous_background_color,
                                   font=self.styles1,
                                   bg=self.button_color
                                   )
        back_color_button.pack(pady=10)

    def change_previous_background_color(self):
        self.current_color_index -= 1
        if self.current_color_index < 0:
            self.current_color_index = len(self.colors) - 1
        new_color = self.colors[self.current_color_index]
        self.change_bg(new_color)

    def Setting_About_Fea(self):
        self.Delta_BG = Frame(self.window, bg=self.bg_color)
        self.Delta_BG.grid(row=0, column=0, sticky="nsew")

        setting_label = Label(self.Delta_BG, 
                              text="About Your Device",
                              font=self.styles1,
                              bg=self.bg_color,
                              bd=50,
                              highlightbackground=self.baground_Border_color,
                              relief="solid",
                              borderwidth=5)
        setting_label.pack()

        back_button = Button(self.Delta_BG,
                               text="Back",
                               command=self.Settings,
                               font=self.styles1,
                               bg=self.button_color
                               )
        back_button.pack(pady=20)

        # Device Data Print Out
        UserName = "PC Name : "+ self.USER_NAME
        device_name_OutPut = Label(self.Delta_BG,
                                   text=UserName,
                                   font=self.styles3,
                                   bg=self.button_color,
                                   )
        device_name_OutPut.place(x=10,y=100)
        

    def Default_Main(self):
        self.default_page.tkraise()

    def cal_icon(self):
        app_Size = 40
        image = Image.open('importImage\\calc.png')
        image = image.resize((app_Size,app_Size))
        self.icon = ImageTk.PhotoImage(image)

        Setting_butn = Button(self.default_page,
                                   command=self.Settings,
                                   bg=self.button_color,
                                   image=self.icon)
        Setting_butn.place(x=10, y=40)

        PowerOFF_image = Image.open('importImage\\Power.png')
        PowerOFF_image = PowerOFF_image.resize((app_Size,app_Size))
        self.icon2 = ImageTk.PhotoImage(PowerOFF_image)
        
        PowerOFF_butn = Button(self.default_page,
                                   command=self.PowerOFF_butn,
                                   bg=self.button_color,
                                   image=self.icon2)
        PowerOFF_butn.place(x=60, y=40)

    def PowerOFF_butn(self):
        self.window.destroy()

    def change_next_background_color(self):
        self.current_color_index += 1
        if self.current_color_index > len(self.colors) - 1:
            self.current_color_index = 0
        new_color = self.colors[self.current_color_index]
        self.change_bg(new_color)

    def change_bg(self, color):
        print(color)
        self.bg_color = color
        self.color_page.configure(bg=color)
        self.settings_page.configure(bg=color)
        self.window.configure(bg=color)
        self.Delta_BG.configure(bg=color)
        self.default_page.configure(bg=color)
        self.Def_page.configure(bg=color)
        self.color_label.configure(bg=color)

    def run(self):
        print('Start')
        self.window.mainloop()
        print('End')

if __name__ == "__main__":
    app = Desktop()
    app.run()
  