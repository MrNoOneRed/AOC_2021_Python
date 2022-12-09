#!/usr/bin/python

import sys
import configparser
import os
import importlib
import inquirer

config_path = ".\config.txt"

# check config path
if not os.path.exists(config_path):
    raise Exception("config.txt not found")

# check argument
if len(sys.argv) < 2:
    raise Exception("You need to provide day number as first argument. For example 'python day.py 12'")

if not sys.argv[1].isnumeric():
    raise Exception("Argument need to be number")

# load config
configparser = configparser.RawConfigParser()
configparser.read(config_path)
input_path = configparser.get('app-config', 'input_path')

# check config
if not configparser.has_section('app-config'):
    raise Exception("There is no section app-config in config.txt")
if not configparser.has_option('app-config', 'input_path'):
    raise Exception("There is no option input_path defined")

# check puzzle path
if not os.path.exists(input_path):
    raise Exception("Path to puzzle inputs not exists")

# import solution
day = sys.argv[1]
solution_file = ".\solutions\day" + day + ".py"
solution_module = 'solutions.day' + day
input_path += "\\" + day

# check solution
if not os.path.isfile(solution_file):
    raise Exception("Solution not exists")

# get all puzzle inputs for selected day
puzzle_files = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]

# check inputs for puzzles
if len(puzzle_files) == 0:
    raise Exception("You dont have any puzzle inputs")

# ask user which puzzle input to use
inputs_choose = [
    inquirer.List('input', message="What input you want to check ?", choices=puzzle_files)
]
input_selected = inquirer.prompt(inputs_choose)["input"]

# load module
module = importlib.import_module(solution_module)

# parse input data to use in puzzles
module.parse_input(os.path.join(input_path, input_selected))

# get solution
print("Solution for puzzle1:", module.puzzle1())
print("Solution for puzzle2:", module.puzzle2())

sys.exit()
