#!/usr/bin/python

data = []

def parse_input(input_path):
    with open(input_path) as file:
        for line in file:
            bits = line.strip()
            data.append(bits)
    return 0

def puzzle1():
    solution = 0
    code = ''

    for charIndex in range(0, len(data[0])):
        one = 0
        zero = 0

        for lineIndex in range(0, len(data)):
            if int(data[lineIndex][charIndex]) == 0:
                zero += 1
            else:
                one += 1

        if zero > one:
            code += '0'
        else:
            code += '1'

    gamma = convert_binary_to_int(code)

    epsilon = convert_binary_to_int(code, True)

    solution = gamma * epsilon

    return solution

def puzzle2(pos: int = 0):
    solution = 0

    oxygen_data = data.copy()
    oxygen_binary = get_puzzle_to_bits(oxygen_data)
    co2_data = data.copy()
    co2_binary = get_puzzle_to_bits(co2_data, 0, True)

    oxygen = convert_binary_to_int(oxygen_binary)
    co2 = convert_binary_to_int(co2_binary)

    solution = oxygen * co2

    return solution

def get_puzzle_to_bits(input_data: [], pos: int = 0, reverse: bool = False):
    solution = 0

    if not reverse:
        compare = 0
    else:
        compare = 1

    if pos < len(input_data[0]):
        one = 0
        zero = 0
        indexes_to_remove = []

        for line_index in range(0, len(input_data)):
            if int(input_data[line_index][pos]) == 0:
                zero += 1
            else:
                one += 1

        for line_index in range(0, len(input_data)):
            if one == zero:
                if int(input_data[line_index][pos]) == reverse:
                    indexes_to_remove.append(line_index)
            else:
                if int(input_data[line_index][pos]) == reverse and one > zero:
                    indexes_to_remove.append(line_index)

                if int(input_data[line_index][pos]) != reverse and zero > one:
                    indexes_to_remove.append(line_index)

        indexes_to_remove = indexes_to_remove[::-1]

        for index in indexes_to_remove:
            input_data.pop(index)

        if len(input_data) > 1 and pos + 1 < len(input_data[0]):
            return get_puzzle_to_bits(input_data, pos + 1, reverse)
        else:
            solution = input_data[0]

    return solution

def convert_binary_to_int(code: str, reverse: bool = False):
    if reverse:
        reverse_code = ''
        for i in code:
            if i == '0':
                reverse_code += '1'
            else:
                reverse_code += '0'
        code = reverse_code

    return int(code, 2)
