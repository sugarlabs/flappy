#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

back = pygame.image.load('images/score_alfa.png')
mes = pygame.image.load('images/init_alfa.png')

class Scores(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.image = back
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]

class CurrentScore(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.points = 0
        self.image = back
        self.size = (50, 50)
        self.font = pygame.font.Font('DejaVuSans-Bold.ttf', 50)
        self.fgColor = (255, 255, 255)
        self.bgColor = (113, 197, 207)
        self._update_image()

    def set_score(self, x):
        self.points = x
        self._update_image()

    def _update_image(self):
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        self.image.set_colorkey(self.bgColor)
        fontSurface = self.font.render(str(self.points), True, self.fgColor)
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        self.image.blit(fontSurface, (xPos, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]

class Message(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.image = mes
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]




