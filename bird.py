#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

bird_h = pygame.image.load('data/images/bird_h_alfa.png')
bird_u = pygame.image.load('data/images/bird_u_alfa.png')
bird_d1 = pygame.image.load('data/images/bird_d45_alfa.png')
bird_d2 = pygame.image.load('data/images/bird_d55_alfa.png')


class Bird(pygame.sprite.Sprite):

    def __init__(self, parent, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.parent = parent
        self.mPos = [x, y]
        self.mVel = 0
        self.mAcc = 5   
        self.image = None
        self.setImage(bird_h)
        self.count = -99

    def setImage(self, img):
        if not(self.image == img):
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = self.mPos[0]
            self.rect.y = self.mPos[1]

    def setVel(self, vel):
        self.mVel = vel
        self.count = 20
        self.setImage(bird_u)

    def update(self):
        if not(self.count == -99):
            self.count = self.count - 1

            if self.count < 0:
                self.count = 0
                self.setImage(bird_d1)
                self.mPos[1] = self.mPos[1] + self.mAcc
            elif self.count < 10:
                self.setImage(bird_h)
                self.mPos[1] = self.mPos[1] + self.mAcc
            else:
                self.mPos[1] = self.mPos[1] - self.mVel

            if self.mPos[1] < 0:
                self.mPos[1] = 0

            self.rect.y = self.mPos[1]
        



