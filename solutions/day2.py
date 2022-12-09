#!/usr/bin/python

data = []

def parse_input(input_path):
    with open(input_path) as file:
        for line in file:
            commands = line.strip().split()
            data.append({
                'command': commands[0],
                'value': commands[1]
            })
    return 0

def puzzle1():
    solution = 0
    position = 0
    depth = 0

    for commands in data:
        if commands['command'] == 'forward':
            position += int(commands['value'])
        if commands['command'] == 'down':
            depth += int(commands['value'])
        if commands['command'] == 'up':
            depth -= int(commands['value'])

#         print(commands['command'] + ' - ' + commands['value'])

    solution = position * depth

    return solution

def puzzle2():
    solution = 0
    position = 0
    depth = 0
    aim = 0

    for commands in data:
        if commands['command'] == 'forward':
            position += int(commands['value'])
            depth += aim * int(commands['value'])
        if commands['command'] == 'down':
            aim += int(commands['value'])
        if commands['command'] == 'up':
            aim -= int(commands['value'])

    solution = position * depth

    return solution