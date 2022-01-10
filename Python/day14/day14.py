import sys
sys.path.append('../')
from helper_functions import *
from time import time

class Polymer:
    def __init__(self, lineList):
        self.template = lineList[0]
        self.rules = []
        for i in lineList[2:]:
            self.rules.append(i.split(' -> '))

    def printState(self):
        print(self.template)
        print(self.rules)

    def step(self):
        newtemplate = ''
        for x in range(0, len(self.template)-1):
            tempstr = str(self.template[x]) + str(self.template[x + 1])
            for j in self.rules:
                if tempstr == j[0]:
                    newtemplate += str(self.template[x])
                    newtemplate += str(j[1])
        newtemplate += str(self.template[len(self.template)-1])
        self.template = newtemplate
        pass

def part1(lineList):
    polymer = Polymer(lineList)
    for i in range(0, 10):
        polymer.step()

    all_char = {}
    for i in polymer.template:
        if i in all_char:
            all_char[i] += 1
        else:
            all_char[i] = 1

    answer = max(all_char.values()) - min(all_char.values())
    
    return answer

def part2(lineList):
    polymer = Polymer(lineList)
    for i in range(0, 40):
        start = time()
        polymer.step()
        print(str(i) + ' - ' + str(time() - start) + 's')

    all_char = {}
    for i in polymer.template:
        if i in all_char:
            all_char[i] += 1
        else:
            all_char[i] = 1

    answer = max(all_char.values()) - min(all_char.values())
    
    return answer

if __name__ == '__main__':
    lineList = readInput('../inputs/input_14.txt')
    print(part1(lineList))
    print(part2(lineList))