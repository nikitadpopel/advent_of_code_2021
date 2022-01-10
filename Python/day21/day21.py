import sys
sys.path.append('../')
from helper_functions import *

class Board:
    def __init__(self, lineList):
        self.p1 = int(lineList[0].split(' ')[-1])
        self.p2 = int(lineList[1].split(' ')[-1])
        self.p1s = 0
        self.p2s = 0
        self.die = 0
        self.diet = 0
    
    def printBoard(self):
        print('Player 1 Position: ' + str(self.p1) + '   Score: ' + str(self.p1s))
        print('Player 2 Position: ' + str(self.p2) + '   Score: ' + str(self.p2s))

    def movep1(self):
        self.die += 1
        if self.die > 100:
            self.die = 1
        self.p1 += self.die
        print('Player 1 rolls ' + str(self.die))
        if self.p1 > 10:
            self.p1 = self.p1 % 10
            if self.p1 == 0:
                self.p1 = 10
        self.die += 1
        print('Player 1 rolls ' + str(self.die))
        if self.die > 100:
            self.die = 1
        self.p1 += self.die
        if self.p1 > 10:
            self.p1 = self.p1 % 10
            if self.p1 == 0:
                self.p1 = 10
        self.die += 1
        print('Player 1 rolls ' + str(self.die))
        if self.die > 100:
            self.die = 1
        self.p1 += self.die
        if self.p1 > 10:
            self.p1 = self.p1 % 10
            if self.p1 == 0:
                self.p1 = 10
        self.p1s += self.p1
        self.diet += 3
    
    def movep2(self):
        self.die += 1
        if self.die > 100:
            self.die = 1
        self.p2 += self.die
        print('Player 2 rolls ' + str(self.die))
        if self.p2 > 10:
            self.p2 = self.p2 % 10
            if self.p2 == 0:
                self.p2 = 10
        self.die += 1
        if self.die > 100:
            self.die = 1
        self.p2 += self.die
        print('Player 2 rolls ' + str(self.die))
        if self.p2 > 10:
            self.p2 = self.p2 % 10
            if self.p2 == 0:
                self.p2 = 10
        self.die += 1
        if self.die > 100:
            self.die = 1
        self.p2 += self.die
        print('Player 2 rolls ' + str(self.die))
        if self.p2 > 10:
            self.p2 = self.p2 % 10
            if self.p2 == 0:
                self.p2 = 10
        self.p2s += self.p2
        self.diet += 3
        
def part1(lineList):
    board = Board(lineList)
    board.printBoard()
    while True:
        board.movep1()
        if board.p1s >= 1000:
            break
        board.movep2()
        if board.p2s >= 1000:
            break
    if board.p1s >= 1000:
            return board.p2s * board.diet
    if board.p2s >= 1000:
            return board.p1s * board.diet
    
    pass

def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('../inputs/input_21.txt')
    print(part1(lineList))
    print(part2(lineList))