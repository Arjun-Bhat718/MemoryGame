import pygame
from card import *
from consts import *
import time
import random
import sys
import json
import requests
from firebase import firebase
num = 0

pygame.init()
nameEntered = False

user_name = input("What is your name?")
screen_size = 1000, 400
font = pygame.font.SysFont(None, 40)
cardPairsFound = font.render('Cards Found:', True, BLUE)
leaderboardText = font.render('Leaderboard', True, BLUE)

cardPairsNumber = font.render('0', True, BLUE)
pics = []

seahawks = pygame.image.load(
    'C:\\Users\\damod\Desktop\\SKC Python Workspace\\Memory Game\\1.jpg')


def start_menu():

    mousePos = pygame.mouse.get_pos()
    menuDisplay = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption('Start Menu')
    menuDisplay.fill(LT_GREEN)
    font = pygame.font.SysFont(None, 40)
    bigText = font.render('Memory Game', True, LT_GREEN)
    newText = font.render('Start', True, BLACK)
    exitText = font.render('Exit', True, BLACK)
    leaderboardText = font.render('Leaderboard', True, BLACK)

    nameConcatenate = 'Name: '+user_name
    nameText = font.render(nameConcatenate, True, BLUE)
    menuDisplay.blit(nameText, (50, 10))
    pygame.draw.ellipse(menuDisplay, BLUE, (250, 50, 500, 100))
    menuDisplay.blit(bigText, (410, 85))
    pygame.draw.rect(menuDisplay, LT_GREEN, (340, 220, 300, 50))

    pygame.draw.rect(menuDisplay, LT_GREEN, (340, 380, 300, 50))
    pygame.draw.ellipse(menuDisplay, LT_GREY, (340, 220, 300, 50))

    pygame.draw.ellipse(menuDisplay, LT_GREY, (340, 300, 300, 50))
    menuDisplay.blit(newText, (445, 230))
    menuDisplay.blit(exitText, (455, 310))

    pygame.draw.ellipse(menuDisplay, LT_GREY, (340, 380, 300, 50))
    menuDisplay.blit(leaderboardText, (400, 390))

    if mousePos[0] > 339 and mousePos[0] < 639 and mousePos[1] > 220 and mousePos[1] < 270:
        newText = font.render('Start(S)', True, BLUE)
        menuDisplay.blit(newText, (445, 230))
        # if event == pygame.KEYDOWN:

        #     if pygame.MOUSEBUTTONUP:
        #         game()
    elif mousePos[0] > 339 and mousePos[0] < 639 and mousePos[1] > 300 and mousePos[1] < 350:
        exitText = font.render('Exit(ESC)', True, BLUE)
        menuDisplay.blit(exitText, (455, 310))

    elif mousePos[0] > 339 and mousePos[0] < 639 and mousePos[1] > 380 and mousePos[1] < 430:
        leaderboardText = font.render('Leaderboard(SHIFT)', True, BLUE)
        menuDisplay.blit(leaderboardText, (400, 390))


for l in range(2):
    icons = set(SHAPES)

    for x in range(len(SHAPES)):
        i = icons.pop()
        icon_colors = set(COLORS)
        for y in range(len(COLORS)):
            ic = icon_colors.pop()
            pics.append((i, ic))

for l in range(10):
    random.shuffle(pics)

SURFACE = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Memory Card Game')
SURFACE.fill(LT_GREEN)

cardsList = []


for x in [x*60 for x in range(1, 10)]:
    for y in [y*60 for y in range(1, 5)]:
        image = pics.pop()
        card = Card(x, y, BLUE, image[0], image[1], SURFACE)
        cardsList.append(card)
gameStart = False
leaderboard = False

