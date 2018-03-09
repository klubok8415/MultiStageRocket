from tkinter import *
from custom_canvas import Displayer


class MainFrame(Frame):
    def __init__(self):
        self.root = Tk()
        super(MainFrame, self).__init__(self.root)

        self.displayer1 = Displayer(self.root)
        self.displayer1.grid(row=0)
        self.displayer2 = Displayer(self.root)
        self.displayer2.grid(row=0, column=1)

        self.displayers_list = [self.displayer1, self.displayer2]

        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.size_x_prev = self.root.winfo_width()
        self.size_y_prev = self.root.winfo_height()
        self.root.bind('<Configure>', self.root_resize)

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
            displayer.add_function_data()
            displayer.update_graph()
        self.root.mainloop()


if __name__ == '__main__':
    MainFrame().start()
