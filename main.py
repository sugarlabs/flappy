#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import pygame.sprite as sprite
from floor import Floor
from pipe import Pipe_I
from pipe import Pipe_S
from build import Build

SKY = (113, 197, 207)
GAME_SIZE = (800, 700)
MIN_HEIGHT = 82 * 2 + 160
DIST = 160




class Flappy():

    def __init__(self):
        self.sprites = pygame.sprite.LayeredUpdates()
        self.background = pygame.surface.Surface(GAME_SIZE, 0)
        self.background.fill(SKY)
        self.build_y = GAME_SIZE[1] - 229 - 50
        self.floor_y = GAME_SIZE[1] - 50
        self.game_w = GAME_SIZE[0]
        self.game_h = GAME_SIZE[1]
        self.game_p = GAME_SIZE[0] - DIST - 91
        self.max_s = GAME_SIZE[1] - 82 - 160
        ########################################################################
        pipe1 = Pipe_I(self, self.game_w, 122)
        pipe2 = Pipe_S(self, self.game_w, GAME_SIZE[1] - 122 - 160)
        self.floor = Floor(0, self.floor_y, GAME_SIZE[0])
        self.build = Build(0, self.build_y)
        
        ########################################################################
        self.sprites.add(self.build)
        self.sprites.add(self.floor)
        
        self.sprites.add(pipe1)
        self.sprites.add(pipe2)
        

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

