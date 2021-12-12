import sys
sys.path.append('../')
from helper_functions import *

def part1(lineList):
    pos = 0
    depth = 0
    for i in lineList:
        command = i.split(' ')
        if command[0] == 'forward':
            pos += int(command[1])
        if command[0] == 'down':
            depth += int(command[1])
        if command[0] == 'up':
            depth -= int(command[1])
    return pos * depth

def part2(lineList):
    pos = 0
    depth = 0
    aim = 0
    for i in lineList:
        command = i.split(' ')
        if command[0] == 'down':
            aim += int(command[1])
        if command[0] == 'up':
            aim -= int(command[1])
        if command[0] == 'forward':
            pos += int(command[1])
            depth += aim * int(command[1])
    return pos * depth

if __name__ == '__main__':
    lineList = readInput('../inputs/input_02.txt')
    print(part1(lineList))
    print(part2(lineList))