#!/usr/bin/python

import sys

from collections import defaultdict

data = []


def parse_input(input_path):
    global data

    with open(input_path) as file:
        for line in file:
            line = line.strip()
            numbers = list(map(int, line.split(',')))
            data = [0] * 9
            for n in numbers:
                data[n] += 1


def puzzle1():
    solution = get_solution(80)

    return solution


def puzzle2():
    solution = get_solution(256)

    return solution


def get_solution(days: int):
    ocean = data.copy()

    for i in range(1, days + 1):
        first = ocean.pop(0)
        ocean.append(first)
        ocean[6] += first

    return sum(ocean)
