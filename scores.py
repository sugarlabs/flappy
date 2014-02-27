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



class Message(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.image = mes
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]




