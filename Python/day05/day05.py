import sys
sys.path.append('../')
from helper_functions import *
import re

class board:
    def __init__(self, maxval):
        self.spots = []
        for i in range(maxval+1):
            temp = []
            for j in range(maxval+1):
                temp.append(0)
            self.spots.append(temp)


    def printBoard(self):
        for i in self.spots:
            print(i)

    def makeMovep1(self, move):
        if move[0] == move[2]:
            for i in range(min([move[1],move[3]]), 1 + max([move[1],move[3]])):
                self.spots[move[0]][i] += 1
        if move[1] == move[3]:
            for i in range(min([move[0],move[2]]), 1 + max([move[0],move[2]])):
                self.spots[i][move[3]] += 1

    
    def makeMovep2(self, move):
        if move[0] == move[2]:
            for i in range(min([move[1],move[3]]), 1 + max([move[1],move[3]])):
                self.spots[move[0]][i] += 1
        if move[1] == move[3]:
            for i in range(min([move[0],move[2]]), 1 + max([move[0],move[2]])):
                self.spots[i][move[3]] += 1

        if move[0] != move[2] and move[1] != move[3]:
            if move[0] < move[2] and move[1] < move[3]:
                for i in range(0, 1 + max([move[0],move[2]]) - min([move[0],move[2]])):
                    self.spots[move[0]+ i][move[1] + i] += 1
            
            if move[0] > move[2] and move[1] > move[3]:
                for i in range(0, 1 + max([move[0],move[2]]) - min([move[0],move[2]])):
                    self.spots[move[0]- i][move[1] - i] += 1
            
            if move[0] < move[2] and move[1] > move[3]:
                for i in range(0, 1 + max([move[0],move[2]]) - min([move[0],move[2]])):
                    self.spots[move[0] + i][move[1] - i] += 1

            if move[0] > move[2] and move[1] < move[3]:
                for i in range(0, 1 + max([move[0],move[2]]) - min([move[0],move[2]])):
                    self.spots[move[0] - i][move[1] + i] += 1
        
        
    
    def checkIntersections(self):
        interNum = 0
        for i in self.spots:
            for j in i:
                if j > 1:
                    interNum += 1
        return interNum

def findMax(moves):
    maximum = 0
    for i in moves:
        for j in i:
            if int(j) > maximum:
                maximum = int(j)
    return maximum

def createMoves(lineList):
    moves = []
    for i in lineList:
        templist = re.split(' -> |,', i)
        moves.append(templist)
    for i in range(0, len(moves)):
        for j in range(0, len(moves[0])):
            moves[i][j] = int(moves[i][j])
    return moves

def part1(lineList):
    moves = createMoves(lineList)
    maxsize = findMax(moves)
    myboard = board(maxsize)
    
    for i in moves:
        myboard.makeMovep1(i)
        
    
    return myboard.checkIntersections()

def part2(lineList):
    moves = createMoves(lineList)
    maxsize = findMax(moves)
    myboard = board(maxsize)
    
    for i in moves:
        myboard.makeMovep2(i)
        
    myboard.printBoard()
    return myboard.checkIntersections()

if __name__ == '__main__':
    lineList = readInput('../inputs/input_05.txt')
    print(part1(lineList))
    print(part2(lineList))