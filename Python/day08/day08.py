import sys
sys.path.append('../')
from helper_functions import *

def uniqueVals(signalList):
    uniqueVal = 0
    for i in signalList:
        if len(i) in [2, 3, 4, 7]:
            uniqueVal += 1
    return uniqueVal
    

def makeSignalList(lineList):
    signalList = []
    for i in range(0, len(lineList)):
        splitlist = lineList[i].split(' | ')
        outvals = splitlist[1].split(' ')
        for i in outvals:
            signalList.append(i)
    return signalList

# easy
def part1(lineList):
    signalList = makeSignalList(lineList)
    return uniqueVals(signalList)

# oof part 1 was so easy but had to completely rethink for part 2
def part2(lineList):
    pass

if __name__ == '__main__':
    lineList = readInput('../inputs/input_08.txt')
    print(part1(lineList))
    print(part2(lineList))