#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sugargame
import sugargame.canvas
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton, StopButton
from sugar3.graphics.radiotoolbutton import RadioToolButton
from sugar3.graphics.toolbutton import ToolButton
from gettext import gettext as _
import main
import pygame


class Activity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.max_participants = 1
        self.sound = True
        self.game = main.Flappy()
        self.build_toolbar()
        self.game.canvas = sugargame.canvas.PygameCanvas(self, main=self.game.run, modules=[pygame.display, pygame.font, pygame.mixer])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()

    def build_toolbar(self):
        toolbar_box = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)

        separator = Gtk.SeparatorToolItem(draw=False, expand=False)
        toolbar_box.toolbar.insert(separator, -1)

        self._levels_buttons = []

        def add_level_button(icon_name, tooltip, numeric_level):
            button = RadioToolButton(icon_name=icon_name, group=self._levels_buttons[0] if self._levels_buttons else None)
            self._levels_buttons.append(button)

            def callback(source):
                if source.get_active():
                    self.game.set_level(numeric_level)
                    self.game.run()

            button.connect('clicked', callback)
            button.set_tooltip(tooltip)

        add_level_button('male-7', _("Hard"), 3)
        add_level_button('male-4', _("Medium"), 2)
        add_level_button('male-1', _("Easy"), 1)

        for button in reversed(self._levels_buttons):
            toolbar_box.toolbar.insert(button, -1)

        separator2 = Gtk.SeparatorToolItem(draw=True, expand=False)
        toolbar_box.toolbar.insert(separator2, -1)

        sound_button = ToolButton('speaker-muted-100')
        sound_button.set_tooltip(_('Sound'))
        sound_button.connect('clicked', self.sound_control)
        toolbar_box.toolbar.insert(sound_button, -1)

        separator3 = Gtk.SeparatorToolItem(draw=False, expand=True)
        toolbar_box.toolbar.insert(separator3, -1)

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show_all()

    def sound_control(self, button):
        self.sound = not self.sound
        self.game.sound = self.sound
        if not self.sound:
            button.set_icon_name('speaker-muted-000')
            button.set_tooltip(_('No sound'))
        else:
            button.set_icon_name('speaker-muted-100')
            button.set_tooltip(_('Sound'))


if __name__ == "__main__":
    Gtk.init([])
    activity = Activity(None)
    activity.show_all()
    Gtk.main()
