#EXAMPLES FOR THINGS:

'''
ROTATED TEXT
myfont = pygame.font.SysFont('Arial', 40,  True, True)
message = myfont.render("Guess Who Said It", True, (245,231,20))
message = pygame.transform.rotate(message, -20)
self.screen.blit(message, (136,123))
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
        #Example -> self.gameBG = pygame.transform.smoothscale(pygame.image.load('assets/bg.<type>').convert_alpha(), (width,height))
        
        #FONT
        pygame.font.init()
        #INITIAL STATE
        self.state = "MENU"

    def mainLoop(self):
        """Controls the state of the game"""
        while True:
            if(self.state == "MENU"):
                self.menuLoop()
            if(self.state == "GAME"):
                self.gameLoop()
            if(self.state == "INSERT"):
                self.insertLoop()

    def menuLoop(self):
        """This is the Menu Loop of the Game"""
        clock = pygame.time.Clock()
        text_rotate_degrees = 0
        while self.state == "MENU":
            #BACKGROUND
            #self.screen.blit(self.menuBG, (0, 0))
            #SCREEN WORDS
            myfont = pygame.font.Font('BRLNSDB.TTF', 40)
            text = myfont.render("Guess Who Said It", True, (245,231,20))
            self.screen.blit(text, (136,123))
            
            
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    #if((temp[0]>=2 and temp[0]<=342) and (temp[1]>=452 and temp[1]<=485)):
                        #self.state = "GAME"
                        #self.mainLoop()
                    #elif((temp[0]>=357 and temp[0]<=698) and (temp[1]>=451 and temp[1]<=484)):
                        #self.state = "INS"
                        #self.mainLoop()
            
            pygame.display.flip()
            clock.tick(5)
