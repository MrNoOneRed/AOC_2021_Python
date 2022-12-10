#!/usr/bin/python

import sys

from collections import defaultdict

data = []


def parse_input(input_path):
    global data

    with open(input_path) as file:
        for line in file:
            line = line.strip()
            data = list(map(int, line.split(',')))


def puzzle1():
    solution = get_solution()

    return solution


def puzzle2():
    solution = get_solution(True)

    return solution


def get_solution(step: bool = False):
    crabs = data.copy()

    crabs.sort(reverse=True)

    consumption = []

    for i in range(0, crabs[0] + 1):
        fuel = 0

        for n in crabs:
            if step:
                for c in range(0, abs(n - i)):
                    fuel += (c + 1)
            else:
                fuel += abs(n - i)

        consumption.append(fuel)

    consumption.sort()

    return consumption[0]
