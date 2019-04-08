import pygame
import json

#GLOBAL VARIABLE - NOT RECOMMENDED
quoteNum = 0;

class QuoteInfo:
    def __init__(self):
        self.fo = open("assets/QuoteList.txt", "r")
        self.lines = self.fo.read().splitlines()
        self.quoteDict = {}
        self.quoteNum = 0
        self.pagelist = []

    def countQuotes(self):
        count = 0
        for x in self.lines:
            count+=1
        print("Number of Lines in Quotes Files: ",count)
        self.quoteNum = count // 3
        print("Number of Quotes: ",self.quoteNum)

    def makeDicts(self):
        qCount = 1

        for i in range(0,self.quoteNum):
            listy = []
            listy.append(self.lines[(i*3)-3])
            listy.append(self.lines[(i*3)-2])
            listy.append(self.lines[(i*3)-1])
            self.quoteDict.update({i+1:listy})
        #print(self.quoteDict)

    def makePages(self):
        pages = self.quoteNum//6
        counter = 1
        where = 1
        for i in range(0,pages):
            listy= []
            for x in range(0,6):
                listy.append(self.quoteDict[where])
                where+=1
            self.pagelist.append(listy)
        #print("YES")
        #print(self.pagelist)
