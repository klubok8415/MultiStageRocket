from tkinter import *
from custom_canvas import Displayer
from calculator import Calculator


class MainFrame(Frame):
    def __init__(self):
        self.root = Tk()
        super(MainFrame, self).__init__(self.root)
        self.calculator = Calculator()

        self.displayer1 = Displayer(self.root)
        self.displayer1.grid(row=0)
        self.displayer2 = Displayer(self.root)
        self.displayer2.grid(row=0, column=1)

        self.entry1 = Entry()
        self.entry1.pack()
        self.entry2 = Entry()
        self.entry2.pack()
        self.but = Button(command=self.on_click)
        self.but.pack()

        self.displayers_list = [self.displayer1, self.displayer2]

        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.size_x_prev = self.root.winfo_width()
        self.size_y_prev = self.root.winfo_height()
        self.root.bind('<Configure>', self.root_resize)

    def on_click(self):
        self.calculator.add_data()
        self.calculator.add_data()

    def root_resize(self, event):
        delta_x = (self.root.winfo_width() - self.size_x_prev) / len(self.displayers_list)
        delta_y = (self.root.winfo_height() - self.size_y_prev) / len(self.displayers_list)
        if delta_x != 0 or delta_y != 0:
            for displayer in self.displayers_list:
                displayer.size_x += delta_x
                displayer.size_y += delta_y
                displayer.config(width=displayer.size_x + displayer.border,
                                      height=displayer.size_y + displayer.border)
                displayer.delete(ALL)
                displayer.update_graph()
                self.size_x_prev += delta_x
                self.size_y_prev += delta_y

    def start(self):
        for displayer in self.displayers_list:
            displayer.update_graph()
            displayer.add_function_data()
        self.root.mainloop()


if __name__ == '__main__':
    MainFrame().start()
