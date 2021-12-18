import sys
sys.path.append('../')
from helper_functions import *


def part1(lineList):
    crabbiestr = lineList[0].split(',')
    crabbies = []
    for i in crabbiestr:
        crabbies.append(int(i))
    fuelamounts = []
    for i in range(0, max(crabbies) + 1):
        tempamount = 0
        for j in crabbies:
            tempamount += abs(j - i)
        fuelamounts.append(tempamount)
    return min(fuelamounts)

def part2(lineList):
    crabbiestr = lineList[0].split(',')
    crabbies = []
    for i in crabbiestr:
        crabbies.append(int(i))
    fuelamounts = []
    for i in range(0, max(crabbies) + 1):
        tempamount = 0
        print(i)
        for j in crabbies:
            for k in range(1, abs(j - i) + 1):
                tempamount += k
        fuelamounts.append(tempamount)
    return min(fuelamounts)

if __name__ == '__main__':
    lineList = readInput('../inputs/input_07.txt')
    print(part1(lineList))
    print(part2(lineList))