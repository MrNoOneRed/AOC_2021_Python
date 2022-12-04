#!/usr/bin/python

import sys
import configparser
import os
import importlib
import inquirer

configPath = ".\config.txt"

# check config path
if not os.path.exists(configPath):
    raise Exception("config.txt not found")

# check argument
if len(sys.argv) < 2:
    raise Exception("You need to provide day number as first argument. For example 'python day.py 12'")

if not sys.argv[1].isnumeric():
    raise Exception("Argument need to be number")

# load config
configparser = configparser.RawConfigParser()
configparser.read(configPath)
inputPath = configparser.get('app-config', 'inputPath')

# check config
if not configparser.has_section('app-config'):
    raise Exception("There is no section app-config in config.txt")
if not configparser.has_option('app-config', 'inputPath'):
    raise Exception("There is no option inputPath defined")

# check puzzle path
if not os.path.exists(inputPath):
    raise Exception("Path to puzzle inputs not exists")

# import solution
day = sys.argv[1]
solutionFile = ".\solutions\day" + day + ".py"
solutionModule = 'solutions.day' + day
inputPath += "\\" + day

# check solution
if not os.path.isfile(solutionFile):
    raise Exception("Solution not exists")

# get all puzzle inputs for selected day
puzzleFiles = [f for f in os.listdir(inputPath) if os.path.isfile(os.path.join(inputPath, f))]

# check inputs for puzzles
if len(puzzleFiles) == 0:
    raise Exception("You dont have any puzzle inputs")

# ask user which puzzle input to use
inputsChoose = [
    inquirer.List('input', message="What input you want to check ?", choices=puzzleFiles)
]
inputSelected = inquirer.prompt(inputsChoose)["input"]

# load module
module = importlib.import_module(solutionModule)

# parse input data to use in puzzles
module.parseInput(os.path.join(inputPath, inputSelected))

# get solution
print("Solution for puzzle1:", module.puzzle1())
print("Solution for puzzle2:", module.puzzle2())

sys.exit()
