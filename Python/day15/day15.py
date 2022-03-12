import sys
sys.path.append('../')
from helper_functions import *
import random

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
    
    def checkFinish(self):
        result =  all(elem in self.ShortPath  for elem in self.spotstr)
        if result:
            return True
        else:
            return False

    def pickVertex(self):
        for i in self.spotstr:
            if i not in self.ShortPath and self.Distance[i] != 9999999999999:
                self.ShortPath.append(i)
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
        adjList = self.getAdjacent(currVert)
        # print('Adjacent Vertices: ' + str(adjList))
        for i in adjList:
            if self.Distance[currVert] + self.spotsval[i] < self.Distance[i]:
                self.Distance[i] = self.Distance[currVert] + self.spotsval[i]
        pass

    def Solve(self):
        iterations = 0
        while not self.checkFinish():
            currVert = self.pickVertex()
            # print('Evaluating Vertex <' + str(currVert) + '>...')
            self.updateAdjacent(currVert)
            iterations += 1
            print(iterations)
        
        self.print()
        return True
        



    def print(self):
        print('\n--- Cave Layout ---')
        for i in self.spots:
            print(i)

        print('\n--- My Shortest Path Set ---')
        print(self.ShortPath)

        print('\n--- My Distances ---')
        print(self.Distance)

        # print('\n--- My Spot Values ---')
        # print(self.spotsval)

def part1(lineList):
    cave = Cave(lineList)
    cave.Solve()
    pass
def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('../inputs/input_15.txt')
    print(part1(lineList))
    print(part2(lineList))