from math import *
from calculator_exceptions import OverSpeedError


class Calculator:
    parachute_data = {}
    stages_data = []
    velocity_list = {}
    height_list = {}

    def __init__(self):
        self.current_speed = 0
        self.current_height = 0
        self.all_time = 0
        self.current_stage = 1
        self.cx_list = [0.775084047,
                        0.607780256,
                        0.491020986,
                        0.592614012,
                        0.577720113,
                        0.566142305,
                        0.556707884,
                        0.548769063,
                        0.541931052,
                        0.535935909,
                        0.530606125,
                        0.525859244,
                        0.521665488,
                        0.519660613,
                        0.517897913,
                        0.517915039,
                        0.517930387,
                        0.517944644,
                        0.517958491,
                        0.517972597,
                        0.51798762,
                        0.518004211,
                        0.518023003,
                        0.51804462,
                        0.51806967,
                        0.518098746,
                        0.518383377,
                        0.518672945,
                        0.518967973,
                        0.519268967,
                        0.519576411,
                        0.519890769,
                        0.520212482,
                        0.52054197,
                        0.520879627,
                        0.521225824,
                        0.521580905,
                        0.521945189,
                        0.522318967,
                        0.522702506,
                        0.523096042,
                        0.523499783,
                        0.523913911,
                        0.524338577,
                        0.524773905,
                        0.525219988,
                        0.525676893,
                        0.526144658,
                        0.526623292,
                        0.527112776,
                        0.527613065,
                        0.528124086,
                        0.528645742,
                        0.52917791,
                        0.529720441,
                        0.530273165,
                        0.530835888,
                        0.531408396,
                        0.531990454,
                        0.53258181,
                        0.533182191,
                        0.533175739,
                        0.533179075,
                        0.533191909,
                        0.533213936,
                        0.533244842,
                        0.533284302,
                        0.533331984,
                        0.533387547,
                        0.533450644,
                        0.533520924,
                        0.533598034,
                        0.533681618,
                        0.533771319,
                        0.533866781,
                        0.53396765,
                        0.534073574,
                        0.534184204,
                        0.534299198,
                        0.534418218,
                        0.534540932,
                        0.534654753,
                        0.534747181,
                        0.534818063,
                        0.534867292,
                        0.53489481,
                        0.535330268,
                        0.536607882,
                        0.538727684,
                        0.541689923,
                        0.545452526,
                        0.550212732,
                        0.555894265,
                        0.562513198,
                        0.570095113,
                        0.578678613,
                        0.58832099,
                        0.599107154,
                        0.611163687,
                        0.624681088,
                        0.640621228]
        self.cx_dictionary = {}
        for i in range(101):
            self.cx_dictionary[i * 3.4] = self.cx_list[i]

    def count(self, density=1.29, b=5.6 * 10 ** -5, gravity=9.81, delta_t=0.01, parachute_resistance=1.1):
        diameter = self.stages_data[self.current_stage - 1]['diameter']
        force = self.stages_data[self.current_stage - 1]['force']
        consumption = self.stages_data[self.current_stage - 1]['consumption']
        time = self.stages_data[self.current_stage - 1]['time']
        initial_mass = self.stages_data[self.current_stage - 1]['initial_mass']
        final_mass = self.stages_data[self.current_stage - 1]['final_mass']
        area = pi * (0.5 * diameter) ** 2

        current_mass = initial_mass

        current_time = 0
        parachute_forse = 0

        while self.current_height >= 0 or (current_time <= time and self.parachute_data['pcs_stages'] == int(
                        self.current_stage)):

            if current_mass > final_mass:
                current_mass = initial_mass - consumption * current_time
            else:
                current_mass = final_mass

            current_density = density * 10 ** (-b * self.current_height)

            speed_for_cx = self.current_speed
            if speed_for_cx > 0:
                while round(speed_for_cx, 1) not in self.cx_dictionary.keys():
                    speed_for_cx -= 0.1
                    if speed_for_cx < 0:
                        break
                current_resistance = self.cx_dictionary[round(speed_for_cx, 1)]
            else:
                while round(speed_for_cx, 1) not in self.cx_dictionary.keys():
                    speed_for_cx += 0.1
                current_resistance = self.cx_dictionary[round(speed_for_cx, 1)]

            self.velocity_list[round(current_time + self.all_time, 3)] = self.current_speed
            self.height_list[round(current_time + self.all_time, 3)] = self.current_height

            if current_time >= (initial_mass - final_mass) / consumption:
                force = 0

            if self.parachute_data['check_parachute']:
                if self.parachute_data['time'] < current_time and self.parachute_data['pcs_stages'] == self.current_stage:
                    parachute_forse = parachute_resistance * pi * (self.parachute_data['diameter']/2) ** 2 * \
                                      self.current_speed ** 2 * current_density / 2
            self.current_speed = self.current_speed + (force + parachute_forse - current_mass * gravity - current_resistance *
                                             area * self.current_speed ** 2 * current_density / 2) \
                            * delta_t / current_mass
            if 1 > 340:
                raise OverSpeedError('Speed limit reached')

            self.current_height = self.current_height + self.current_speed * delta_t

            current_time += delta_t

            if current_time >= time and self.current_stage != self.parachute_data['pcs_stages']:
                break

            if self.current_height < 0:
                # print('Falcon has landed with landing velocity {} m/s'.format(
                #     round(abs(self.velocity_list[round(t - delta_t, 2)]), 2)))
                return

        self.all_time += current_time
        self.current_stage += 1
        if self.current_stage <= self.parachute_data['pcs_stages']:
            self.count()

    def add_data_stage(self, **kwargs):
        if kwargs['stage_num'] == 1:
            self.stages_data.clear()
        self.stages_data.append(kwargs)

    def add_data_parachute(self, **kwargs):

        self.parachute_data = kwargs


if __name__ == '__main__':
    calculator = Calculator()
    calculator.add_data_stage(
        diameter=0.05,
        force=200,
        consumption=1,
        time=5,
        initial_mass=3,
        final_mass=2,

    )
    calculator.add_data_stage(
        diameter=0.05,
        force=200,
        consumption=1,
        time=5,
        initial_mass=2,
        final_mass=1,)
    calculator.add_data_parachute(time=15,
                                  check_parachute=False,
                                  diameter=1,
                                  pcs_stages=2
                                  )

    calculator.count()
    for key, value in calculator.height_list.items():
        if round(key, 1) == key:
            print('{0}sec : {1}m'.format(key, value))
    print(max(calculator.height_list.values()))
    print(max(calculator.velocity_list.values()))
