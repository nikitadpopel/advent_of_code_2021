import sys
sys.path.append('../')
from helper_functions import *

def part1(lineList):
    previous = int(lineList[0])
    increaseNum = 0
    for i in lineList[1:]:
        if int(i) > previous:
            increaseNum += 1
        previous = int(i)
    return increaseNum

def part2(lineList):
    first = int(lineList[0])
    second = int(lineList[1])
    third = int(lineList[2])
    oldSum = first + second + third
    increaseNum = 0
    for i in lineList[3:]:
        first = second
        second = third
        third = int(i)
        newSum = first + second + third 
        if newSum > oldSum:
            increaseNum += 1
        oldSum = newSum
    return increaseNum

if __name__ == '__main__':
    lineList = readInput('../inputs/input_01.txt')
    print(part1(lineList))
    print(part2(lineList))