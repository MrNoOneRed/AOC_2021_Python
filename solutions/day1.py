#!/usr/bin/python

data = []

def parse_input(input_path):
    with open(input_path) as file:
        for line in file:
            data.append(line.strip())
    return 0

def puzzle1():
    solution = 0

    for i, depth in enumerate(data):
        if i == 0:
            continue
        if int(data[i - 1]) < int(depth):
            solution += 1

    return solution

def puzzle2():
    solution = 0

    for i, depth in enumerate(data):
        if i + 3 >= len(data):
            break

        left = int(data[i]) + int(data[i + 1]) + int(data[i + 2])
        right = int(data[i + 1]) + int(data[i + 2]) + int(data[i + 3])

        if right > left:
            solution += 1

    return solution