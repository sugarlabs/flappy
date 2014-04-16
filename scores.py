#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from gettext import gettext as _

back = pygame.image.load('data/images/score_alfa.png')
mes = pygame.image.load('data/images/init_alfa.png')

class EndScore(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.score = 0
        self.best = 0
        self.font20 = pygame.font.Font('data/DejaVuSans-Bold.ttf', 20)
        self.font30 = pygame.font.Font('data/DejaVuSans-Bold.ttf', 30)
        self.font40 = pygame.font.Font('data/DejaVuSans-Bold.ttf', 40)
        self.fgColor = (255, 255, 255)
        self.mes_color = (252, 120, 88)
        self.mes_score = _('Score')
        self.mes_best = _('Best')
        self.mes_button = _('Restart')
        self._update_image()

    def update_scores(self, score, best):
        self.score = score
        self.best = best
        self._update_image()

    def _update_image(self):
        self.image = back.copy()
        w = self.image.get_width()
        # score
        fontSurface = self.font20.render(self.mes_score, True, self.mes_color)
        xPos = (w - fontSurface.get_width())/2
        self.image.blit(fontSurface, (xPos, 10))
        # score number
        fontSurface = self.font40.render(str(self.score), True, self.fgColor)
        xPos = (w - fontSurface.get_width())/2
        self.image.blit(fontSurface, (xPos, 35))
        # best
        fontSurface = self.font20.render(self.mes_best, True, self.mes_color)
        xPos = (w - fontSurface.get_width())/2
        self.image.blit(fontSurface, (xPos, 80))
        # best number
        fontSurface = self.font40.render(str(self.best), True, self.fgColor)
        xPos = (w - fontSurface.get_width())/2
        self.image.blit(fontSurface, (xPos, 97))
        # restart
        fontSurface = self.font30.render(self.mes_button, True, self.fgColor)
        xPos = (w - fontSurface.get_width())/2
        self.image.blit(fontSurface, (xPos, 185))
        # update rect
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]
    

class CurrentScore(pygame.sprite.Sprite):

    def __init__(self, parent, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.parent = parent
        self.mPos = [x, y]
        self.points = 0
        self.image = back
        self.size = [50, 50]
        self.font = pygame.font.Font('data/DejaVuSans-Bold.ttf', 50)
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
        self.mPos[0] = (self.parent.game_w - self.size[0]) / 2
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

