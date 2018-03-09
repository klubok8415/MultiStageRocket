from tkinter import *
from custom_canvas import Displayer
from calculator import Calculator


class MainFrame(Frame):
    def __init__(self):
        self.root = Tk()
        super(MainFrame, self).__init__(self.root)
        self.calculator = Calculator(3)

        self.displayer_frame = Frame(self.root)

        self.displayer1 = Displayer(self.displayer_frame)
        self.displayer1.grid(row=0)
        self.displayer2 = Displayer(self.displayer_frame)
        self.displayer2.grid(row=0, column=1)

        self.stage1_frame = Frame(self.root)
        self.stage1_frame.grid(row=0, column=0)

        self.stage1_diameter_label = Label(self.stage1_frame, text='diameter')
        self.stage1_diameter_label.grid(row=0, column=0)
        self.stage1_diameter_entry = Entry(self.stage1_frame)
        self.stage1_diameter_entry.grid(row=0, column=1)
        self.stage1_force_label = Label(self.stage1_frame, text='force')
        self.stage1_force_label.grid(row=1, column=0)
        self.stage1_force_entry = Entry(self.stage1_frame)
        self.stage1_force_entry.grid(row=1, column=1)
        self.stage1_consumption_label = Label(self.stage1_frame, text='consumption')
        self.stage1_consumption_label.grid(row=2, column=0)
        self.stage1_consumption = Entry(self.stage1_frame)
        self.stage1_consumption.grid(row=2, column=1)
        self.stage1_time_label = Label(self.stage1_frame, text='time')
        self.stage1_time_label.grid(row=3, column=0)
        self.stage1_time = Entry(self.stage1_frame)
        self.stage1_time.grid(row=3, column=1)
        self.stage1_initial_mass_label = Label(self.stage1_frame, text='initial_mass')
        self.stage1_initial_mass_label.grid(row=4, column=0)
        self.stage1_initial_mass = Entry(self.stage1_frame)
        self.stage1_initial_mass.grid(row=4, column=1)
        self.stage1_final_mass_label = Label(self.stage1_frame, text='final_mass')
        self.stage1_final_mass_label.grid(row=5, column=0)
        self.stage1_final_mass = Entry(self.stage1_frame)
        self.stage1_final_mass.grid(row=5, column=1)
        self.stage1_time_parachute_label = Label(self.stage1_frame, text='time_parachute')
        self.stage1_time_parachute_label.grid(row=6, column=0)
        self.stage1_time_parachute = Entry(self.stage1_frame)
        self.stage1_time_parachute.grid(row=6, column=1)
        self.stage1_diameter_parachute_label = Label(self.stage1_frame, text='diameter_parachute')
        self.stage1_diameter_parachute_label.grid(row=7, column=0)
        self.stage1_diameter_parachute_entry = Entry(self.stage1_frame)
        self.stage1_diameter_parachute_entry.grid(row=7, column=1)
        self.stage1_resistance_parachute_label = Label(self.stage1_frame, text='resistance_parachute')
        self.stage1_resistance_parachute_label.grid(row=8, column=0)
        self.stage1_resistance_parachute_entry = Entry(self.stage1_frame)
        self.stage1_resistance_parachute_entry.grid(row=8, column=1)

        self.stage2_frame = Frame(self.root, padx=50)
        self.stage2_frame.grid(row=0, column=1)

        self.stage2_diameter_label = Label(self.stage2_frame, text='diameter')
        self.stage2_diameter_label.grid(row=0, column=0)
        self.stage2_diameter_entry = Entry(self.stage2_frame)
        self.stage2_diameter_entry.grid(row=0, column=1)
        self.stage2_force_label = Label(self.stage2_frame, text='force')
        self.stage2_force_label.grid(row=1, column=0)
        self.stage2_force_entry = Entry(self.stage2_frame)
        self.stage2_force_entry.grid(row=1, column=1)
        self.stage2_consumption_label = Label(self.stage2_frame, text='consumption')
        self.stage2_consumption_label.grid(row=2, column=0)
        self.stage2_consumption = Entry(self.stage2_frame)
        self.stage2_consumption.grid(row=2, column=1)
        self.stage2_time_label = Label(self.stage2_frame, text='time')
        self.stage2_time_label.grid(row=3, column=0)
        self.stage2_time = Entry(self.stage2_frame)
        self.stage2_time.grid(row=3, column=1)
        self.stage2_initial_mass_label = Label(self.stage2_frame, text='initial_mass')
        self.stage2_initial_mass_label.grid(row=4, column=0)
        self.stage2_initial_mass = Entry(self.stage2_frame)
        self.stage2_initial_mass.grid(row=4, column=1)
        self.stage2_final_mass_label = Label(self.stage2_frame, text='final_mass')
        self.stage2_final_mass_label.grid(row=5, column=0)
        self.stage2_final_mass = Entry(self.stage2_frame)
        self.stage2_final_mass.grid(row=5, column=1)
        self.stage2_time_parachute_label = Label(self.stage2_frame, text='time_parachute')
        self.stage2_time_parachute_label.grid(row=6, column=0)
        self.stage2_time_parachute = Entry(self.stage2_frame)
        self.stage2_time_parachute.grid(row=6, column=1)
        self.stage2_diameter_parachute_label = Label(self.stage2_frame, text='diameter_parachute')
        self.stage2_diameter_parachute_label.grid(row=7, column=0)
        self.stage2_diameter_parachute_entry = Entry(self.stage2_frame)
        self.stage2_diameter_parachute_entry.grid(row=7, column=1)
        self.stage2_resistance_parachute_label = Label(self.stage2_frame, text='resistance_parachuter')
        self.stage2_resistance_parachute_label.grid(row=8, column=0)
        self.stage2_resistance_parachute_entry = Entry(self.stage2_frame)
        self.stage2_resistance_parachute_entry.grid(row=8, column=1)

        self.stage3_frame = Frame(self.root)
        self.stage3_frame.grid(row=0, column=2)

        self.stage3_diameter_label = Label(self.stage3_frame, text='diameter')
        self.stage3_diameter_label.grid(row=0, column=0)
        self.stage3_diameter_entry = Entry(self.stage3_frame)
        self.stage3_diameter_entry.grid(row=0, column=1)
        self.stage3_force_label = Label(self.stage3_frame, text='force')
        self.stage3_force_label.grid(row=1, column=0)
        self.stage3_force_entry = Entry(self.stage3_frame)
        self.stage3_force_entry.grid(row=1, column=1)
        self.stage3_consumption_label = Label(self.stage3_frame, text='consumption')
        self.stage3_consumption_label.grid(row=2, column=0)
        self.stage3_consumption = Entry(self.stage3_frame)
        self.stage3_consumption.grid(row=2, column=1)
        self.stage3_time_label = Label(self.stage3_frame, text='time')
        self.stage3_time_label.grid(row=3, column=0)
        self.stage3_time = Entry(self.stage3_frame)
        self.stage3_time.grid(row=3, column=1)
        self.stage3_initial_mass_label = Label(self.stage3_frame, text='initial_mass')
        self.stage3_initial_mass_label.grid(row=4, column=0)
        self.stage3_initial_mass = Entry(self.stage3_frame)
        self.stage3_initial_mass.grid(row=4, column=1)
        self.stage3_final_mass_label = Label(self.stage3_frame, text='final_mass')
        self.stage3_final_mass_label.grid(row=5, column=0)
        self.stage3_final_mass = Entry(self.stage3_frame)
        self.stage3_final_mass.grid(row=5, column=1)
        self.stage3_time_parachute_label = Label(self.stage3_frame, text='time_parachute')
        self.stage3_time_parachute_label.grid(row=6, column=0)
        self.stage3_time_parachute = Entry(self.stage3_frame)
        self.stage3_time_parachute.grid(row=6, column=1)
        self.stage3_diameter_parachute_label = Label(self.stage3_frame, text='diameter_parachute')
        self.stage3_diameter_parachute_label.grid(row=7, column=0)
        self.stage3_diameter_parachute_entry = Entry(self.stage3_frame)
        self.stage3_diameter_parachute_entry.grid(row=7, column=1)
        self.stage3_resistance_parachute_label = Label(self.stage3_frame, text='resistance_parachute')
        self.stage3_resistance_parachute_label.grid(row=8, column=0)
        self.stage3_resistance_parachute_entry = Entry(self.stage3_frame)
        self.stage3_resistance_parachute_entry.grid(row=8, column=1)

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
            displayer.add_function_data()
            displayer.update_graph()
        self.root.mainloop()


if __name__ == '__main__':
    MainFrame().start()
