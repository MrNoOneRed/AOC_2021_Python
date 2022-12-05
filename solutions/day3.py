#!/usr/bin/python

data = []

def parseInput(inputPath):
    with open(inputPath) as file:
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

    gamma = convertBinaryToInt(code)

    epsilon = convertBinaryToInt(code, True)

    return gamma * epsilon

def puzzle2(pos: int = 0):
    oxygenData = data.copy()
    oxygenBinary = getPuzzle2Bits(oxygenData)
    co2Data = data.copy()
    co2Binary = getPuzzle2Bits(co2Data, 0, True)

    oxygen = convertBinaryToInt(oxygenBinary)
    co2 = convertBinaryToInt(co2Binary)

    return oxygen * co2

def getPuzzle2Bits(inputData: [], pos: int = 0, reverse: bool = False):
    solution = 0

    if not reverse:
        compare = 0
    else:
        compare = 1

    if pos < len(inputData[0]):
        one = 0
        zero = 0
        indexesToRemove = []

        for lineIndex in range(0, len(inputData)):
            if int(inputData[lineIndex][pos]) == 0:
                zero += 1
            else:
                one += 1

        for lineIndex in range(0, len(inputData)):
            if one == zero:
                if int(inputData[lineIndex][pos]) == reverse:
                    indexesToRemove.append(lineIndex)
            else:
                if int(inputData[lineIndex][pos]) == reverse and one > zero:
                    indexesToRemove.append(lineIndex)

                if int(inputData[lineIndex][pos]) != reverse and zero > one:
                    indexesToRemove.append(lineIndex)

        indexesToRemove = indexesToRemove[::-1]

        for index in indexesToRemove:
            inputData.pop(index)

        if len(inputData) > 1 and pos + 1 < len(inputData[0]):
            return getPuzzle2Bits(inputData, pos + 1, reverse)
        else:
            solution = inputData[0]

    return solution

def convertBinaryToInt(code: str, reverse: bool = False):
    if reverse:
        reverseCode = ''
        for i in code:
            if i == '0':
                reverseCode += '1'
            else:
                reverseCode += '0'
        code = reverseCode

    return int(code, 2)