while not gameStart and not leaderboard:
    menu = True
    num += 1
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:

                if mousePos[0] > 339 and mousePos[0] < 639 and mousePos[1] > 220 and mousePos[1] < 270:
                    print('key pressed')
                    print('game start')
                    gameStart = True
                    menu = False
            elif event.key == pygame.K_ESCAPE:
                if mousePos[0] > 339 and mousePos[0] < 639 and mousePos[1] > 300 and mousePos[1] < 350:
                    pygame.quit()
                    quit()

            elif event.key == pygame.K_LSHIFT:
                print('key pressed')
                if mousePos[0] > 339 and mousePos[0] < 639 and mousePos[1] > 380 and mousePos[1] < 430:
                    print('key pressed inside')
                    SURFACE.fill(LT_GREEN)
                    leaderboard = True

    mousePos = pygame.mouse.get_pos()

    start_menu()
    pygame.display.update()


SURFACE.fill(LT_GREEN)
if not leaderboard:

    for card in cardsList:
        card.draw()
    time.sleep(1)

    for k in range(5):
        reveals = [random.randint(0, len(cardsList)-1) for x in range(10)]

        for i in range(len(cardsList)):
            if i in reveals:
                cardsList[i].keepOpen = True

        for card in cardsList:
            card.draw()

        for i in range(len(cardsList)):
            cardsList[i].keepOpen = False
        time.sleep(1)

    for card in cardsList:
        card.draw()

    pairOfCards = set()
    cardFound = 0
    SURFACE.blit(cardPairsFound, (10, 10))
    SURFACE.blit(cardPairsNumber, (200, 10))


while not menu and not leaderboard:

    quitText = font.render('Quit', True, BLACK)
    mousePos = pygame.mouse.get_pos()
    pygame.draw.ellipse(SURFACE, LT_GREY, (450, 350, 300, 50))
    SURFACE.blit(quitText, (560, 365))

    for event in pygame.event .get():
        if event.type == pygame.KEYDOWN:
            if mousePos[0] > 449 and mousePos[0] < 749 and mousePos[1] > 349 and mousePos[1] < 400:
                print('in range')
                leaderboard = True

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            for card in cardsList:
                if card.isMouseOver(pygame.mouse.get_pos()):
                    if len(pairOfCards) < 2:
                        card.select()

                        pairOfCards.add(card)
                    else:
                        pairOfCards = list(pairOfCards)
                        if pairOfCards[0].icon == pairOfCards[1].icon and pairOfCards[0].icon_color == pairOfCards[1].icon_color:
                            cardFound = int(cardFound)
                            pairOfCards[0].keepOpen = True
                            pairOfCards[1].keepOpen = True
                            cardFound += 1
                            cardFound = str(cardFound)
                            cardPairsNumber = font.render(
                                cardFound, True, BLUE)

                            SURFACE.fill(LT_GREEN)
                            for card in cardsList:
                                card.draw()
                            SURFACE.blit(cardPairsFound, (10, 10))
                            SURFACE.blit(cardPairsNumber, (200, 10))

                        pairOfCards[0].select()
                        pairOfCards[1].select()
                        pairOfCards = set(pairOfCards)
                        pairOfCards.clear()
                        card.select()
                        pairOfCards.add(card)
    pygame.display.update()
m = 0
while leaderboard:
    for event in pygame.event .get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if m < 2:
        SURFACE.fill(GREEN)
        SURFACE.blit(leaderboardText, (400, 40))
        for event in pygame.event .get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for i in range(0, 3):
            m += 1
            m = str(m)
            nameUrl = "https://memorygameleaderboard.firebaseio.com/Player%20"+m+"/Name.json"
            scoreUrl = "https://memorygameleaderboard.firebaseio.com/Player%20"+m+"/Score.json"

            nameResult = requests.get(nameUrl)
            scoreResult = requests.get(scoreUrl)
            name = json.loads(nameResult.content.decode())
            name = str(name)
            score = json.loads(scoreResult.content.decode())
            score = str(score)
            cocatenatedScore = name+'  '+score
            concatenatedText = font.render(cocatenatedScore, True, BLUE)
            SURFACE.blit(concatenatedText, (400, 100+(i*50)))
            m = int(m)
        # time.sleep(60)

        pygame.display.update()
