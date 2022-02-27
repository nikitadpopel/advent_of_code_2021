import sys
sys.path.append('../')
from helper_functions import *
import random

def printGrid(grid):
    for i in grid:
        print(i)

def solveGrid(grid):
    value = 0
    xVal = len(grid[0])
    yVal = len(grid)
    for i in range(0, 1000):
        temp = [0, 0]
        templist = [[0,0]]
        isValid = True
        tempval = int(grid[0][0])
        while isValid:
            isSpot = True
            options = ["right", "down", "left", "up"]
            
            while isSpot:
                if len(options) == 0:
                    isValid = False
                    isSpot = False
                    break
                tempchoice = random.choice(options)
                if tempchoice == "right":
                    #first we check the square to the right
                    if temp[0] > xVal and [temp[0] + 1, temp[1]] not in templist:
                        temp = [temp[0] + 1, temp[1]]
                        templist.append(temp)
                        isSpot = False
                        print(temp[0])
                        print(temp[1])
                        tempval += int(grid[temp[0]][temp[1]])
                    options.remove("right")
                if tempchoice == "down":
                    if temp[1] > yVal and [temp[0], temp[1] + 1] not in templist:
                        temp = [temp[0], temp[1] + 1]
                        templist.append(temp)
                        isSpot = False
                    options.remove("down")
                if tempchoice == "left":
                    if temp[0] != 0 and [temp[0] - 1, temp[1]] not in templist:
                        temp = [temp[0] - 1, temp[1]]
                        templist.append(temp)
                        isSpot = False
                    options.remove("left")
                if tempchoice == "up":
                    if temp[1] != 0 and [temp[0], temp[1] - 1] not in templist:
                        temp = [temp[0], temp[1] - 1]
                        templist.append(temp)
                        isSpot = False
                    options.remove("up")

        print(templist)
    return value

         


def part1(lineList):
    grid = []
    for i in lineList:
        temp = []
        for j in i:
            temp.append(j)
        grid.append(temp)
    printGrid(grid)
    solveGrid(grid)
    answer = 0
    return answer
def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('../inputs/input_15.txt')
    print(part1(lineList))
    print(part2(lineList))