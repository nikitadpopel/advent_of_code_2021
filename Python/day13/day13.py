import sys
sys.path.append('../')
from helper_functions import *

class Board:
    def __init__(self, points):
        self.spots = []
        for i in range(maxY(points)+1):
            temp = []
            for j in range(maxX(points)+1):
                temp.append('.')
            self.spots.append(temp)
    def printBoard(self):
        for i in self.spots:
            print(i)

    def plotPoints(self, points):
        for i in points:
            self.spots[int(i.split(',')[1])][int(i.split(',')[0])] = '#'

    def makeFold(self, fold):
        impInst = fold.split(' ')[-1]
        newInst = impInst.split('=')
        if newInst[0] == 'x':
            self.foldX(newInst[1])
        if newInst[0] == 'y':
            self.foldY(newInst[1])
        pass

    def foldX(self, val):
        newspots = []
        for i in self.spots:
            temp = []
            for j in range(0, int(val)):
                if i[j] == '#' or i[-1-j] == '#':
                    temp.append('#')
                else:
                    temp.append('.')
            newspots.append(temp)
        self.spots = newspots.copy()
        pass

    
    def foldY(self, val):
        newspots = []
        for i in range (0, int(val)):
            temp = []
            for x, j in enumerate(self.spots[i]):
                if self.spots[i][x] == '#' or self.spots[-1-i][x] == '#':
                    temp.append('#')
                else:
                    temp.append('.')
            newspots.append(temp)
        self.spots = newspots.copy()
        pass
    
    def getDots(self):
        dots = 0
        for i in self.spots:
            for j in i:
                if j == '#':
                    dots += 1

        return dots

def maxX(points):
    maxval = 0
    for i in points:
        if int(i.split(',')[0]) > maxval:
            maxval = int(i.split(',')[0])
    return maxval

def maxY(points):
    maxval = 0
    for i in points:
        if int(i.split(',')[1]) > maxval:
            maxval = int(i.split(',')[1])
    return maxval

def part1(lineList):
    splitspot = lineList.index('')
    points = lineList[:splitspot]
    folds = lineList[splitspot+1:]
    board = Board(points)
    board.plotPoints(points)
    board.makeFold(folds[0])
    return board.getDots()

def part2(lineList):
    splitspot = lineList.index('')
    points = lineList[:splitspot]
    folds = lineList[splitspot+1:]
    board = Board(points)
    board.plotPoints(points)
    for i in folds:
        board.makeFold(i)
    board.printBoard()
    return board.getDots()

if __name__ == '__main__':
    lineList = readInput('../inputs/input_13.txt')
    print(part1(lineList))
    print(part2(lineList))