#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import math

SKY = (113, 197, 207)
GROUND = (221, 216, 148)

build = pygame.image.load('data/images/buildings.png')


def make_back(parent):
    w = parent.game_w
    h = parent.game_h
    floor_y = parent.floor_y
    back = pygame.surface.Surface((w, h), 0)
    back.fill(SKY)
    rect = pygame.rect.Rect(0, floor_y, w, h - floor_y)
    back.fill(GROUND, rect)
    if w > 684:
        t = int(math.ceil(w / 684.0))
    else:
        t = 1
    y = floor_y - 229
    for i in range(t):
        back.blit(build, (684 * i, y))
    return back

