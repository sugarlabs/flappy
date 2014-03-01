
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math

build = pygame.image.load('images/buildings.png')


class Build(pygame.sprite.Sprite):

    def __init__(self, parent, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.parent = parent
        self.mPos = [x, y]
        if self.parent.game_w > 684:
            t = math.ceil(self.parent.game_w / 684.0)
            t = int(t)
        else:
            t = 1
        self.image = pygame.surface.Surface((684 * t, 229), 0)
        self.image.fill((255, 255, 255))
        for i in range(t):
            self.image.blit(build, (684 * i, 0))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = self.mPos[0]
        self.rect.y = self.mPos[1]
 

