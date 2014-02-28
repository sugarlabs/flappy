#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Flappy
# Copyright (C) 2014 Alan Aguiar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Alan Aguiar alanjas@hotmail.com

import pygame
import sys
import pygame.sprite as sprite
from floor import Floor
from pipe import Pipe_I
from pipe import Pipe_S
from build import Build
from bird import Bird
from scores import Scores
from scores import Message
from scores import CurrentScore

SKY = (113, 197, 207)
GAME_SIZE = (684, 600)
MIN_HEIGHT = 82 * 2 + 160
DIST = 160



class Flappy():

    def __init__(self):
        self.best = 0
        self.bird_x = 200
        self.bird_y = 300
        self.pipe_w = 91
        self.build_y = GAME_SIZE[1] - 229 - 50
        self.floor_y = GAME_SIZE[1] - 50
        self.game_w = GAME_SIZE[0]
        self.game_h = GAME_SIZE[1]
        self.game_p = GAME_SIZE[0] - DIST - 91
        self.max_s = GAME_SIZE[1] - 82 - 160

    def increment_score(self):
        self.score = self.score + 1
        self.currentS.set_score(self.score)

    def load_all(self):
        self.score = 0
        self.sprites = pygame.sprite.LayeredUpdates()
        self.tubes = pygame.sprite.LayeredUpdates()
        self.background = pygame.surface.Surface(GAME_SIZE, 0)
        self.background.fill(SKY)
        self.screen.blit(self.background, (0, 0))

        ########################################################################
        self.floor = Floor(0, self.floor_y, GAME_SIZE[0])
        self.floor.mVel = 0
        self.build = Build(0, self.build_y)
        self.bird = Bird(self, self.bird_x, self.bird_y)
        self.bird.mAcc = 0
        self.scores = Scores(200, 200)
        self.message = Message(200, 200)
        self.currentS = CurrentScore(300, 100)
        ########################################################################
        self.sprites.add(self.build, layer=0)
        self.sprites.add(self.floor, layer=0)
        self.sprites.add(self.bird, layer=2)
        self.sprites.add(self.message, layer=3)
        

    def load_game(self):
        pipe1 = Pipe_I(self, self.game_w, 122)
        pipe2 = Pipe_S(self, self.game_w, GAME_SIZE[1] - 122 - 160)
        self.sprites.add(pipe1, layer=1)
        self.sprites.add(pipe2, layer=1)
        self.tubes.add(pipe1)
        self.tubes.add(pipe2)
        self.tubes.add(self.floor)
        self.sprites.add(self.currentS, layer=3)
        self.bird.mAcc = 5
        self.bird.count = 20
        self.floor.mVel = -5
        self.sprites.remove(self.scores)
        self.sprites.remove(self.message)

    def main(self):
        pygame.display.init()
        pygame.font.init()
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

                    t = col[0]
                    self.running = False
                    self.bird.mAcc = 0
                    self.bird.count = -99
                    self.floor.mVel = 0
                    for spr in self.tubes:
                        spr.mVel = 0
                    self.sprites.add(self.scores, layer=3)
                    self.sprites.draw(self.screen)
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

