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
        fo = open("quotes.json","r")
        arr = fo.readlines()
        fo.close()
        length=int(len(arr)/3)
        print(length)
        count=0;
        self.personArr = []
        for i in range(length):
            self.newQuote = Person.Person(arr[count].rstrip('\n'),arr[count+1].rstrip('\n'), arr[count+2].rstrip('\n'))
            self.personArr.append(self.newQuote)
            count+=3
        for x in range(len(self.personArr)):
            print(self.personArr[x].quote)
        #BACKGROUND IMAGES
        #FONT
        pygame.font.init()
        #INITIAL STATE
        self.state = "MENU"
        self.AllQuotes = QuoteInfo.QuoteInfo()
        self.AllQuotes.countQuotes()
        self.AllQuotes.makeDicts()
        self.AllQuotes.makePages()


    def mainLoop(self):
        """Controls the state of the game"""
        while True:
            if(self.state == "MENU"):
                self.menuLoop()
            if(self.state == "LIST"):
                self.listLoop()
            if(self.state == "LIST2"):
                self.listLoop2()
            if(self.state == "LIST3"):
                self.listLoop3()
            if(self.state == "LIST4"):
                self.listLoop4()
            if(self.state == "LIST5"):
                self.listLoop5()
            if(self.state == "LIST6"):
                self.listLoop6()
            if(self.state == "LIST7"):
                self.listLoop7()
            if(self.state == "LIST8"):
                self.listLoop8()
            if(self.state == "LIST9"):
                self.listLoop9()
            if(self.state == "LIST10"):
                self.listLoop10()
            if(self.state == "LIST11"):
                self.listLoop11()
            if(self.state == "LIST12"):
                self.listLoop12()
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
            if(self.state == "WIN"):
                self.winLoop()
            if(self.state == "GAMEOVER"):
                self.goLoop()

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

    def text_qLoop(self):
        """This is the Text Loop of the Game"""
        clock = pygame.time.Clock()
        textinput = TextInput.TextInput()
        while self.state == "TEXTQ":
            #BACKGROUND
            self.screen.fill((255,255,255))
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            text = myfont.render("QUOTE", True, (0,0,0))
            self.screen.blit(text, (439, 300))
            #MOUSE
            pygame.mouse.set_visible(True)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_RETURN):
                        fo = open("quotes.json","a")
                        fo.write(textinput.get_text())
                        fo.close()
                        self.state = "INSERT"
                        self.mainLoop()
            #print(events)
            textinput.update(events)
            self.screen.blit(textinput.get_surface(), (10, 10))
            pygame.display.flip()
            clock.tick(30)

    def listLoop(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])

            ptext.draw(self.AllQuotes.pagelist[0][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[0][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[0][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[0][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[0][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[0][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[0][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=951) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST2"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "MENU"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop2(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST2":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
        #    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 2
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST3"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop3(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST3":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 3
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST4"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST2"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop4(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST4":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 4
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(180,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,360),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,565),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,565),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST5"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST3"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop5(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST5":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 6
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,155),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,565),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,565),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST6"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST4"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop6(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST6":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 6
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST7"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST5"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop7(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST7":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 7
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,360),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,360),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST8"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST6"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop8(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST8":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 8
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST9"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST7"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop9(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST9":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 9
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST10"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST8"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop10(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST10":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 10
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST11"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST9"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop11(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST11":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 10
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "LIST12"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST10"
                        self.mainLoop()
            pygame.display.flip()

    def listLoop12(self):
        """This is the List Loop of the Game"""
        while self.state == "LIST12":
            self.listBG = pygame.transform.smoothscale(pygame.image.load('assets/QuotesBlank.png').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.listBG, (0, 0))
            #BUTTONS
            #pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(450, 500, 100, 100), 3)
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            #text = myfont.render((self.AllQuotes.quoteDict[0][0]), True, (0,0,0))
            #print(self.AllQuotes.pagelist[0][0][0])
            curr_page = 10
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][0],(140,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][1],(140,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][0][2],(440,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][1][0],(140,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][1],(140,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][1][2],(440,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][2][0],(140,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][1],(140,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][2][2],(440,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][3][0],(561,23),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][1],(561,115),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][3][2],(861,115),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][4][0],(561,228),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][1],(561,320),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][4][2],(861,320),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')

            ptext.draw(self.AllQuotes.pagelist[curr_page][5][0],(561,433),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][1],(561,525),width = 400,align="left", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            ptext.draw(self.AllQuotes.pagelist[curr_page][5][2],(861,525),width = 400,align="right", color = (12,24,45),fontsize=40,fontname='assets/sunshine.ttf')
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=892 and temp[0]<=992) and (temp[1]>=620 and temp[1]<=675)):
                        self.state = "MENU"
                        self.mainLoop()
                    if((temp[0]>=147 and temp[0]<=217) and (temp[1]>=646 and temp[1]<=675)):
                        self.state = "LIST11"
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
        ran=random.randint(1, (self.AllQuotes.quoteNum))
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
                    if(answerlocation == 1):
                        if((temp[0]>=210 and temp[0]<=416) and (temp[1]>=430 and temp[1]<=518)):
                            self.state = "WIN"
                            self.mainLoop()
                        if((temp[0]>=210 and temp[0]<=416) and (temp[1]>=560 and temp[1]<=644)):
                            self.state = "GAMEOVER"
                            self.mainLoop()
                    if(answerlocation == 2):
                        if((temp[0]>=210 and temp[0]<=416) and (temp[1]>=430 and temp[1]<=518)):
                            self.state = "GAMEOVER"
                            self.mainLoop()
                        if((temp[0]>=210 and temp[0]<=416) and (temp[1]>=560 and temp[1]<=644)):
                            self.state = "WIN"
                            self.mainLoop()
                    if(answerlocation == 3):
                        if((temp[0]>=210 and temp[0]<=416) and (temp[1]>=430 and temp[1]<=518)):
                            self.state = "GAMEOVER"
                            self.mainLoop()
                        if((temp[0]>=623 and temp[0]<=416) and (temp[1]>=430 and temp[1]<=518)):
                            self.state = "WIN"
                            self.mainLoop()
                        if((temp[0]>=210 and temp[0]<=416) and (temp[1]>=560 and temp[1]<=644)):
                            self.state = "GAMEOVER"
                            self.mainLoop()
                    if(answerlocation == 4):
                        if((temp[0]>=210 and temp[0]<=416) and (temp[1]>=430 and temp[1]<=518)):
                            self.state = "GAMEOVER"
                            self.mainLoop()
                        if((temp[0]>=210 and temp[0]<=416) and (temp[1]>=560 and temp[1]<=644)):
                            self.state = "GAMEOVER"
                            self.mainLoop()


            pygame.display.flip()

    def text_yLoop(self):
        clock = pygame.time.Clock()
        textinput = TextInput.TextInput()
        while self.state == "TEXTY":
            #BACKGROUND
            self.screen.fill((255,255,255))
            #SCREEN WORDS
            myfont = pygame.font.Font('assets/BRLNSDB.TTF', 40)
            text = myfont.render("YEAR", True, (0,0,0))
            self.screen.blit(text, (439, 300))
            #MOUSE
            pygame.mouse.set_visible(True)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_RETURN):
                        fo = open("quotes.json","a")
                        fo.write('\n'+textinput.get_text()+'\n')
                        fo.close()
                        self.state = "INSERT"
                        self.mainLoop()
            #print(events)
            textinput.update(events)
            self.screen.blit(textinput.get_surface(), (10, 10))
            pygame.display.flip()
            clock.tick(30)

    def insertLoop(self):
        """This is the Insert Loop of the Game"""
        #BACKGROUND
        self.insertBG = pygame.transform.smoothscale(pygame.image.load('assets/Insert.png').convert_alpha(), (self.width,self.height))
        self.screen.blit(self.insertBG, (0, 0))
        #SCREEN WORDS
        myfont = pygame.font.Font('assets/BRLNSDB.TTF', 23)
        text = myfont.render('Insert: Quote W/ Quote Marks, Name, and Year - Ordered', True, (0,0,0))
        self.screen.blit(text, (444, 100))
        while self.state == "INSERT":
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
                    elif((temp[0]>=98 and temp[0]<=285) and (temp[1]>=293 and temp[1]<=345)):
                        self.state = "TEXTN"
                        self.mainLoop()
                    elif((temp[0]>=12 and temp[0]<=201) and (temp[1]>=456 and temp[1]<=508)):
                        self.state = "TEXTY"
                        self.mainLoop()
                    elif((temp[0]>=339 and temp[0]<=1044) and (temp[1]>=132 and temp[1]<=617)):
                        self.state = "TEXTQ"
                        self.mainLoop()
                    elif((temp[0]>=193 and temp[0]<=235) and (temp[1]>=603 and temp[1]<=646)):
                        self.state = "MENU"
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

    def winLoop(self):
        """
        Game Over Screen
        """
        while self.state == "WIN":
            #BACKGROUND
            self.winBG = pygame.transform.smoothscale(pygame.image.load('assets/uwoncool.jpg').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.winBG, (0, 0))
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=687 and temp[0]<=1022) and (temp[1]>=500 and temp[1]<=667)):
                        self.state = "GAME"
                        self.mainLoop()
                    elif((temp[0]>=57 and temp[0]<=392) and (temp[1]>=500 and temp[1]<=667)):
                        self.state = "MENU"
                        self.mainLoop()
            pygame.display.flip()
    def goLoop(self):
        """
        Game Over Screen
        """
        while self.state == "GAMEOVER":
            #BACKGROUND
            self.goBG = pygame.transform.smoothscale(pygame.image.load('assets/Gameoverrrrr.jpg').convert_alpha(), (self.width,self.height))
            self.screen.blit(self.goBG, (0, 0))
            #MOUSE
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #BUTTON REPLACEMENT (WITH COORDINATES)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    temp=pygame.mouse.get_pos()
                    print(temp)
                    if((temp[0]>=0 and temp[0]<=1080) and (temp[1]>=0 and temp[1]<=720)):
                        self.state = "MENU"
                        self.mainLoop()
            pygame.display.flip()
