
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Pipe():

    def __init__(self, height):
        if height < 82:
            height = 82
        h = height - 42
        self.p = h / 40
        self.height = self.p * 40 + 42
        self.head = pygame.image.load('head_pipe.png')
        self.body = pygame.image.load('pipe.png')
        self.image = pygame.surface.Surface((91, self.height), 0)
        self.image.fill((255, 255, 255))
        self.image.set_colorkey((255, 255, 255))
        self.image.blit(self.head, (0, 0))
        for i in range(self.p):
            self.image.blit(self.body, (4, 42 + i * 40))
