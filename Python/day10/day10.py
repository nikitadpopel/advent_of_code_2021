import sys
sys.path.append('../')
from helper_functions import *
import statistics

def checkLeft(bracket):
    if bracket in ['(',  '[', '{', '<']:
        return True
    else:
        return False


def checkMatch(left, right):
    if left == '(' and right != ')':
        return False
    if left == '[' and right != ']':
        return False
    if left == '{' and right != '}':
        return False
    if left == '<' and right != '>':
        return False
    return True

def getComplete(line):
    returnline = ''
    for i in reversed((line)):
        if i == '(':
            returnline += ')'
        if i == '[':
            returnline += ']'
        if i == '{':
            returnline += '}'
        if i == '<':
            returnline += '>'
    return returnline

def getFinalScore(completeList):
    scorelist = []
    for i in completeList:
        score = 0
        for j in i:
            score = score * 5
            if j == ')':
                score += 1
            if j == ']':
                score += 2
            if j == '}':
                score += 3
            if j == '>':
                score += 4
        scorelist.append(score)
    return scorelist


def part1(lineList):
    totalscore = 0
    for i in lineList:
        temp = []
        notFinished = 1
        for j in i:
            if notFinished:
                if checkLeft(j):
                    temp.append(j)
                else:
                    if checkMatch(temp[-1], j):
                        temp.pop(-1)
                    else:
                        notFinished = 0
                        if j == ')':
                            totalscore += 3
                        if j == ']':
                            totalscore += 57
                        if j == '}':
                            totalscore += 1197
                        if j == '>':
                            totalscore += 25137
            
    return totalscore

def part2(lineList):
    totalscore = 0
    newList = []
    for i in lineList:
        temp = []
        notFinished = 1
        for j in i:
            if notFinished:
                if checkLeft(j):
                    temp.append(j)
                else:
                    if checkMatch(temp[-1], j):
                        temp.pop(-1)
                    else:
                        notFinished = 0
        if notFinished:
            newList.append(temp)
    
    completeList = []
    for i in newList:
        completeList.append(getComplete(i))
    totalscores = getFinalScore(completeList)
    totalscore = statistics.median(totalscores)
    return totalscore

if __name__ == '__main__':
    lineList = readInput('../inputs/input_10.txt')
    print(part1(lineList))
    print(part2(lineList))