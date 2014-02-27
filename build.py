
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

build = pygame.image.load('buildings.png')


class Build(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)

        self.mPos = [x, y]
        self.image = pygame.surface.Surface((684, 229), 0)
        self.image.fill((255, 255, 255))
        
        self.image.blit(build, (0, 0))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]
 
    def setXY(self, aX, aY):
        self.mPos = [aX, aY]

    def setPosTuple(self, position):
        self.mPos = position

    def setVel(self, aVec):
        self.mVel = aVec
        
    def getX(self):
        return self.mPos[0]
    
    def getY(self):
        return self.mPos[1]
   
    def getSize(self):
        return (self.rect[2], self.rect[3])

    def destroy(self):
        self.image = None

