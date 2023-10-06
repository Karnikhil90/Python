from tkinter import *

class ColorChanger:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Color Changer")
        self.root.geometry("400x200")
        self.colors = [
            '#E6BE8A', '#20B2AA', '#C5E17A', '#20B2AA', '#87CEEB',
            '#E59866', '#F9E79F', '#A2D9CE', '#D2B4DE', '#73C6B6'
        ]
        self.current_color_index = 0

        self.main_frame = Frame(self.root, bg=self.colors[self.current_color_index])
        self.main_frame.pack(fill=BOTH, expand=True)

        self.heading_label = Label(self.main_frame, text="Background Color Changing Option", font=("Arial", 14), bg=self.colors[self.current_color_index])
        self.heading_label.pack(pady=10)

        self.next_color_button = Button(self.main_frame, text="Next", command=self.change_next_background_color)
        self.next_color_button.pack(pady=5)

        self.back_color_button = Button(self.main_frame, text="Back", command=self.change_previous_background_color)
        self.back_color_button.pack(pady=5)

    def change_next_background_color(self):
        self.current_color_index += 1
        if self.current_color_index > len(self.colors) - 1:
            self.current_color_index = 0
        new_color = self.colors[self.current_color_index]
        self.main_frame.configure(bg=new_color)
        self.heading_label.configure(bg=new_color)

    def change_previous_background_color(self):
        self.current_color_index -= 1
        if self.current_color_index < 0:
            self.current_color_index = len(self.colors) - 1
        new_color = self.colors[self.current_color_index]
        self.main_frame.configure(bg=new_color)
        self.heading_label.configure(bg=new_color)

def main():
    root = Tk()
    app = ColorChanger(root)
    root.mainloop()

if __name__ == "__main__":
    main()
