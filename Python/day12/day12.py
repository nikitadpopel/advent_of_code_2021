import sys
sys.path.append('../')
from helper_functions import *
import random

class CaveSys:
    def __init__(self, lineList):
        self.caves = []
        for i in lineList:
            if i.split('-')[0] in self.caves:
                pass
            else:
                self.caves.append(i.split('-')[0])
            if i.split('-')[1] in self.caves:
                pass
            else:
                self.caves.append(i.split('-')[1])
        self.possib = []
        for i in self.caves:
            temp = []
            for j in lineList:
                temppos = j.split('-')
                if i in temppos:
                    if temppos[0] == i:
                        temp.append(temppos[1])
                    if temppos[1] == i:
                        temp.append(temppos[0])
            self.possib.append([i, temp])
        self.smallcaves = []
        for i in self.caves:
            if i.islower():
                if i in ['start', 'end']:
                    pass
                else:
                    self.smallcaves.append(i)

    def printCave(self):
        for i in self.possib:
            print(str(i[0]) + ' - ' + str(i[1]))

    def getPaths(self):
        pass

    def getPossib(self, currentNode):
        for i in self.possib:
            if i[0] == currentNode:
                return i[1]
        return 0

    def getRandoms1(self):
        
        possib = []

        
        possib.append(['start'])
        notDone = True
        
        finalans = []
        temp = -1
        temp2 = -2
        while notDone:
            temppaths = []
            for x,i in enumerate(possib):
                newlist = list(i)
                if i[-1] != 'end':
                    for j in self.getPossib(i[-1]):
                        if j != 'start':
                            if i.count(j) > 0 and j in self.smallcaves:
                                pass
                            else:
                                templist = list(newlist)
                                templist.append(j)
                                temppaths.append(templist)
                
                
                
            
            possib = temppaths.copy()
            for i in possib:
                if i[-1] == 'end':
                    finalans.append(i)
            if len(finalans) == temp2:
                notDone = False
            temp2 = temp
            temp = len(finalans)
        return len(finalans)
        
    def getRandoms2(self):
        
        possib = []

        
        possib.append(['start'])
        notDone = True
        
        finalans = []
        temp = -1
        temp2 = -2
        while notDone:
            temppaths = []
            for x,i in enumerate(possib):
                newlist = list(i)
                notVisited = True
                if i[-1] != 'end':
                    for j in self.getPossib(i[-1]):
                        if j != 'start':
                            for k in i:
                                if k in self.smallcaves and i.count(k) == 2:
                                    notVisited = False
                                    
                            if notVisited:
                                if i.count(j) > 1 and j in self.smallcaves:
                                    pass
                                else:
                                    templist = list(newlist)
                                    templist.append(j)
                                    temppaths.append(templist)
                            else:
                                if i.count(j) > 0 and j in self.smallcaves:
                                    pass
                                else:
                                    templist = list(newlist)
                                    templist.append(j)
                                    temppaths.append(templist)
                
                
                
            
            possib = temppaths.copy()
            for i in possib:
                if i[-1] == 'end':
                    finalans.append(i)
            if len(finalans) == temp2:
                notDone = False
            temp2 = temp
            temp = len(finalans)
        return len(finalans)
        

def part1(lineList):
    cavesys = CaveSys(lineList)
    possibilities = cavesys.getRandoms1()
    return possibilities

def part2(lineList):
    cavesys = CaveSys(lineList)
    possibilities = cavesys.getRandoms2()
    return possibilities

if __name__ == '__main__':
    lineList = readInput('../inputs/input_12.txt')
    print(part1(lineList))
    print(part2(lineList))