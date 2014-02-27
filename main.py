#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import pygame.sprite as sprite

SKY = (113, 197, 207)
GAME_SIZE = (800, 700)
MIN_HEIGHT = 82 * 2 + 160

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

