#This is where we will put all our imports:
#Regular
import pygame
import sys
import random
import json
#Created
from src import TextInput

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
            if(self.state == "TEXT"):
                self.textLoop()

    def menuLoop(self):
        """This is the Menu Loop of the Game"""
        while self.state == "MENU":
            #BACKGROUND
            self.menuBG = pygame.transform.smoothscale(pygame.image.load('assets/MainMenu.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.menuBG, (0, 0))
            #MOUSE           
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=118 and temp[0]<=228) and (temp[1]>=318 and temp[1]<=409)):
                        self.state = "LIST"
                        self.mainLoop()
                    elif((temp[0]>=396 and temp[0]<=765) and (temp[1]>=174 and temp[1]<=471)):
                        self.state = "GAME"
                        self.mainLoop()
                    elif((temp[0]>=811 and temp[0]<=980) and (temp[1]>=498 and temp[1]<=608)):
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
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
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
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            text = myfont.render("GAME", True, (245,231,20))
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

    def insertLoop(self):
        """This is the List Loop of the Game"""    
        while self.state == "INSERT":
            #BACKGROUND
            self.screen.fill((0,0,0))
            #BUTTONS
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(118, 318, 110, 91), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            text = myfont.render("INSERT", True, (245,231,20))
            self.screen.blit(text, (439, 300))
            #MOUSE           
            pygame.mouse.set_visible(True)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=450 and temp[0]<=550) and (temp[1]>=500 and temp[1]<=600)):
                        self.state = "MENU"
                        self.mainLoop()
                    if((temp[0]>=118 and temp[0]<=228) and (temp[1]>=318 and temp[1]<=409)):
                        self.state = "TEXT"
                        self.mainLoop()
            pygame.display.flip()
            
    def textLoop(self):
        """This is the Text Loop of the Game"""
        clock = pygame.time.Clock()
        textinput = TextInput.TextInput()      
        while self.state == "TEXT":
            #BACKGROUND
            self.screen.fill((255,255,255))
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            text = myfont.render("TEXT", True, (0,0,0))
            self.screen.blit(text, (439, 300))
            #MOUSE           
            pygame.mouse.set_visible(True)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
            #print(events)
            textinput.update(events)
            self.screen.blit(textinput.get_surface(), (10, 10))
            
            #HERE
            if textinput.update(events):
                print(textinput.get_text())

            pygame.display.flip()
            clock.tick(30)
    
