from calculator import Calculator

# One stage, 1 kg, consumption from 0.01 kg/s to 1kg/s

with open('tests_result.txt', 'w') as file:
    for consumption in range(10, 101, 10):
        force = 200 * consumption / 100
        calculator = Calculator()
        calculator.add_data_stage(
            stage_num=1,
            diameter=0.05,
            force=force,
            consumption=consumption/100,
            time=5,
            initial_mass=2,
            final_mass=1, )


        calculator.add_data_parachute(time=15,
                                      check_parachute=False,
                                      diameter=1,
                                      pcs_stages=1
                                      )
        calculator.count()
        file.write(str(consumption / 100) + ' : ' + str(max(calculator.height_list.values())))
        file.write('\n')
        print(str(consumption/100) + 'done!')
    print('done')
