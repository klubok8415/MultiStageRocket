from math import *


class Calculator:
    def __init__(self, stages):
        self.stages_data = []
        self.speed_list = {}
        self.height_list = {}
        self.stage_counter = stages
        self.current_stage = 0

    def count(self, density=1.29, b=5.6 * 10 ** -5, gravity=9.81, delta_t=0.01):
        diameter = self.stages_data[self.current_stage]['diameter']
        force = self.stages_data[self.current_stage]['force']
        consumption = self.stages_data[self.current_stage]['consumption']
        time = self.stages_data[self.current_stage]['time']
        initial_mass = self.stages_data[self.current_stage]['initial_mass']
        final_mass = self.stages_data[self.current_stage]['final_mass']
        resistance = self.stages_data[self.current_stage]['resistance']

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
            print(current_density)

            self.speed_list[current_time + t] = current_speed
            self.height_list[current_time + t] = current_height

            if t >= (initial_mass - final_mass) / consumption:
                force = 0

            current_speed = current_speed
            + (force - current_mass * gravity -
                resistance * area * current_speed ** 2 * current_density / 2) * \
                delta_t / current_mass

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
    calculator = Calculator(stages=1)
    calculator.add_data(
        diameter=0.05,
        force=500,
        consumption=1,
        time=100,
        initial_mass=2,
        final_mass=1,
        resistance=0.333
    )

    calculator.count()
    print(calculator.height_list)
    print(max(calculator.height_list.values()))
    print(max(calculator.speed_list.values()))
