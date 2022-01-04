import pygame
from consts import *


class Card:
    size = 50

    def __init__(self, x, y, c, icon, icon_color, s):
        pygame.init()
        self.x = x
        self.y = y
        self.c = c
        self.fc = LT_GREY
        self.s = s

        self.rect = None
        self.selected = False
        self.icon = icon
        self.icon_color = icon_color
        self.keepOpen = False

    def draw(self):
        self.rect = pygame.draw.rect(
            self.s, self.c, (self.x, self.y, Card.size, Card.size), 3)
        if self.keepOpen:
            self.s.fill(self.fc, self.rect)
            self.draw_icon()
        else:
            self.s.fill(self.c, self.rect)
        self.icon = self.icon
        self.icon_color = self.icon_color
        pygame.display.update()

    def select(self):
        if self.keepOpen or not self.selected:
            self.s.fill(self.fc, self.rect)
            self.draw_icon()

        else:
            self.s.fill(self.c, self.rect)
        self.selected = not(self.selected)

    def isMouseOver(self, mouse_pos):
        mouseX, mouseY = mouse_pos
        if (mouseX >= self.x and mouseX <= self.x+Card.size) and (mouseY >= self.y and mouseY <= self.y+Card.size):
            return True
        return False

    def draw_icon(self):
        if self.icon == UNFILLEDSQUARE:

            pygame.draw.rect(self.s, self.icon_color, (self.x+(Card.size*0.2)/2,
                                                       self.y+(Card.size*0.2)/2, Card.size*0.8, Card.size*0.8),)

        elif self.icon == SQUARE:
            iconObj = pygame.draw.rect(self.s, self.icon_color, (self.x+(
                Card.size*0.2)/2, self.y+(Card.size*0.2)/2, Card.size*0.8, Card.size*0.8), 0)
            self.s.fill(self.icon_color, iconObj)

        elif self.icon == ELLIPSE:
            pygame.draw.ellipse(self.s, self.icon_color, (self.x+(Card.size*0.2)/2,
                                                          self.y+(Card.size*0.2)/2, Card.size*0.8, Card.size*0.5))

        elif self.icon == TRIANGLE:
            pygame.draw.polygon(self.s, self.icon_color, ((self.x+Card.size/2, self.y+Card.size*0.2/2),
                                                          (self.x+Card.size*0.2/2, self.y+Card.size*0.9), (self.x+Card.size*0.9, self.y+Card.size*0.9)))

        elif self.icon == DIFFERENTTRIANGLE:

            pygame.draw.polygon(self.s, self.icon_color, ((self.x+Card.size/2, self.y+Card.size*0.2/2),
                                                          (self.x+Card.size*0.2/2, self.y+Card.size*0.6), (self.x+Card.size*0.6, self.y+Card.size*0.6)))
