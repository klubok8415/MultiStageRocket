from math import *

class Calculator:
    def __init__(self):
        self.stages_data = []
        self.speed_list = {}
        self.height_list = {}
        self.stage_counter = 1
        self.current_stage = 0
        cx_list = [0, 775084047,
                   0, 607780256,
                   0, 491020986,
                   0, 592614012,
                   0, 577720113,
                   0, 566142305,
                   0, 556707884,
                   0, 548769063,
                   0, 541931052,
                   0, 535935909,
                   0, 530606125,
                   0, 525859244,
                   0, 521665488,
                   0, 519660613,
                   0, 517897913,
                   0, 517915039,
                   0, 517930387,
                   0, 517944644,
                   0, 517958491,
                   0, 517972597,
                   0, 51798762,
                   0, 518004211,
                   0, 518023003,
                   0, 51804462,
                   0, 51806967,
                   0, 518098746,
                   0, 518383377,
                   0, 518672945,
                   0, 518967973,
                   0, 519268967,
                   0, 519576411,
                   0, 519890769,
                   0, 520212482,
                   0, 52054197,
                   0, 520879627,
                   0, 521225824,
                   0, 521580905,
                   0, 521945189,
                   0, 522318967,
                   0, 522702506,
                   0, 523096042,
                   0, 523499783,
                   0, 523913911,
                   0, 524338577,
                   0, 524773905,
                   0, 525219988,
                   0, 525676893,
                   0, 526144658,
                   0, 526623292,
                   0, 527112776,
                   0, 527613065,
                   0, 528124086,
                   0, 528645742,
                   0, 52917791,
                   0, 529720441,
                   0, 530273165,
                   0, 530835888,
                   0, 531408396,
                   0, 531990454,
                   0, 53258181,
                   0, 533182191,
                   0, 533175739,
                   0, 533179075,
                   0, 533191909,
                   0, 533213936,
                   0, 533244842,
                   0, 533284302,
                   0, 533331984,
                   0, 533387547,
                   0, 533450644,
                   0, 533520924,
                   0, 533598034,
                   0, 533681618,
                   0, 533771319,
                   0, 533866781,
                   0, 53396765,
                   0, 534073574,
                   0, 534184204,
                   0, 534299198,
                   0, 534418218,
                   0, 534540932,
                   0, 534654753,
                   0, 534747181,
                   0, 534818063,
                   0, 534867292,
                   0, 53489481,
                   0, 535330268,
                   0, 536607882,
                   0, 538727684,
                   0, 541689923,
                   0, 545452526,
                   0, 550212732,
                   0, 555894265,
                   0, 562513198,
                   0, 570095113,
                   0, 578678613,
                   0, 58832099,
                   0, 599107154,
                   0, 611163687,
                   0, 624681088,
                   0, 640621228]
        self.cx_dictionary = {}
        for i in range(101):
            self.cx_dictionary[i*3.4] =cx_list[i]

    def count(self, density=1.29, b=5.6 * 10 ** -5, gravity=9.81, delta_t=0.01, resistance=0):
        diameter = self.stages_data[self.current_stage]['diameter']
        force = self.stages_data[self.current_stage]['force']
        consumption = self.stages_data[self.current_stage]['consumption']
        time = self.stages_data[self.current_stage]['time']
        initial_mass = self.stages_data[self.current_stage]['initial_mass']
        final_mass = self.stages_data[self.current_stage]['final_mass']
        height = 0
        speed = 0
        t = 0
        area = pi * (0.5 * diameter) ** 2
        current_height = height
        current_mass = initial_mass
        current_speed = speed
        current_time = 0
        while t <= time:
            if current_mass > final_mass:
                current_mass = initial_mass - consumption * t
            else:
                current_mass = final_mass

            current_density = density * 10 ** (-b * current_height)

            self.speed_list[current_time+t] = current_speed
            self.height_list[current_time+t] = current_height
            if t >= (initial_mass - final_mass)/consumption:
                force = 0
            current_speed = current_speed + (force-current_mass * gravity - resistance * area * current_speed ** 2 * current_density / 2) * delta_t / current_mass
            current_height = current_height + current_speed * delta_t
            t += delta_t
            if current_height < 0:
                print('Falcon has landed')
                return

        current_time += time
        self.stage_counter -= 1
        self.current_stage += 1
        if self.stage_counter > 0:
            self.count()

    def add_data(self, **kwargs):
        self.stages_data.append(kwargs)

if __name__ == '__main__':
    calculator = Calculator()
    calculator.add_data(diameter=0.05, force=500, consumption=1, time=100, initial_mass=2, final_mass=1, resistance=0.333)
    calculator.count()
    print(calculator.height_list)
    print(max(calculator.height_list.values()))
    print(max(calculator.speed_list.values()))
