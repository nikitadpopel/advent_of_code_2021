import sys
sys.path.append('../')
from helper_functions import *

def convertCave(lineList):
    cave = []
    for i in lineList:
        temp = []
        for j in i:
            temp.append(int(j))
        cave.append(temp)
    return cave

def printCave(cave):
    for i in cave:
        print(i)

def getLowPoints(cave):
    lowpoints = []
    lowpointsum = 0
    for y, i in enumerate(cave):
        for x, j in enumerate(i):
            isLow = True
            if x != 0:
                if cave[y][x - 1] < j:
                    isLow = False
            if y != 0:
                if cave[y - 1][x] < j:
                    isLow = False
            if x != len(i) - 1:
                if cave[y][x + 1] < j: 
                    isLow = False
            if y != len(cave) - 1:
                if cave[y + 1][x] < j:
                    isLow = False
            if j == 9:
                isLow = False
            if isLow:
                tempcoord = [y,x]
                lowpoints.append(tempcoord)
                lowpointsum += j + 1
    return lowpointsum, lowpoints

def part1(lineList):
    cave = convertCave(lineList)
    lowpointsum, lowpoints = getLowPoints(cave)
    return lowpointsum    

def getBasins(lowpoints, cave):
    basins = []
    for i in lowpoints:
        tempbasin = []
        tempbasin.append(i)
        isWorking = True
        while isWorking:
            amountAdded = 0
            for i in tempbasin:
                if i[1] != 0:
                    if cave[i[0]][i[1] - 1] != 9:
                        if [i[0], i[1] - 1] in tempbasin:
                            pass
                        else:
                            tempbasin.append([i[0], i[1] - 1])
                            amountAdded += 1
                if i[0] != 0:
                    if cave[i[0]-1][i[1]] != 9:
                        if [i[0]-1, i[1]] in tempbasin:
                            pass
                        else:
                            tempbasin.append([i[0]-1, i[1]])
                            amountAdded += 1
                if i[1] != len(cave[0]) - 1:
                    if cave[i[0]][i[1] + 1] != 9:
                        if [i[0], i[1] + 1] in tempbasin:
                            pass
                        else:
                            tempbasin.append([i[0], i[1] + 1])
                            amountAdded += 1
                if i[0] != len(cave) - 1:
                    if cave[i[0]+1][i[1]] != 9:
                        if [i[0]+1, i[1]] in tempbasin:
                            pass
                        else:
                            tempbasin.append([i[0]+1, i[1]])
                            amountAdded += 1
            if amountAdded == 0:
                isWorking = False
        basins.append(tempbasin)
    return basins


def part2(lineList):
    cave = convertCave(lineList)
    lowpointsum, lowpoints = getLowPoints(cave)
    basins = getBasins(lowpoints, cave)
    max1 = max(basins, key=len)
    basins.remove(max1)
    max2 = max(basins, key=len)
    basins.remove(max2)
    max3 = max(basins, key=len)
    basins.remove(max3)
    finalansw = len(max1) * len(max2) * len(max3)
    return finalansw 

if __name__ == '__main__':
    lineList = readInput('../inputs/input_09.txt')
    print(part1(lineList))
    print(part2(lineList))