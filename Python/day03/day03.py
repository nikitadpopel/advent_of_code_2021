import sys
sys.path.append('../')
from helper_functions import *

def getBinaryList(lineList):
    binaryList = []
    for i in lineList:
        newBinaryNum = []
        for j in i:
            newBinaryNum.append(j)
        binaryList.append(newBinaryNum)
    return binaryList

def getGammaRate(binaryList):
    gammaRate = []
    for i in range(len(binaryList[0])):
        oneCnt = 0
        zeroCnt = 0
        for j in binaryList:
            if j[i] == '1':
                oneCnt += 1
            if j[i] == '0':
                zeroCnt += 1
        if oneCnt > zeroCnt:
            gammaRate.append('0')
        if zeroCnt > oneCnt:
            gammaRate.append('1')
    return gammaRate

def getEpsilonRate(binaryList):
    gammaRate = []
    for i in range(len(binaryList[0])):
        oneCnt = 0
        zeroCnt = 0
        for j in binaryList:
            if j[i] == '1':
                oneCnt += 1
            if j[i] == '0':
                zeroCnt += 1
        if oneCnt > zeroCnt:
            gammaRate.append('1')
        if zeroCnt > oneCnt:
            gammaRate.append('0')
    return gammaRate

def readBinary(binaryNum):
    decimal = 0
    for i in range(len(binaryNum)):
        if binaryNum[i] == '1':
            decimal += 2 ** (len(binaryNum) - i - 1)
    return decimal

def getOxyGenRating(binaryList):
    for i in range(len(binaryList[0])):
        oneCnt = 0
        zeroCnt = 0
        deletionList = []
        for j in binaryList:
            if j[i] == '1':
                oneCnt += 1
            if j[i] == '0':
                zeroCnt += 1
        if oneCnt >= zeroCnt:
            for k in binaryList:
                if k[i] == '0':
                    deletionList.append(k)
        else:
            for k in binaryList:
                if k[i] == '1':
                    deletionList.append(k)
        for m in deletionList:
            binaryList.remove(m)
    return binaryList[0]

def getCO2ScrubberRating(binaryList2):
    print(binaryList2)
    for i in range(len(binaryList2[0])):
        oneCnt = 0
        zeroCnt = 0
        deletionList = []
        for j in binaryList2:
            if j[i] == '1':
                oneCnt += 1
            if j[i] == '0':
                zeroCnt += 1
        print(str(i) + ' : ' + str(zeroCnt) + ' ------ ' + str(oneCnt))
        if zeroCnt <= oneCnt:
            for k in binaryList2:
                if k[i] == '1':
                    deletionList.append(k)
        else:
            for k in binaryList2:
                if k[i] == '0':
                    deletionList.append(k)
        for m in deletionList:
            binaryList2.remove(m)
        print('                  ' + str(binaryList2))
        if len(binaryList2) == 1:
            break
    print(binaryList2)
    return binaryList2[0]

def part1(lineList):
    binaryList = getBinaryList(lineList)
    gammaRate = readBinary(getGammaRate(binaryList))
    epsilonRate = readBinary(getEpsilonRate(binaryList))
    return gammaRate * epsilonRate

def part2(lineList):
    binaryList = getBinaryList(lineList)
    binaryList2 = getBinaryList(lineList)
    OxyGenRating = readBinary(getOxyGenRating(binaryList))
    CO2ScrubberRating = readBinary(getCO2ScrubberRating(binaryList2))
    print('Oxygen ' + str(OxyGenRating))
    print('CO2 ' + str(CO2ScrubberRating))
    return OxyGenRating * CO2ScrubberRating

if __name__ == '__main__':
    lineList = readInput('../inputs/input_03.txt')
    print(part1(lineList))
    print(part2(lineList))