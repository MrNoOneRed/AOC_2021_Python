#!/usr/bin/python

data = []

def parseInput(inputPath):
    with open(inputPath) as file:
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

#         test = data[i - 1] + " - " + depth
#         print(test + " -> increase " + str(solution) if data[i - 1] < depth else test + " -> descreased " + str(solution) )

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

#         test = str(left) + " - " + str(right)
#         print(test + " -> increase " + str(solution) if right > left else test + " -> descreased " + str(solution) )

    return solution