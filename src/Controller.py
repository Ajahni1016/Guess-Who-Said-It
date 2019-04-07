#EXAMPLES FOR THINGS:

'''
ROTATED TEXT
myfont = pygame.font.SysFont('Arial', 40,  True, True)
message = myfont.render("Guess Who Said It", True, (245,231,20))
message = pygame.transform.rotate(message, -20)
self.screen.blit(message, (136,123))
'''

'''
DRAW RECT                       color            x, y, width, height, border
pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(0, 0, 40, 30), 0)
pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(100, 300, 40, 30), 10)
pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(300, 100, 10, 50), 3)
'''

'''
BACKGROUND IMAGES
self.gameBG = pygame.transform.smoothscale(pygame.image.load('assets/bg.<type>').convert_alpha(), (width,height))
self.screen.blit(self.menuBG, (0, 0))
'''


#This is where we will put all our imports:
#Regular
import pygame
import sys
import random
import json
#Created

class Controller:
    def __init__(self, width=1080, height=720):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        #BACKGROUND IMAGES
        #FONT
        pygame.font.init()
        #INITIAL STATE
        self.state = "MENU"

    def mainLoop(self):
        """Controls the state of the game"""
        while True:
            if(self.state == "MENU"):
                self.menuLoop()
            if(self.state == "LIST"):
                self.listLoop()
            if(self.state == "GAME"):
                self.gameLoop()
            if(self.state == "INSERT"):
                self.insertLoop()

    def menuLoop(self):
        """This is the Menu Loop of the Game"""
        while self.state == "MENU":
            #BACKGROUND
            self.screen.fill((0,0,0))
            #BUTTONS
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(148, 256, 100, 100), 0)
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(439, 259, 100, 100), 3)
            pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(742, 253, 100, 100), 6)
            #SCREEN WORDS
            myfont = pygame.font.Font('BRLNSDB.TTF', 40)
            text = myfont.render("PLAY", True, (245,231,20))
            self.screen.blit(text, (439, 300))
            #MOUSE           
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=148 and temp[0]<=248) and (temp[1]>=256 and temp[1]<=356)):
                        self.state = "LIST"
                        self.mainLoop()
                    elif((temp[0]>=439 and temp[0]<=539) and (temp[1]>=259 and temp[1]<=359)):
                        self.state = "GAME"
                        self.mainLoop()
                    elif((temp[0]>=742 and temp[0]<=842) and (temp[1]>=253 and temp[1]<=353)):
                        self.state = "INSERT"
                        self.mainLoop()
            pygame.display.flip()
    
    def listLoop(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST":
            #BACKGROUND
            self.screen.fill((0,0,0))
            #BUTTONS
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('BRLNSDB.TTF', 40)
            text = myfont.render("QUOTES", True, (245,231,20))
            self.screen.blit(text, (439, 300))
            #MOUSE           
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=450 and temp[0]<=550) and (temp[1]>=500 and temp[1]<=600)):
                        self.state = "MENU"
                        self.mainLoop()
            pygame.display.flip()
            
    def gameLoop(self):
        """This is the List Loop of the Game"""
        while self.state == "GAME":
            #BACKGROUND
            self.screen.fill((0,0,0))
            #BUTTONS
            #SCREEN WORDS
            myfont = pygame.font.Font('BRLNSDB.TTF', 40)
            text = myfont.render("GAME", True, (245,231,20))
            self.screen.blit(text, (439, 300))
            #MOUSE           
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            
    def insertLoop(self):
        """This is the List Loop of the Game"""
        while self.state == "INSERT":
            #BACKGROUND
            self.screen.fill((0,0,0))
            #BUTTONS
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('BRLNSDB.TTF', 40)
            text = myfont.render("INSERT", True, (245,231,20))
            self.screen.blit(text, (439, 300))
            #MOUSE           
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=450 and temp[0]<=550) and (temp[1]>=500 and temp[1]<=600)):
                        self.state = "MENU"
                        self.mainLoop()
            pygame.display.flip()
            
