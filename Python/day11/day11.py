import sys
sys.path.append('../')
from helper_functions import *

class Cave:
    def __init__(self, cavespots):
        self.spots = []
        for i in lineList:
            temp = []
            for j in i:
                temp.append(int(j))
            self.spots.append(temp)

    def printCave(self):
        for i in self.spots:
            print(i)

    def makeStep(self):
        hasflashed = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        for y, i in enumerate(self.spots):
            for x, j in enumerate(i):
                self.spots[x][y] += 1
        notDone = True
        while notDone:
            amountchange = 0
            for y, i in enumerate(self.spots):
                for x, j in enumerate(i):
                    if j > 9 and hasflashed[y][x] == 0:
                        if y != 0 and x != 0:
                            self.spots[y - 1][x - 1] += 1
                        if y != 0:
                            self.spots[y - 1][x] += 1
                        if y != 0 and x != 9:
                            self.spots[y - 1][x + 1] += 1
                        if x != 9:
                            self.spots[y][x + 1] += 1
                        if y != 9 and x != 9:
                            self.spots[y + 1][x + 1] += 1
                        if y != 9:
                            self.spots[y + 1][x] += 1
                        if y != 9 and x != 0:
                            self.spots[y + 1][x - 1] += 1
                        if x != 0:
                            self.spots[y][x - 1] += 1
                        hasflashed[y][x] = 1
                        amountchange += 1
            if amountchange == 0:
                notDone = False
        totalflashes = 0
        for y, i in enumerate(self.spots):
            for x, j in enumerate(i):
                if j > 9:
                    self.spots[y][x] = 0
                    totalflashes += 1
        
        return totalflashes
        
def part1(lineList):
    cave = Cave(lineList)
    totalflashes = 0
    for i in range(0, 100):
        totalflashes += cave.makeStep()
    return totalflashes

def part2(lineList):
    notDone = True
    cave = Cave(lineList)
    amountStep = 0
    totalflashes = 0
    while notDone:
        totalflashes = cave.makeStep()
        amountStep += 1
        if totalflashes == 100:
            notDone = False
    return amountStep

if __name__ == '__main__':
    lineList = readInput('../inputs/input_11.txt')
    print(part1(lineList))
    print(part2(lineList))