import sys
sys.path.append('../')
from helper_functions import *
import random
import time

class Cave:
    def __init__(self, lineList):
        self.spots = []
        for i in lineList:
            temp = []
            for j in i:
                temp.append(j)
            self.spots.append(temp)
        self.spotsval = {}
        for y, j in enumerate(self.spots):
            for x, i in enumerate(j):
                self.spotsval[str(x) + ' ' + str(y)] = int(i)
                
        self.ShortPath = []
        self.Distance = {}
        self.spotstr = []
        self.maxX = len(lineList[0])
        self.maxY = len(lineList)
        for i in range(self.maxX):
            for j in range(self.maxY):
                self.Distance[str(i) + ' ' + str(j)] = 9999999999999
                self.spotstr.append(str(i) + ' ' + str(j))

        self.Distance['0 0'] = 0

    def pickVertex(self):
        for i in self.spotstr:
            if self.Distance[i] != 9999999999999:
                
                self.ShortPath.append(i)
                self.spotstr.remove(i)
                return i
        return False

    def getAdjacent(self, currVert):
        adjList = []
        xVal = int(currVert.split(' ')[0])
        yVal = int(currVert.split(' ')[1])
        if xVal != 0:
            adjList.append(str(xVal - 1) + ' ' + str(yVal))
        
        if xVal != self.maxX - 1:
            adjList.append(str(xVal + 1) + ' ' + str(yVal))

        if yVal != 0:
            adjList.append(str(xVal) + ' ' + str(yVal - 1))
        
        if yVal != self.maxY - 1:
            adjList.append(str(xVal) + ' ' + str(yVal + 1))
        return adjList

    def updateAdjacent(self, currVert):
        if not currVert:
            return
        adjList = self.getAdjacent(currVert)
        for i in adjList:
            if self.Distance[currVert] + self.spotsval[i] < self.Distance[i]:
                self.Distance[i] = self.Distance[currVert] + self.spotsval[i]
        return

    def SolveDijkstras(self):
        while str(self.maxX - 1) + ' ' + str(self.maxY - 1) not in self.ShortPath:
            currVert = self.pickVertex()
            self.updateAdjacent(currVert)
        return self.Distance[str(self.maxX-1) + ' ' + str(self.maxY - 1)]

    def print(self):
        print('\n--- Cave Layout ---')
        for i in self.spots:
            print(i)

        # print('\n--- My Shortest Path Set ---')
        # print(self.ShortPath)

        # print('\n--- My Distances ---')
        # print(self.Distance)

        # print('\n--- My Spot Values ---')
        # print(self.spotsval)
def extendCave(lineList):
    intList = []
    newList = lineList
    for i in lineList:
        tempList = []
        for j in i:
            tempList.append(int(j))
        intList.append(tempList)
    # for i in range(5):
    addedVals = intList.copy()
    for y,j in enumerate(addedVals):
        for x,k in enumerate(j):
            if k == 9:
                addedVals[y][x] = 0
            else:
                addedVals[y][x] = k + 1
    print(addedVals)
    print('-----')
    for m in addedVals:
        print(m)
        intList.append(m)
    print(intList)
    return intList

def part1(lineList):
    cave = Cave(lineList)
    return cave.SolveDijkstras()

def part2(lineList):
    lineListExtended = extendCave(lineList)
    cave = Cave(lineListExtended)
    cave.print()
    return cave.SolveDijkstras()

if __name__ == '__main__':
    lineList = readInput('../inputs/input_15.txt')
    print(part1(lineList))
    print(part2(lineList))