#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sugargame
import sugargame.canvas
from sugar.activity import activity

import main

class Activity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.max_participants = 1
        self.actividad = main.Flappy()
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self)
        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()
        self._pygamecanvas.run_pygame(self.actividad.main)

