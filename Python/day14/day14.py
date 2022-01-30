import sys
sys.path.append('../')
from helper_functions import *
from time import time
from collections import Counter

def calculate(template, rules, stepnum):
    answer = 0
    curr_pol = Counter()
    new_pol = None
    chars = None
    for i in range(0, len(template)-1):
        curr_pol[f'{template[i]}{template[i+1]}'] += 1


    for i in range(0, stepnum):
        new_pol = Counter()
        chars = Counter()
        for j,k in curr_pol.items():
            new_pol[f'{j[0]}{rules[j]}'] += k
            new_pol[f'{rules[j]}{j[1]}'] += k
            chars[f'{rules[j]}'] += k
            chars[f'{j[0]}'] += k
        chars[f'{template[-1]}'] += 1
        curr_pol = new_pol
        new_pol = None
    answer = chars.most_common()[0][1] - chars.most_common()[-1][1]
    return answer

def part1(lineList):
    template = lineList[0]
    rules = {}
    for i in lineList[2:]:
        rule = i.split(' -> ')
        rules[rule[0]] = rule[1]
    answer = calculate(template, rules, 10)
    return answer

def part2(lineList):
    template = lineList[0]
    rules = {}
    for i in lineList[2:]:
        rule = i.split(' -> ')
        rules[rule[0]] = rule[1]
    answer = calculate(template, rules, 40)
    return answer

if __name__ == '__main__':
    lineList = readInput('../inputs/input_14.txt')
    print(part1(lineList))
    print(part2(lineList))