#This is where we will put all our imports:
#Regular
import pygame
import sys
import random
import json
#Created
from src import TextInput
from src import Person
from src import ptext
from src import QuoteInfo

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
        self.AllQuotes = QuoteInfo.QuoteInfo()
        self.AllQuotes.countQuotes()
        self.AllQuotes.makeDicts()


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
            if(self.state == "TEXTN"):
                self.text_nLoop()
            if(self.state == "TEXTY"):
                self.text_yLoop()
            if(self.state == "TEXTQ"):
                self.text_qLoop()

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
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #ptext.draw(INSERT TEXT, color = (12,24,45),fontsize=60,fontname='assets/sunshine.ttf')
            #text = myfont.render("QUOTES", True, (245,231,20))
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
        """This is the Game Loop of the Game"""
        #BACKGROUND
        choices = ['assets/Questions1.png', 'assets/Questions2.png','assets/Questions3.png', 'assets/Questions4.png','assets/Questions5.png', 'assets/Questions6.png']
        img_file = random.choice(choices)
        self.gameBG = pygame.transform.smoothscale(pygame.image.load(img_file).convert_alpha(), (self.width,self.height))
        self.screen.blit(self.gameBG, (0, 0))
        #SCREEN WORDS
        myfont = pygame.font.Font('assets/sunshine.ttf', 80)
        ran=random.randint(0, (self.AllQuotes.quoteNum - 2))
        print(ran)
        text = myfont.render((self.AllQuotes.quoteDict[ran][0]), True, (0,0,0))
        ptext.draw(self.AllQuotes.quoteDict[ran][0],(340,90),width = 581,align="center", color = (12,24,45),fontsize=60,fontname='assets/sunshine.ttf')

        #BUTTON WORDS
        answer = self.AllQuotes.quoteDict[ran][1]

        val1 = random.randint(1, self.AllQuotes.quoteNum)
        val2 = random.randint(1, self.AllQuotes.quoteNum)
        val3 = random.randint(1, self.AllQuotes.quoteNum)

        print("Fake1: ",val1)
        print("Fake2: ",val2)
        print("Fake3: ",val3)

        fake1 = self.AllQuotes.quoteDict[val1][1]
        fake2 = self.AllQuotes.quoteDict[val2][1]
        fake3 = self.AllQuotes.quoteDict[val3][1]

        if(fake1 == answer):
            val1 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake1: ",val1)
            fake1 = self.AllQuotes.quoteDict[val1][1]
        if(fake1 == answer):
            val1 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake1: ",val1)
            fake1 = self.AllQuotes.quoteDict[val1][1]
        if(fake1 == answer):
            val1 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake1: ",val1)
            fake1 = self.AllQuotes.quoteDict[val1][1]

        if(fake2 ==answer or fake2==fake1):
            val2 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake2: ",val2)
            fake2 = self.AllQuotes.quoteDict[val2][1]
        if(fake2 ==answer or fake2==fake1):
            val2 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake2: ",val2)
            fake2 = self.AllQuotes.quoteDict[val2][1]
        if(fake2 ==answer or fake2==fake1):
            val2 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake2: ",val2)
            fake2 = self.AllQuotes.quoteDict[val2][1]

        if(fake3 == answer or fake3==fake2 or fake3==fake1):
            val3 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake3: ",val3)
            fake3 = self.AllQuotes.quoteDict[val3][1]
        if(fake3 == answer or fake3==fake2 or fake3==fake1):
            val3 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake3: ",val3)
            fake3 = self.AllQuotes.quoteDict[val3][1]
        if(fake3 == answer or fake3==fake2 or fake3==fake1):
            val3 = random.randint(1, self.AllQuotes.quoteNum)
            print("Fake3: ",val3)
            fake3 = self.AllQuotes.quoteDict[val3][1]

        answerlocation=random.randint(1, 4)

        if(answerlocation==1):
            ptext.draw(answer,(210,426),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake1,(210,557),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake2,(663,439),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake3,(663,564),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
        elif(answerlocation==2):
            ptext.draw(answer,(210,557),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake1,(210,426),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake2,(663,439),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake3,(663,564),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
        elif(answerlocation==3):
            ptext.draw(answer,(663,439),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake1,(210,426),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake2,(210,557),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake3,(663,564),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
        elif(answerlocation==4):
            ptext.draw(answer,(663,564),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake1,(210,426),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake2,(210,557),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')
            ptext.draw(fake3,(663,439),width = 225,lineheight=.7 ,color = (12,24,45),align="center",fontsize=50,fontname='assets/sunshine.ttf')


        while self.state == "GAME":
            #BUTTONS -> JUST FOR TESTING
            #pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(99, 34, 80, 59), 3)
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=99 and temp[0]<=179) and (temp[1]>=34 and temp[1]<=93)):
                        self.state = "MENU"
                        self.mainLoop()
            pygame.display.flip()

    def insertLoop(self):
        """This is the Insert Loop of the Game"""
        #CREATED A PERSON OBJECT
        self.person = Person.Person()

        while self.state == "INSERT":
            #BACKGROUND
            self.insertBG = pygame.transform.smoothscale(pygame.image.load('assets/Insert.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.insertBG, (0, 0))
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
                    if((temp[0]>=249 and temp[0]<=288) and (temp[1]>=603 and temp[1]<=649)):
                        self.state = "MENU"
                        self.mainLoop()
                    if((temp[0]>=98 and temp[0]<=285) and (temp[1]>=293 and temp[1]<=345)):
                        self.state = "TEXTN"
                        self.mainLoop()
                    if((temp[0]>=12 and temp[0]<=201) and (temp[1]>=456 and temp[1]<=508)):
                        self.state = "TEXTY"
                        self.mainLoop()
                    if((temp[0]>=339 and temp[0]<=1044) and (temp[1]>=132 and temp[1]<=617)):
                        self.state = "TEXTQ"
                        self.mainLoop()
            pygame.display.flip()

    def text_nLoop(self):
        """This is the Text Loop of the Game"""
        clock = pygame.time.Clock()
        textinput = TextInput.TextInput()
        while self.state == "TEXTN":
            #BACKGROUND
            self.screen.fill((255,255,255))
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            text = myfont.render("TEXTN", True, (0,0,0))
            self.screen.blit(text, (439, 300))
            #MOUSE
            pygame.mouse.set_visible(True)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_RETURN):
                        fo = open("quotes.json","w")
                        fo.write(textinput.get_text())
                        fo.close()
                        self.state = "INSERT"
                        self.mainLoop()
            #print(events)
            textinput.update(events)
            self.screen.blit(textinput.get_surface(), (10, 10))
            pygame.display.flip()
            clock.tick(30)
