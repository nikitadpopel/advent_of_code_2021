import sys
sys.path.append('../')
from helper_functions import *

# this one, I was able to do with same function

def function(lineList, days):
    listOfish = [0,0,0,0,0,0,0,0,0]
    fishies = lineList[0].split(',')
    for i in fishies:
        listOfish[int(i)] += 1
    for i in range(0, days):
        listOfish = oneDay(listOfish)
    return sum(listOfish)

def oneDay(listOfish):
    newfishies = listOfish[0]
    listOfish.pop(0)
    listOfish[6] += newfishies
    listOfish.append(newfishies)
    return listOfish

def part1(lineList, days):
    return function(lineList, days)

def part2(lineList, days):
    return function(lineList, days)

if __name__ == '__main__':
    lineList = readInput('../inputs/input_06.txt')
    print(part1(lineList, 80))
    print(part2(lineList, 256))