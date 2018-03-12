from tkinter import *
from gui.CustomCanvas import CustomCanvas
from gui.EntryWithBackgroundText import EntryWithBackgroundText
from calculator import Calculator


class MainFrame(Frame):
    def __init__(self):
        self.root = Tk()
        super(MainFrame, self).__init__(self.root)
        self.calculator = Calculator(stages=3)

        self.stages_frame = Frame(self.root)
        self.stages_frame.pack(fill=X, expand=1)
        self.displayer_frame = Frame(self.root, pady=20)
        self.displayer_frame.pack()

        self.displayer1 = CustomCanvas(self.displayer_frame)
        self.displayer1.grid(row=0)
        self.displayer2 = CustomCanvas(self.displayer_frame)
        self.displayer2.grid(row=0, column=1)

        self.general_data_frame = Frame(self.stages_frame, padx=25)
        self.general_data_frame.pack(side=LEFT, fill=X, expand=1)

        self.general_data_title = Label(self.general_data_frame, text='general data')
        self.general_data_title.grid(row=0, columnspan=2)
        self.parachute_diameter_label = Label(self.general_data_frame, text='parachute diameter')
        self.parachute_diameter_label.grid(row=1, column=0)
        self.parachute_diameter_entry = EntryWithBackgroundText(self.general_data_frame, background_text='metres')
        self.parachute_diameter_entry.grid(row=1, column=1)
        # self.stage0_force_label = Label(self.general_data_frame, text='force')
        # self.stage0_force_label.grid(row=2, column=0)
        # self.stage0_force_entry = EntryWithBackgroundText(self.general_data_frame, background_text='N')
        # self.stage0_force_entry.grid(row=2, column=1)
        # self.stage0_consumption_label = Label(self.general_data_frame, text='consumption')
        # self.stage0_consumption_label.grid(row=3, column=0)
        # self.stage0_consumption = EntryWithBackgroundText(self.general_data_frame, background_text='kg/sec')
        # self.stage0_consumption.grid(row=3, column=1)
        # self.stage0_time_label = Label(self.general_data_frame, text='time')
        # self.stage0_time_label.grid(row=4, column=0)
        # self.stage0_time = EntryWithBackgroundText(self.general_data_frame, background_text='sec')
        # self.stage0_time.grid(row=4, column=1)
        # self.stage0_initial_mass_label = Label(self.general_data_frame, text='initial_mass')
        # self.stage0_initial_mass_label.grid(row=5, column=0)
        # self.stage0_initial_mass = EntryWithBackgroundText(self.general_data_frame, background_text='kg')
        # self.stage0_initial_mass.grid(row=5, column=1)
        # self.stage0_final_mass_label = Label(self.general_data_frame, text='final_mass')
        # self.stage0_final_mass_label.grid(row=6, column=0)
        # self.stage0_final_mass = EntryWithBackgroundText(self.general_data_frame, background_text='kg')
        # self.stage0_final_mass.grid(row=6, column=1)

        self.stage1_frame = Frame(self.stages_frame, padx=25)
        self.stage1_frame.pack(side=LEFT, fill=X, expand=1)

        self.stage1_title = Label(self.stage1_frame, text='1st stage')
        self.stage1_title.grid(row=0, columnspan=2)
        self.stage1_diameter_label = Label(self.stage1_frame, text='diameter')
        self.stage1_diameter_label.grid(row=1, column=0)
        self.stage1_diameter_entry = EntryWithBackgroundText(self.stage1_frame, background_text='metres')
        self.stage1_diameter_entry.grid(row=1, column=1)
        self.stage1_force_label = Label(self.stage1_frame, text='force')
        self.stage1_force_label.grid(row=2, column=0)
        self.stage1_force_entry = EntryWithBackgroundText(self.stage1_frame, background_text='N')
        self.stage1_force_entry.grid(row=2, column=1)
        self.stage1_consumption_label = Label(self.stage1_frame, text='consumption')
        self.stage1_consumption_label.grid(row=3, column=0)
        self.stage1_consumption = EntryWithBackgroundText(self.stage1_frame, background_text='kg/sec')
        self.stage1_consumption.grid(row=3, column=1)
        self.stage1_time_label = Label(self.stage1_frame, text='time')
        self.stage1_time_label.grid(row=4, column=0)
        self.stage1_time = EntryWithBackgroundText(self.stage1_frame, background_text='sec')
        self.stage1_time.grid(row=4, column=1)
        self.stage1_initial_mass_label = Label(self.stage1_frame, text='initial_mass')
        self.stage1_initial_mass_label.grid(row=5, column=0)
        self.stage1_initial_mass = EntryWithBackgroundText(self.stage1_frame, background_text='kg')
        self.stage1_initial_mass.grid(row=5, column=1)
        self.stage1_final_mass_label = Label(self.stage1_frame, text='final_mass')
        self.stage1_final_mass_label.grid(row=6, column=0)
        self.stage1_final_mass = EntryWithBackgroundText(self.stage1_frame, background_text='kg')
        self.stage1_final_mass.grid(row=6, column=1)

        self.stage2_frame = Frame(self.stages_frame, padx=25)
        self.stage2_frame.pack(side=LEFT, fill=X, expand=1)

        self.stage2_title = Label(self.stage2_frame, text='2nd stage')
        self.stage2_title.grid(row=0, columnspan=2)
        self.stage2_diameter_label = Label(self.stage2_frame, text='diameter')
        self.stage2_diameter_label.grid(row=1, column=0)
        self.stage2_diameter_entry = EntryWithBackgroundText(self.stage2_frame, background_text='metres')
        self.stage2_diameter_entry.grid(row=1, column=1)
        self.stage2_force_label = Label(self.stage2_frame, text='force')
        self.stage2_force_label.grid(row=2, column=0)
        self.stage2_force_entry = EntryWithBackgroundText(self.stage2_frame, background_text='N')
        self.stage2_force_entry.grid(row=2, column=1)
        self.stage2_consumption_label = Label(self.stage2_frame, text='consumption')
        self.stage2_consumption_label.grid(row=3, column=0)
        self.stage2_consumption = EntryWithBackgroundText(self.stage2_frame, background_text='kg/sec')
        self.stage2_consumption.grid(row=3, column=1)
        self.stage2_time_label = Label(self.stage2_frame, text='time')
        self.stage2_time_label.grid(row=4, column=0)
        self.stage2_time = EntryWithBackgroundText(self.stage2_frame, background_text='sec')
        self.stage2_time.grid(row=4, column=1)
        self.stage2_initial_mass_label = Label(self.stage2_frame, text='initial_mass')
        self.stage2_initial_mass_label.grid(row=5, column=0)
        self.stage2_initial_mass = EntryWithBackgroundText(self.stage2_frame, background_text='kg')
        self.stage2_initial_mass.grid(row=5, column=1)
        self.stage2_final_mass_label = Label(self.stage2_frame, text='final_mass')
        self.stage2_final_mass_label.grid(row=6, column=0)
        self.stage2_final_mass = EntryWithBackgroundText(self.stage2_frame, background_text='kg')
        self.stage2_final_mass.grid(row=6, column=1)

        self.stage3_frame = Frame(self.stages_frame, padx=25)
        self.stage3_frame.pack(side=LEFT, fill=X, expand=1)

        self.stage3_title = Label(self.stage3_frame, text='3rd stage')
        self.stage3_title.grid(row=0, columnspan=2)
        self.stage3_diameter_label = Label(self.stage3_frame, text='diameter')
        self.stage3_diameter_label.grid(row=1, column=0)
        self.stage3_diameter_entry = EntryWithBackgroundText(self.stage3_frame, background_text='metres')
        self.stage3_diameter_entry.grid(row=1, column=1)
        self.stage3_force_label = Label(self.stage3_frame, text='force')
        self.stage3_force_label.grid(row=2, column=0)
        self.stage3_force_entry = EntryWithBackgroundText(self.stage3_frame, background_text='N')
        self.stage3_force_entry.grid(row=2, column=1)
        self.stage3_consumption_label = Label(self.stage3_frame, text='consumption')
        self.stage3_consumption_label.grid(row=3, column=0)
        self.stage3_consumption = EntryWithBackgroundText(self.stage3_frame, background_text='kg/sec')
        self.stage3_consumption.grid(row=3, column=1)
        self.stage3_time_label = Label(self.stage3_frame, text='time')
        self.stage3_time_label.grid(row=4, column=0)
        self.stage3_time = EntryWithBackgroundText(self.stage3_frame, background_text='sec')
        self.stage3_time.grid(row=4, column=1)
        self.stage3_initial_mass_label = Label(self.stage3_frame, text='initial_mass')
        self.stage3_initial_mass_label.grid(row=5, column=0)
        self.stage3_initial_mass = EntryWithBackgroundText(self.stage3_frame, background_text='kg')
        self.stage3_initial_mass.grid(row=5, column=1)
        self.stage3_final_mass_label = Label(self.stage3_frame, text='final_mass')
        self.stage3_final_mass_label.grid(row=6, column=0)
        self.stage3_final_mass = EntryWithBackgroundText(self.stage3_frame, background_text='kg')
        self.stage3_final_mass.grid(row=6, column=1)

        self.displayers_list = [self.displayer1, self.displayer2]

        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.size_x_prev = self.root.winfo_width()
        self.size_y_prev = self.root.winfo_height()
        self.root.bind('<Configure>', self.root_resize)

    def on_click(self):
        self.calculator.add_data_parachute()
        self.calculator.add_data_parachute()

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
