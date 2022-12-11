#!/usr/bin/python

import sys

from collections import defaultdict

data = {'left': [], 'right': []}
n1 = 2
n2 = 5
n3 = 5
n4 = 4
n5 = 5
n6 = 6
n7 = 3
n8 = 7
n9 = 6

layout = {'t': '', 'tl': '', 'tr': '', 'm': '', 'bl': '', 'br': '', 'b': ''}
numbers = {
    '1': ['tr', 'br'],
    '2': ['t', 'tr', 'm', 'bl', 'b'],
    '3': ['t', 'tr', 'm', 'br', 'b'],
    '4': ['tl', 'tr', 'm', 'br'],
    '5': ['t', 'tl', 'm', 'br', 'b'],
    '6': ['t', 'tl', 'm', 'bl', 'br', 'b'],
    '7': ['t', 'tr', 'br'],
    '8': ['t', 'tl', 'tr', 'm', 'bl', 'br', 'b'],
    '9': ['t', 'tl', 'tr', 'm', 'br', 'b']
}


def parse_input(input_path):
    with open(input_path) as file:
        for line in file:
            line = line.strip()
            parts = line.split(' | ')
            left = parts[0].split(' ')
            # left = sorted(left, key=len)
            # for l in range(0, len(left)):
            #     left[l] = ''.join(sorted(left[l]))

            data['left'].append(left)
            data['right'].append(parts[1].split(' '))


def puzzle1():
    solution = 0

    for i in data['right']:
        for n in list(map(len, i)):
            if n == n1 or n == n4 or n == n7 or n == n8:
                solution += 1

    return solution


def puzzle2():
    solution = 0

    for i in range(len(data['left'])):
        digit = layout.copy()
        digit = map_digit(digit, data['left'][i])

        solution += int(get_code(data['right'][i], digit))

    return solution


def get_code(codes: list, digit: dict):
    result = ''

    for code in codes:
        result += str(get_number(code, digit))

    return result


def get_number(code: str, digit: dict):
    found = defaultdict(list)

    for key, val in numbers.items():
        if len(code) == len(val):
            found[key] = val

    if len(found) == 1:
        return list(found)[0]
    else:
        for item in found:
            compare = ''
            for e in found[item]:
                compare += digit[e]
            if ''.join(sorted(compare)) == ''.join(sorted(code)):
                return item

    return 0


def map_digit(digit: dict, codes: list):
    w1 = [word for word in codes if len(word) == 2][0]
    w7 = [word for word in codes if len(word) == 3][0]
    w4 = [word for word in codes if len(word) == 4][0]
    w8 = [word for word in codes if len(word) == 7][0]
    w_lst = [word for word in codes if len(word) == 5]

    # compare 1 and 7. Difference is digit top
    digit['t'] = string_diff(w1, w7)

    # compare 1 and 4 than 7 and 3 than get same result for each comparison. Same result is for digit middle
    diff1 = string_diff(w1, w4)
    diff2 = ''
    for w in w_lst:
        if has_string(w7, w):
            diff2 = string_diff(w7, w)
            break

    digit['m'] = get_first_same(diff1, diff2)

    # remove middle from 7 and 3 comparison results to get digit bottom
    digit['b'] = diff2.replace(digit['m'], '')

    # remove middle from 1 and 4 comparison results to get digit top left
    digit['tl'] = diff1.replace(digit['m'], '')

    # try to find 2 and compare it with digital top, top left, middle and bottom to get digit bottom right
    search = digit['t'] + digit['tl'] + digit['m'] + digit['b']
    for w in w_lst:
        if has_string(search, w):
            digit['br'] = string_diff(search, w)
            break

    # compare digit bottom right with number 1 to get digit top left
    search = digit['br']
    digit['tr'] = string_diff(search, w1)

    # compare all digit to 8 to get last digit bottom right
    search = digit['t'] + digit['tl'] + digit['tr'] + digit['m'] + digit['br'] + digit['b']
    digit['bl'] = string_diff(search, w8)

    return digit


def has_string(find: str, stack: str):
    found = 0
    target = len(find)

    lst_f = [find[i] for i in range(len(find))]
    lst_s = [stack[i] for i in range(len(stack))]

    for search in lst_f:
        for char in lst_s:
            if search == char:
                found += 1
                break
        if found == target:
            return True
    return False


def get_first_same(left: str, right: str):
    lst_l = [left[i] for i in range(len(left))]
    lst_r = [right[i] for i in range(len(right))]

    for search in lst_l:
        for char in lst_r:
            if search == char:
                return search

    return ''


def string_diff(left: str, right: str):
    lst_l = [left[i] for i in range(len(left))]
    lst_r = [right[i] for i in range(len(right))]

    for i in lst_l:
        lst_r.remove(i)

    return ''.join(lst_r)


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
