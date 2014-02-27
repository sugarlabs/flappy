#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys
import pygame.sprite as sprite
from floor import Floor
from pipe import Pipe_I
from pipe import Pipe_S
from build import Build
from bird import Bird

SKY = (113, 197, 207)
GAME_SIZE = (800, 700)
MIN_HEIGHT = 82 * 2 + 160
DIST = 160




class Flappy():

    def __init__(self):
        pass


    def load_all(self):
        self.sprites = pygame.sprite.LayeredUpdates()
        self.tubes = pygame.sprite.LayeredUpdates()
        self.background = pygame.surface.Surface(GAME_SIZE, 0)
        self.background.fill(SKY)
        self.screen.blit(self.background, (0, 0))
        self.build_y = GAME_SIZE[1] - 229 - 50
        self.floor_y = GAME_SIZE[1] - 50
        self.game_w = GAME_SIZE[0]
        self.game_h = GAME_SIZE[1]
        self.game_p = GAME_SIZE[0] - DIST - 91
        self.max_s = GAME_SIZE[1] - 82 - 160
        ########################################################################
        self.floor = Floor(0, self.floor_y, GAME_SIZE[0])
        self.floor.mVel = 0
        self.build = Build(0, self.build_y)
        self.bird = Bird(self, 300)
        self.bird.mAcc = 0
        ########################################################################
        self.sprites.add(self.build)
        self.sprites.add(self.floor)
        self.sprites.add(self.bird)

    def load_game(self):
        pipe1 = Pipe_I(self, self.game_w, 122)
        pipe2 = Pipe_S(self, self.game_w, GAME_SIZE[1] - 122 - 160)
        self.sprites.add(pipe1)
        self.sprites.add(pipe2)
        self.tubes.add(pipe1)
        self.tubes.add(pipe2)
        self.bird.mAcc = 5
        self.bird.count = 20
        self.floor.mVel = -5

    def main(self):
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(GAME_SIZE)
        pygame.display.set_caption('Flappy')
        
        self.load_all()
        self.big_running = True
        self.running_t = True
        self.running = False
        while self.big_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.big_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.running = True
                    self.load_game()
                elif event.type == pygame.KEYDOWN:
                    pass

            self.sprites.clear(self.screen, self.background)
            self.sprites.update()
            self.sprites.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)
            
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        self.big_running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.bird.setVel(8)
                    elif event.type == pygame.KEYDOWN:
                        pass

                self.sprites.clear(self.screen, self.background)
                self.sprites.update()
                self.sprites.draw(self.screen)

                col = pygame.sprite.spritecollide(self.bird, self.tubes, False)
                if not(col == []):
                    print 'Toco'
                    t = col[0]
                    self.running = False
                    self.bird.mAcc = 0
                    self.bird.count = -99
                    self.floor.mVel = 0
                    for spr in self.tubes:
                        spr.mVel = 0
                    self.running_t = True
                    while self.running_t:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                self.running = False
                                self.running_t = False
                                self.big_running = False
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                self.running_t = False
                                self.load_all()
                        #self.sprites.clear(self.screen, self.background)
                        #self.sprites.update()
                        #self.sprites.draw(self.screen)
                        pygame.display.flip()
                        self.clock.tick(30)

                pygame.display.flip()
                self.clock.tick(30)


if __name__ == "__main__":
    g = Flappy()
    g.main()

