from tkinter import *
from custom_canvas import Displayer


class MainFrame(Frame):
    def __init__(self):
        self.root = Tk()
        super(MainFrame, self).__init__(self.root)

        self.displayer = Displayer(self.root)
        self.displayer.pack()

        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.size_x_prev = self.root.winfo_width()
        self.size_y_prev = self.root.winfo_height()
        self.root.bind('<Configure>', self.root_resize)

    def root_resize(self, event):
        delta_x = self.root.winfo_width() - self.size_x_prev
        delta_y = self.root.winfo_height() - self.size_y_prev
        if delta_x != 0 or delta_y != 0:
            self.displayer.size_x += delta_x
            self.displayer.size_y += delta_y
            self.displayer.config(width=self.displayer.size_x + self.displayer.border,
                                  height=self.displayer.size_y + self.displayer.border)
            self.displayer.delete(ALL)
            self.displayer.update_graph()
            self.size_x_prev += delta_x
            self.size_y_prev += delta_y

    def start(self):
        self.displayer.update_graph()
        self.displayer.add_function_data()
        self.root.mainloop()


if __name__ == '__main__':
    MainFrame().start()
