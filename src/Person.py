import pygame

class Person:
    def __init__(self, quote, name, num):
        self.name = name
        self.year = num
        self.quote = quote

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

    def getQuote(self):
        return self.quote
    
