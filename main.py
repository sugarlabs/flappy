#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import pygame.sprite as sprite
from floor import Floor
from pipe import Pipe
from build import Build

SKY = (113, 197, 207)
GAME_SIZE = (800, 700)
MIN_HEIGHT = 82 * 2 + 160
DIST = 160




class Flappy():

    def __init__(self):

        self.build_y = GAME_SIZE[1] - 229 - 50
        self.build = Build(0, self.build_y)
        self.background = pygame.surface.Surface(GAME_SIZE, 0)
        self.background.fill(SKY)
        self.floor_y = GAME_SIZE[1] - 50
        self.floor_x = 0
        self.floor = Floor(self.floor_x, self.floor_y, GAME_SIZE[0])
        self.l = self.floor.large - self.floor.dx
        self.floor_x1 = self.l
        ########################################################################
        self.pipe = Pipe(500, 500, 122)
        self.sprites = pygame.sprite.Group()
        ########################################################################
        self.sprites.add(self.pipe)
        self.sprites.add(self.floor)
        self.sprites.add(self.build)
        

    def main(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GAME_SIZE)
        self.screen.blit(self.background, (0, 0))
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.sprites.clear(self.screen, self.background)
            self.sprites.update()
            self.sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)


if __name__ == "__main__":
    g = Flappy()
    g.main()

