#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Floor():

    def __init__(self, large):
        self.p = large / 66
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


