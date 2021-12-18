import sys
sys.path.append('../')
from helper_functions import *

class bingocard:
    def __init__(self, bingosquares):
        self.spots = bingosquares
        self.isFound = [[0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0]]
        self.isWin = False
        self.hasBeenChecked = False

    def printcard(self):
        print(self.spots)
        print(self.isFound)

    def checkspot(self, bingonum):
        for i in self.spots:
            for j in i:
                if j == bingonum:
                    self.isFound[self.spots.index(i)][i.index(j)] = 1
        pass
    
    def checkWin(self):
        if self.isFound[0][0] and self.isFound[0][1] and self.isFound[0][2] and self.isFound[0][3] and self.isFound[0][4]:
            self.isWin = True
        if self.isFound[1][0] and self.isFound[1][1] and self.isFound[1][2] and self.isFound[1][3] and self.isFound[1][4]:
            self.isWin = True
        if self.isFound[2][0] and self.isFound[2][1] and self.isFound[2][2] and self.isFound[2][3] and self.isFound[2][4]:
            self.isWin = True
        if self.isFound[3][0] and self.isFound[3][1] and self.isFound[3][2] and self.isFound[3][3] and self.isFound[3][4]:
            self.isWin = True
        if self.isFound[4][0] and self.isFound[4][1] and self.isFound[4][2] and self.isFound[4][3] and self.isFound[4][4]:
            self.isWin = True
        if self.isFound[0][0] and self.isFound[1][0] and self.isFound[2][0] and self.isFound[3][0] and self.isFound[4][0]:
            self.isWin = True
        if self.isFound[0][1] and self.isFound[1][1] and self.isFound[2][1] and self.isFound[3][1] and self.isFound[4][1]:
            self.isWin = True
        if self.isFound[0][2] and self.isFound[1][2] and self.isFound[2][2] and self.isFound[3][2] and self.isFound[4][2]:
            self.isWin = True
        if self.isFound[0][3] and self.isFound[1][3] and self.isFound[2][3] and self.isFound[3][3] and self.isFound[4][3]:
            self.isWin = True
        if self.isFound[0][4] and self.isFound[1][4] and self.isFound[2][4] and self.isFound[3][4] and self.isFound[4][4]:
            self.isWin = True
        return self.isWin

    def getScore(self, currentcall):
        score = 0
        for m,i in enumerate(self.isFound):
            for n,j in enumerate(i):
                if j == 0:
                    score += int(self.spots[m][n])
        return score * currentcall



def part1(lineList):
    bingonums = lineList[0].split(',')
    lineList.pop(0)
    bingocardinputs = []
    for i in lineList:
        if i == '':
            lineList.remove(i)
    count = 0
    templist = []
    for i in lineList:
        temp = i.split(' ')
        temp = ' '.join(temp).split()
        templist.append(temp)
        count += 1
        if count == 5:
            bingocardinputs.append(templist)
            templist = []
            count = 0
    bingocards = []

    for i in bingocardinputs:
        bingocards.append(bingocard(i))

    round = 1
    for i in bingonums:
        for j in bingocards:
            j.checkspot(i)
        for w in bingocards:
            if w.checkWin():
                return w.getScore(int(i))

        round +=1
    return False

def part2(lineList):
    bingonums = lineList[0].split(',')
    lineList.pop(0)
    bingocardinputs = []
    for i in lineList:
        if i == '':
            lineList.remove(i)
    count = 0
    templist = []
    for i in lineList:
        temp = i.split(' ')
        temp = ' '.join(temp).split()
        templist.append(temp)
        count += 1
        if count == 5:
            bingocardinputs.append(templist)
            templist = []
            count = 0
    bingocards = []

    for i in bingocardinputs:
        bingocards.append(bingocard(i))

    round = 1
    for i in bingonums:
        for j in bingocards:
            j.checkspot(i)
        for w in bingocards:
            if w.checkWin() and not w.hasBeenChecked:
                lastscore = w.getScore(int(i))
                w.hasBeenChecked = True
            round +=1
    return lastscore

if __name__ == '__main__':
    lineList = readInput('../inputs/input_04.txt')
    lineList2 = readInput('../inputs/input_04.txt')
    print(part1(lineList))
    print(part2(lineList2))