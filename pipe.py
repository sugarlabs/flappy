#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

head = pygame.image.load('images/head_pipe.png')
body = pygame.image.load('images/pipe.png')


class Pipe_I(pygame.sprite.Sprite):

    def __init__(self, parent, x=0, height=82):
        pygame.sprite.Sprite.__init__(self)
        self.flag = True
        self.points = True
        self.parent = parent
        self.mPos = [x, 500]
        self.mVel = -5
        if height < 82:
            height = 82
        h = height - 42
        self.p = h / 40
        self.height = self.p * 40 + 42
        self.mPos[1] = self.parent.floor_y - self.height
        self.image = pygame.surface.Surface((91, self.height), 0)
        self.image.fill((255, 255, 255))
        
        self.image.blit(head, (0, 0))
        for i in range(self.p):
            self.image.blit(body, (4, 42 + i * 40))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]

    def update(self):
        self.mPos[0] = self.mPos[0] + self.mVel
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]

        if self.mPos[0] < -91:
            self.parent.sprites.remove(self)
            self.parent.tubes.remove(self)

        elif self.mPos[0] < (self.parent.bird_x - self.parent.pipe_w):
            if self.points:
                self.points = False
                self.parent.score = self.parent.score + 1
                print self.parent.score
            
        elif self.mPos[0] < (self.parent.game_p):
            if self.flag:
                self.flag = False
                h = random.randrange(82, self.parent.max_s)
     
                p = Pipe_I(self.parent, self.parent.game_w, h)
                self.parent.sprites.add(p)
                self.parent.tubes.add(p)
                s = p.mPos[1] + p.height + 160
                s = self.parent.game_h - p.height - 160 - 50
                p = Pipe_S(self.parent, self.parent.game_w, s)
                self.parent.sprites.add(p)
                self.parent.tubes.add(p)



class Pipe_S(pygame.sprite.Sprite):

    def __init__(self, parent, x=0, height=82):
        pygame.sprite.Sprite.__init__(self)
        self.flag = True
        self.parent = parent
        self.mPos = [x, 0]
        self.mVel = -5
        if height < 82:
            height = 82
        h = height - 42
        self.p = h / 40
        self.height = self.p * 40 + 42
        #self.mPos[1] = self.parent.game_h - self.height
        self.image = pygame.surface.Surface((91, self.height), 0)
        self.image.fill((255, 255, 255))

        for i in range(self.p):
            self.image.blit(body, (4, i * 40))
        self.image.blit(head, (0, self.p * 40))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]

    def update(self):
        self.mPos[0] = self.mPos[0] + self.mVel
        self.rect.x = self.mPos[0]

        if self.mPos[0] < -91:
            self.parent.sprites.remove(self)
            self.parent.tubes.remove(self)

