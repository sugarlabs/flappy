#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Floor(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0, large=100):
        pygame.sprite.Sprite.__init__(self)
        self.mPos = [x, y]
        self.mVel = -5
        self.p = large / 66 + 1
        self.large = self.p * 66
        if (self.large % 5) == 0:
            self.dx = 5
        else:
            l = self.large / 5
            l = l + 1
            self.dx = l * 5 - self.large
        self.image = pygame.surface.Surface((self.large, 16), 0)
        self.piece = pygame.image.load('floor.png')
        for i in range(self.p):
            self.image.blit(self.piece, (i * 66, 0))
        self.rect = self.image.get_rect()

    def setXY(self, aX, aY):
        self.mPos = [aX, aY]

    def setPosTuple(self, position):
        self.mPos = position

    def setVel(self, aVec):
        self.mVel = aVec

    def update(self):
        self.mPos[0] = self.mPos[0] + self.mVel
        if self.mPos[0] < -66:
            self.mPos[0] = 0
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]
        
    def getX(self):
        return self.mPos[0]
    
    def getY(self):
        return self.mPos[1]
   
    def getSize(self):
        return (self.rect[2], self.rect[3])

    def destroy(self):
        self.image = None

