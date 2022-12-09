#!/usr/bin/python

import sys

from collections import defaultdict

data = []
board = []


def parse_input(input_path):
    with open(input_path) as file:
        for line in file:
            line = line.strip()
            cords = line.split(' -> ')
            start = cords[0].split(',')
            end = cords[1].split(',')

            data.append({'x1': int(start[0]), 'y1': int(start[1]), 'x2': int(end[0]), 'y2': int(end[1])})


def puzzle1():
    create_board()

    set_cords()

    solution = count_overlaps(2)

    return solution


def puzzle2():
    create_board()

    set_cords(True)

    #draw()

    solution = count_overlaps(2)

    return solution


def create_board():
    board.clear()

    max_x = 0
    max_y = 0

    for cords in data:
        if cords['x1'] > max_x:
            max_x = cords['x1']
        if cords['x2'] > max_x:
            max_x = cords['x2']
        if cords['y1'] > max_y:
            max_y = cords['y1']
        if cords['y2'] > max_y:
            max_y = cords['y2']

    for y in range(0, max_y + 1):
        board.append([0] * (max_x + 1))


def set_cords(diagonal: bool = False):
    for cords in data:
        if cords['x1'] == cords['x2']:
            if cords['y1'] <= cords['y2']:
                for i in range(cords['y1'], cords['y2'] + 1):
                    board[i][cords['x1']] += 1
            if cords['y1'] >= cords['y2']:
                for i in range(cords['y2'], cords['y1'] + 1):
                    board[i][cords['x1']] += 1
        if cords['y1'] == cords['y2']:
            if cords['x1'] <= cords['x2']:
                for i in range(cords['x1'], cords['x2'] + 1):
                    board[cords['y1']][i] += 1
            if cords['x1'] >= cords['x2']:
                for i in range(cords['x2'], cords['x1'] + 1):
                    board[cords['y1']][i] += 1
        if diagonal and cords['x1'] != cords['x2'] and cords['y1'] != cords['y2']:
            for i in range(0, abs(cords['x1'] - cords['x2']) + 1):
                movex = 0
                movey = 0
                if cords['x1'] > cords['x2']:
                    movex = -i
                if cords['x1'] < cords['x2']:
                    movex = i
                if cords['y1'] > cords['y2']:
                    movey = -i
                if cords['y1'] < cords['y2']:
                    movey = i

                board[cords['y1'] + movey][cords['x1'] + movex] += 1


def count_overlaps(number: int):
    result = 0

    for y in range(0, len(board)):
        for x in range(0, len(board[y])):
            if board[y][x] >= number:
                result += 1

    return result


def draw():
    for y in range(0, len(board)):
        print(''.join(map(str, board[y])))

