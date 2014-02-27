#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import pygame.sprite as sprite
from floor import Floor
from pipe import Pipe

SKY = (113, 197, 207)
GAME_SIZE = (800, 700)
MIN_HEIGHT = 82 * 2 + 160





class Flappy():

    def __init__(self):
        self.build = pygame.image.load('buildings.png')
        self.build_y = GAME_SIZE[1] - self.build.get_height() - 50
        self.floor = Floor(GAME_SIZE[0])
        self.floor_y = GAME_SIZE[1] - 50
        self.floor_x = 0
        self.l = self.floor.large - self.floor.dx
        self.floor_x1 = self.l
        ########################################################################
        self.pipe = Pipe(122)

    def main(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GAME_SIZE)
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill(SKY)
            self.screen.blit(self.build, (0, self.build_y))
            self.screen.blit(self.pipe.image, (500, 200))

            self.screen.blit(self.floor.image, (self.floor_x, self.floor_y))
            self.screen.blit(self.floor.image, (self.floor_x1, self.floor_y))
            self.floor_x = self.floor_x - 5
            self.floor_x1 = self.floor_x1 - 5

            if self.floor_x < -self.l:
                self.floor_x = self.l
            if self.floor_x1 < -self.l:
                self.floor_x1 = self.l
            

            pygame.display.flip()
            self.clock.tick(30)


if __name__ == "__main__":
    g = Flappy()
    g.main()

