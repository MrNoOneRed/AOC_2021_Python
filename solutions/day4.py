#!/usr/bin/python

import sys

from collections import defaultdict

data = {}
winner_boards = []


def parse_input(input_path):
    data['numbers'] = []
    data['boards'] = defaultdict(list)

    with open(input_path) as file:
        board_number = 0
        columns = []
        rows = []

        for line in file:
            line = line.strip()

            if line.find(",") >= 0:
                data['numbers'] = list(map(int, line.split(',')))
            else:
                if line:
                    numbers = line.split()

                    for number in numbers:
                        columns.append({'number': int(number), 'found': False})

                    rows.append(columns.copy())
                    columns.clear()

                    if len(rows) == 5:
                        data['boards'][board_number] = rows.copy()
                        rows.clear()
                        board_number += 1

    return 0


def puzzle1():
    solution = 0

    clear_boards()

    for number in data['numbers']:
        mark_as_found(number)
        check_winner_board()

        if len(winner_boards) > 0:
            summary = sum_unchecked(winner_boards[0])
            solution = summary * number
            break

    return solution


def puzzle2():
    solution = 0

    clear_boards()

    for number in data['numbers']:
        mark_as_found(number)
        check_winner_board()

        if len(winner_boards) == len(data['boards']):
            summary = sum_unchecked(winner_boards[-1])
            solution = summary * number
            break

    return solution


def mark_as_found(number: int):
    for board in data['boards']:
        for row in data['boards'][board]:
            for item in row:
                if item['number'] == number:
                    item['found'] = True

    return True


def check_winner_board():
    for board in data['boards']:
        row = check_line(data['boards'][board])
        col = check_line(data['boards'][board], True)

        if row >= 0 or col >= 0:
            if board not in winner_boards:
                winner_boards.append(board)


def check_line(entry: list, reverse: bool = False):
    result = -1

    for x in range(0, 5):
        win = 0

        for y in range(0, 5):
            if (reverse and entry[y][x]['found']) or (not reverse and entry[x][y]['found']):
                win += 1

                if win == 5:
                    return x

    return result


def sum_unchecked(board: int):
    result = 0

    for row in data['boards'][board]:
        for item in row:
            if not item['found']:
                result += item['number']

    return result


def clear_boards():
    for board in data['boards']:
        for row in data['boards'][board]:
            for item in row:
                item['found'] = False
