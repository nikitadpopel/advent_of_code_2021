import sys
sys.path.append('../')
from helper_functions import *
from collections import Counter

def scrambled_comparison(letters, word):
    letters = Counter(letters)
    word = Counter(word)
    return all(word[i] <= letters[i] for i in word)

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


class Cipher:
    def __init__(self, cipherinput):
        inputsplit = cipherinput.split(' | ')
        self.inp = inputsplit[0].split(' ')
        self.out = inputsplit[1].split(' ')
        self.key = ['','','','','','','','','','']
        self.Solve()

    def printStat(self):
            print('inputs: ' + str(self.inp))
            print('outputs: ' + str(self.out))
            print('key: ' + str(self.key))

    def Solve(self):
        self.Solve1()
        self.Solve4()
        self.Solve7()
        self.Solve8()
        self.Solve9()
        self.Solve6()
        self.Solve0()
        self.Solve5()
        self.Solve3()
        self.Solve2()

    def Solve1(self):
        for i in self.inp:
            if len(i) == 2:
                self.key[1] = i
                self.inp.remove(i)

    def Solve4(self):
        for i in self.inp:
            if len(i) == 4:
                self.key[4] = i
                self.inp.remove(i)

    def Solve7(self):
        for i in self.inp:
            if len(i) == 3:
                self.key[7] = i
                self.inp.remove(i)

    def Solve8(self):
        for i in self.inp:
            if len(i) == 7:
                self.key[8] = i
                self.inp.remove(i)

    def Solve9(self):
        for i in self.inp:
            if len(i) == 6 and all(x in i for x in self.key[4]):
                self.key[9] = i
                self.inp.remove(i)

    def Solve6(self):
        for i in self.inp:
            if len(i) == 6 and not all(x in i for x in self.key[1]):
                self.key[6] = i
                self.inp.remove(i)

    def Solve0(self):
        for i in self.inp:
            if len(i) == 6:
                self.key[0] = i
                self.inp.remove(i)

    def Solve5(self):
        temp1 = self.key[8]
        temp2 = self.key[6]
        for i in temp1:
            if i not in temp2:
                val = i
        tempval = self.key[9].replace(val, '', 1)
        for i in self.inp:
            if all(x in i for x in tempval):
                self.key[5] = i
                self.inp.remove(i)

    def Solve3(self):
        for i in self.inp:
            if all(x in i for x in self.key[1]):
                self.key[3] = i
                self.inp.remove(i)

    def Solve2(self):
        self.key[2] = self.inp[0]
        self.inp.pop(0)

    def checkVal(self):
        val = 0
        for i in range(0, 10):
            if scrambled_comparison(self.key[i], self.out[0]) and len(self.key[i]) == len(self.out[0]):
                val += i * 1000
        
        for i in range(0, 10):
            if scrambled_comparison(self.key[i], self.out[1]) and len(self.key[i]) == len(self.out[1]):
                val += i * 100 
                
        for i in range(0, 10):
            if scrambled_comparison(self.key[i], self.out[2]) and len(self.key[i]) == len(self.out[2]):
                val += i * 10 

        
        for i in range(0, 10):
            if scrambled_comparison(self.key[i], self.out[3]) and len(self.key[i]) == len(self.out[3]):
                val += i 
        
        return val
        

# oof part 1 was so easy but had to completely rethink for part 2
def part2(lineList):
    decodedvalue = 0
    for i in lineList:
        cipher = Cipher(i)
        decodedvalue += cipher.checkVal()
    return decodedvalue

if __name__ == '__main__':
    lineList = readInput('../inputs/input_08.txt')
    print(part1(lineList))
    print(part2(lineList))

'''
0: abcefg
1: cf
2: acdeg
3: acdfg
4: bcdf
5: abdfg
6: abdefg
7: acf
8: abcdefg
9: abcdfg 

first example:
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe

First off, we can already tell which one of the segment displays are the digits 1, 4, 7, and 8
This is because those four digits all have unique amounts of segments
1: be
4: cgeb
7: edb
8: cfbegad

From here, we can first start with deducing the nine.
We know that the 9 should have all of the values from 4 in it and it will also have six segments
This way, we figure out that...
9: cbdgef

next, we can use this to figure out which one 6 is because it will have six segments but not have one of the segments from 1
6: fgaecd

this leaves us with only one digit that has six segments, 0
0: agebfd

Now that we know what 6 is, we know which segment from 1 is the top right segment which means we can remove that segment from 9 in order to get 5
5: fdcge

We are now left with two values to figure out, 2 and 3
We can figure out 3 by selectively looking at which one of the remaining digits has both segments from 1 remaining and which one doesn't
3: fecdb
2: fabcd

Using these 10 decoded digit values, we can figure out what the output is
fdgacbe cefdb cefbgd gcbe -> 8 3 9 4

'''