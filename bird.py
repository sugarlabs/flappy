#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

bird1 = pygame.image.load('images/bird_h_alfa.png')


class Bird(pygame.sprite.Sprite):

    def __init__(self, parent, y=0):
        pygame.sprite.Sprite.__init__(self)

        self.parent = parent
        self.image = bird1
        self.mPos = [200, y]
        self.mVel = 0
        self.mAcc = 5
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]
        self.count = 0

    def setVel(self, vel):
        self.mVel = vel
        self.count = 20

    def update(self):
        self.count = self.count - 1
        if self.count < 0:
            self.count = 0
            self.mPos[1] = self.mPos[1] + self.mAcc
            self.rect.y = self.mPos[1]
        else:
            self.mPos[1] = self.mPos[1] - self.mVel

        self.rect.y = self.mPos[1]



