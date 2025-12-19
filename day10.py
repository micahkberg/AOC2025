from Cython.Compiler.ExprNodes import compile_time_binary_operators

from day01 import read_input
import itertools
import collections

def button_press_outcome(buttons_pressed, number_of_lights):
    outcome = ['.']*number_of_lights
    for button in buttons_pressed:
        for connection in button:
            if outcome[connection] == '.':
                outcome[connection] = '#'
            else:
                outcome[connection] = '.'
    return "".join(outcome)

def test_joltage_outcome(pressed, joltages):
    outcome = [0]*len(joltages)
    for k, v in pressed.items():
        for connection in k:
            outcome[connection] += v
            if outcome[connection] > joltages[connection]:
                return False
    return outcome==joltages

def solve_joltage_requirement(buttons, joltage_requirements):
    press_count_found = False
    press_count = max(joltage_requirements)-1
    combinations_tested = 0
    while not press_count_found:
        press_count += 1
        print(press_count)
        press_combinations = itertools.combinations_with_replacement(buttons, press_count)
        for sequence in press_combinations:
            combinations_tested += 1
            if combinations_tested%100000 == 0:
                print(f"combinations_tested: {combinations_tested}")
            press_dict = collections.Counter(sequence)
            joltage_match = test_joltage_outcome(press_dict, joltage_requirements)
            if joltage_match:
                press_count_found = True
                break
    return press_count

def main():
    lines = read_input('10')[:-1]
    total_presses_lights = 0
    total_presses_joltages = 0
    for line in lines:
        print(line)
        light_diagram = line.split(" ")[0].strip("[]")
        buttons = line.split(" ")[1:-1]
        buttons = [tuple(map(int, b.strip("()").split(","))) for b in buttons]
        joltage_requirements = list(map(int, line.split(" ")[-1].strip("{}").split(",")))
        number_of_presses_lights = 0
        solution_found = False
        while not solution_found:
            number_of_presses_lights += 1
            press_sequences = itertools.combinations_with_replacement(buttons, number_of_presses_lights)
            for sequence in press_sequences:
                #print(sequence)
                outcome = button_press_outcome(sequence, len(light_diagram))
                if outcome == light_diagram:
                    solution_found = True
                    break
        print(f"Total number of presses to turn on {number_of_presses_lights}")
        total_presses_lights += number_of_presses_lights
        total_presses_joltages += solve_joltage_requirement(buttons, joltage_requirements)
        print(f'Total joltage button presses so far... {total_presses_joltages}')
    print("finally")
    print(total_presses_lights)
    print(total_presses_joltages)



if __name__ == '__main__':
    main()
