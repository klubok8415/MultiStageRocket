from tkinter import *
from tkinter.messagebox import *
from gui.CustomCanvas import CustomCanvas
from gui.EntryWithBackgroundText import EntryWithBackgroundText
from calculator import Calculator
from calculation_exceptions import OverSpeedError


class MainFrame(Frame):
    def __init__(self):
        self.root = Tk()
        super(MainFrame, self).__init__(self.root)
        self.calculator = Calculator()

        self.stages_frame = Frame(self.root)
        self.stages_frame.pack(fill=X, expand=1)
        self.displayer_frame = Frame(self.root, pady=20)
        self.displayer_frame.pack()

        self.velocity_by_time_displayer = CustomCanvas(self.displayer_frame,
                                                       title='V(t)',
                                                       y_axis_name='V\n(m/s)',
                                                       x_axis_name='t(s)')
        self.velocity_by_time_displayer.grid(row=0)
        self.height_by_time_displayer = CustomCanvas(self.displayer_frame,
                                                     title='H(t)',
                                                     y_axis_name='H\n(m)',
                                                     x_axis_name='t(s)')
        self.height_by_time_displayer.grid(row=0, column=1)

        self.results_frame = Frame(self.displayer_frame, padx=50)
        self.results_title = Label(self.results_frame, text='Results')
        self.results_title.grid(row=0, column=0)
        self.results_max_height_1 = Label(self.results_frame, text='maximum height')
        self.results_max_height_1.grid(row=1, column=0)
        self.results_max_height_2 = Label(self.results_frame, text='')
        self.results_max_height_2.grid(row=1, column=1)
        self.results_max_speed_1 = Label(self.results_frame, text='maximum speed')
        self.results_max_speed_1.grid(row=2, column=0)
        self.results_max_speed_2 = Label(self.results_frame, text='')
        self.results_max_speed_2.grid(row=2, column=1)
        self.results_time = Label(self.results_title, text='flight time')
        self.results_time.grid(row=3, column=0)
        self.results_time = Label(self.results_title, text='')
        self.results_time.grid(row=3, column=1)

        self.results_frame.grid(row=0, column=2)

        self.general_data_frame = Frame(self.stages_frame, padx=25)
        self.general_data_frame.pack(side=LEFT, fill=X, expand=1)

        self.check_parachute = BooleanVar(self.root, value=0)
        self.general_data_title = Label(self.general_data_frame, text='general data')
        self.general_data_title.grid(row=0, columnspan=2)
        self.parachute_checkbox = Checkbutton(self.general_data_frame,
                                              text='parachute',
                                              variable=self.check_parachute,
                                              command=self.on_checkbox_check_parachute)
        self.parachute_checkbox.grid(row=1, columnspan=2)
        self.parachute_diameter_label = Label(self.general_data_frame, text='parachute diameter')
        self.parachute_diameter_label.grid(row=2, column=0)
        self.parachute_diameter_entry = EntryWithBackgroundText(self.general_data_frame, background_text='metres')
        self.parachute_diameter_entry.grid(row=2, column=1)
        self.parachute_time_label = Label(self.general_data_frame, text='parachute time')
        self.parachute_time_label.grid(row=3, column=0)
        self.parachute_time_entry = EntryWithBackgroundText(self.general_data_frame, background_text='sec')
        self.parachute_time_entry.grid(row=3, column=1)

        self.stages_counter_label = Label(self.general_data_frame, text='number of stages')
        self.stages_counter_label.grid(row=4, columnspan=2)
        self.stages_counter = IntVar(self.root, value=1)
        self.one_stage_button = Radiobutton(self.general_data_frame,
                                            text='1',
                                            variable=self.stages_counter,
                                            value=1,
                                            command=self.change_stage_number)
        self.one_stage_button.grid(row=5, columnspan=2)
        self.two_stages_button = Radiobutton(self.general_data_frame,
                                             text='2',
                                             variable=self.stages_counter,
                                             value=2,
                                             command=self.change_stage_number)
        self.two_stages_button.grid(row=6, columnspan=2)
        self.three_stages_button = Radiobutton(self.general_data_frame,
                                               text='3',
                                               variable=self.stages_counter,
                                               value=3,
                                               command=self.change_stage_number)

        self.three_stages_button.grid(row=7, columnspan=2)

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
        self.stage1_consumption_entry = EntryWithBackgroundText(self.stage1_frame, background_text='kg/sec')
        self.stage1_consumption_entry.grid(row=3, column=1)
        self.stage1_time_label = Label(self.stage1_frame, text='time')
        self.stage1_time_label.grid(row=4, column=0)
        self.stage1_time_entry = EntryWithBackgroundText(self.stage1_frame, background_text='sec')
        self.stage1_time_entry.grid(row=4, column=1)
        self.stage1_initial_mass_label = Label(self.stage1_frame, text='initial mass')
        self.stage1_initial_mass_label.grid(row=5, column=0)
        self.stage1_initial_mass_entry = EntryWithBackgroundText(self.stage1_frame, background_text='kg')
        self.stage1_initial_mass_entry.grid(row=5, column=1)
        self.stage1_final_mass_label = Label(self.stage1_frame, text='final mass')
        self.stage1_final_mass_label.grid(row=6, column=0)
        self.stage1_final_mass_entry = EntryWithBackgroundText(self.stage1_frame, background_text='kg')
        self.stage1_final_mass_entry.grid(row=6, column=1)

        self.stage1_property = [
                                self.stage1_diameter_entry,
                                self.stage1_force_entry,
                                self.stage1_consumption_entry,
                                self.stage1_time_entry,
                                self.stage1_initial_mass_entry,
                                self.stage1_final_mass_entry
        ]

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
        self.stage2_consumption_entry = EntryWithBackgroundText(self.stage2_frame, background_text='kg/sec')
        self.stage2_consumption_entry.grid(row=3, column=1)
        self.stage2_time_label = Label(self.stage2_frame, text='time')
        self.stage2_time_label.grid(row=4, column=0)
        self.stage2_time_entry = EntryWithBackgroundText(self.stage2_frame, background_text='sec')
        self.stage2_time_entry.grid(row=4, column=1)
        self.stage2_initial_mass_label = Label(self.stage2_frame, text='initial mass')
        self.stage2_initial_mass_label.grid(row=5, column=0)
        self.stage2_initial_mass_entry = EntryWithBackgroundText(self.stage2_frame, background_text='kg')
        self.stage2_initial_mass_entry.grid(row=5, column=1)
        self.stage2_final_mass_label = Label(self.stage2_frame, text='final mass')
        self.stage2_final_mass_label.grid(row=6, column=0)
        self.stage2_final_mass_entry = EntryWithBackgroundText(self.stage2_frame, background_text='kg')
        self.stage2_final_mass_entry.grid(row=6, column=1)

        self.stage2_property = [
            self.stage2_diameter_entry,
            self.stage2_force_entry,
            self.stage2_consumption_entry,
            self.stage2_time_entry,
            self.stage2_initial_mass_entry,
            self.stage2_final_mass_entry
        ]

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
        self.stage3_consumption_entry = EntryWithBackgroundText(self.stage3_frame, background_text='kg/sec')
        self.stage3_consumption_entry.grid(row=3, column=1)
        self.stage3_time_label = Label(self.stage3_frame, text='time')
        self.stage3_time_label.grid(row=4, column=0)
        self.stage3_time_entry = EntryWithBackgroundText(self.stage3_frame, background_text='sec')
        self.stage3_time_entry.grid(row=4, column=1)
        self.stage3_initial_mass_label = Label(self.stage3_frame, text='initial mass')
        self.stage3_initial_mass_label.grid(row=5, column=0)
        self.stage3_initial_mass_entry = EntryWithBackgroundText(self.stage3_frame, background_text='kg')
        self.stage3_initial_mass_entry.grid(row=5, column=1)
        self.stage3_final_mass_label = Label(self.stage3_frame, text='final mass')
        self.stage3_final_mass_label.grid(row=6, column=0)
        self.stage3_final_mass_entry = EntryWithBackgroundText(self.stage3_frame, background_text='kg')
        self.stage3_final_mass_entry.grid(row=6, column=1)

        self.stage3_property = [
                                self.stage3_diameter_entry,
                                self.stage3_force_entry,
                                self.stage3_consumption_entry,
                                self.stage3_time_entry,
                                self.stage3_initial_mass_entry,
                                self.stage3_final_mass_entry
        ]

        self.displayers_list = [self.velocity_by_time_displayer, self.height_by_time_displayer]

        self.root.update()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())
        self.size_x_prev = self.root.winfo_width()
        self.size_y_prev = self.root.winfo_height()
        self.root.bind('<Configure>', self.root_resize)
        self.root.bind('<Return>', self.on_click_count)

        # values for testing
        self.stage1_diameter_entry.change_enter(1)
        self.stage1_force_entry.change_enter(1)
        self.stage1_consumption_entry.change_enter(1)
        self.stage1_time_entry.change_enter(1)
        self.stage1_initial_mass_entry.change_enter(1)
        self.stage1_final_mass_entry.change_enter(1)

        self.stage1_diameter_entry.insert(0, '0.05')
        self.stage1_force_entry.insert(0, '200')
        self.stage1_consumption_entry.insert(0, '1')
        self.stage1_time_entry.insert(0, '100')
        self.stage1_initial_mass_entry.insert(0, '2')
        self.stage1_final_mass_entry.insert(0, '1')

    def on_click_count(self, event):
        if self.stages_counter.get() == 1:
            self.calculator.add_data_stage(diameter=float(self.stage1_diameter_entry.get()),
                                           consumption=float(self.stage1_consumption_entry.get()),
                                           final_mass=float(self.stage1_final_mass_entry.get()),
                                           force=float(self.stage1_force_entry.get()),
                                           initial_mass=float(self.stage1_initial_mass_entry.get()),
                                           time=float(self.stage1_time_entry.get()))
        if self.stages_counter.get() == 2:
            self.calculator.add_data_stage(diameter=float(self.stage1_diameter_entry.get()),
                                           consumption=float(self.stage1_consumption_entry.get()),
                                           final_mass=float(self.stage1_final_mass_entry.get()),
                                           force=float(self.stage1_force_entry.get()),
                                           initial_mass=float(self.stage1_initial_mass_entry.get()),
                                           time=float(self.stage1_time_entry.get()))
            self.calculator.add_data_stage(diameter=float(self.stage2_diameter_entry.get()),
                                           consumption=float(self.stage2_consumption_entry.get()),
                                           final_mass=float(self.stage2_final_mass_entry.get()),
                                           force=float(self.stage2_force_entry.get()),
                                           initial_mass=float(self.stage2_initial_mass_entry.get()),
                                           time=float(self.stage2_time_entry.get()))
        if self.stages_counter.get() == 3:
            self.calculator.add_data_stage(diameter=float(self.stage1_diameter_entry.get()),
                                           consumption=float(self.stage1_consumption_entry.get()),
                                           final_mass=float(self.stage1_final_mass_entry.get()),
                                           force=float(self.stage1_force_entry.get()),
                                           initial_mass=float(self.stage1_initial_mass_entry.get()),
                                           time=float(self.stage1_time_entry.get()))
            self.calculator.add_data_stage(diameter=float(self.stage2_diameter_entry.get()),
                                           consumption=float(self.stage2_consumption_entry.get()),
                                           final_mass=float(self.stage2_final_mass_entry.get()),
                                           force=float(self.stage2_force_entry.get()),
                                           initial_mass=float(self.stage2_initial_mass_entry.get()),
                                           time=float(self.stage2_time_entry.get()))
            self.calculator.add_data_stage(diameter=float(self.stage3_diameter_entry.get()),
                                           consumption=float(self.stage3_consumption_entry.get()),
                                           final_mass=float(self.stage3_final_mass_entry.get()),
                                           force=float(self.stage3_force_entry.get()),
                                           initial_mass=float(self.stage3_initial_mass_entry.get()),
                                           time=float(self.stage3_time_entry.get()))
        self.calculator.add_data_parachute(pcs_stages=float(self.stages_counter.get()))
        if self.check_parachute.get():
            self.calculator.add_data_parachute(time=float(self.parachute_time_entry.get()),
                                               check_parachute=False,
                                               diameter=float(self.parachute_diameter_entry.get()),
                                               )

        self.calculator.stages_counter = self.stages_counter.get()
        try:
            self.calculator.count()
        except OverSpeedError:
            showerror(title='OverSpeedError', message='Rocket went supersonic \nfurther calculations are ineffectual')
            return
        self.velocity_by_time_displayer.add_function_data(self.calculator.velocity_list)
        self.height_by_time_displayer.add_function_data(self.calculator.height_list)
        self.results_max_height_2['text'] = str(round(float(max(Calculator.height_list.values())), 2)) + ' m'
        self.results_max_speed_2['text'] = str(round(float(max(Calculator.velocity_list.values())), 2)) + ' m/s'
        self.results_time['text'] = str(round(float(max(Calculator.velocity_list.keys())), 2)) + ' s'

    def change_stage_number(self):
        if self.stages_counter.get() == 1:
            for entry in self.stage1_property:
                entry.config(state=NORMAL)
                entry.change_exit(1)
            for entry in self.stage2_property:
                entry.delete(0, 'end')
                entry.config(state=DISABLED)
            for entry in self.stage3_property:
                entry.delete(0, 'end')
                entry.config(state=DISABLED)

        if self.stages_counter.get() == 2:
            for entry in self.stage1_property:
                entry.config(state=NORMAL)
                entry.change_exit(1)
            for entry in self.stage2_property:
                entry.config(state=NORMAL)
                entry.change_exit(1)
            for entry in self.stage3_property:
                entry.delete(0, 'end')
                entry.config(state=DISABLED)

        if self.stages_counter.get() == 3:
            for entry in self.stage1_property:
                entry.config(state=NORMAL)
                entry.change_exit(1)
            for entry in self.stage2_property:
                entry.config(state=NORMAL)
                entry.change_exit(1)
            for entry in self.stage3_property:
                entry.config(state=NORMAL)
                entry.change_exit(1)

    def on_checkbox_check_parachute(self):
        if self.check_parachute.get():
            self.parachute_diameter_entry.config(state=NORMAL)
            self.parachute_diameter_entry.change_exit(1)
            self.parachute_time_entry.config(state=NORMAL)
            self.parachute_time_entry.change_exit(1)
        else:
            self.parachute_diameter_entry.delete(0, 'end')
            self.parachute_time_entry.delete(0, 'end')
            self.parachute_diameter_entry.config(state=DISABLED)
            self.parachute_time_entry.config(state=DISABLED)

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
        self.height_by_time_displayer.update_graph()
        self.velocity_by_time_displayer.update_graph()
        self.change_stage_number()
        self.on_checkbox_check_parachute()
        self.root.mainloop()


if __name__ == '__main__':
    MainFrame().start()
