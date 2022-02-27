import sys
sys.path.append('../')
from helper_functions import *

def part1(lineList):
    templist = lineList
    for i in lineList:
        for j in templist:
            if (i + j) == 2020:
                return i * j


def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('../inputs/input_01.txt')
    print(part1(lineList))
    print(part2(lineList))