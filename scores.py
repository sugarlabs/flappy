#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

back = pygame.image.load('images/score_alfa.png')
mes = pygame.image.load('images/init_alfa.png')

class EndScore(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.score = 0
        self.best = 0
        self.font = pygame.font.Font('DejaVuSans-Bold.ttf', 40)
        self.fgColor = (255, 255, 255)
        self._update_image()

    def update_scores(self, score, best):
        self.score = score
        self.best = best
        self._update_image()

    def _update_image(self):
        self.image = back.copy()
        fontSurface = self.font.render(str(self.score), True, self.fgColor)
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        self.image.blit(fontSurface, (xPos, 35))
        fontSurface = self.font.render(str(self.best), True, self.fgColor)
        xPos = (self.image.get_width() - fontSurface.get_width())/2
        self.image.blit(fontSurface, (xPos, 97))
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]
    

class CurrentScore(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.points = 0
        self.image = back
        self.size = [50, 50]
        self.font = pygame.font.Font('DejaVuSans-Bold.ttf', 50)
        self.fgColor = (255, 255, 255)
        self.bgColor = (113, 197, 207)
        self._update_image()

    def set_score(self, x):
        self.points = x
        self._update_image()

    def _update_image(self):
        fontSurface = self.font.render(str(self.points), True, self.fgColor)
        self.size[0] = fontSurface.get_width()
        self.image = pygame.Surface(self.size)
        self.image.fill(self.bgColor)
        self.image.set_colorkey(self.bgColor)
        self.image.blit(fontSurface, (0, 0))
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




