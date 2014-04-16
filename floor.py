#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

piece = pygame.image.load('data/images/floor.png')

class Floor(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, large=100):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.mVel = -5
        self.p = large / 66 + 2
        self.large = self.p * 66
        self.image = pygame.surface.Surface((self.large, 16), 0)
        for i in range(self.p):
            self.image.blit(piece, (i * 66, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]

    def update(self):
        self.mPos[0] = self.mPos[0] + self.mVel
        if self.mPos[0] <= -65:
            self.mPos[0] = 0
        self.rect.x = self.mPos[0]

