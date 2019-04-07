import pygame

#GLOBAL VARIABLE - NOT RECOMMENDED
UID = 0;

class Person:
    def __init__(self):
        self.uid = UID
        self.name = ""
        self.year = None
        self.quote = ""

    def save(self, s, num, s2):
        """Saves everything into Person Object"""
        UID+=1
        if(self.name==""):
            self.name = s
        if(self.year==None):
            self.year = num
        if(self.quote==""):
            self.quote = s2

    def getName(self):
        return self.name
    
    def getYear(self):
        return self.year
    
    def getQuote(self):
        return self.quote
