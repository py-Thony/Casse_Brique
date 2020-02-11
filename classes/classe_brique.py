# -*- Coding:utf8 -*-

from constants import *

from .classe_objet import*

import pygame


class Brique(Objet):
    def __init__(self, IMAGE, x, y):
        Objet.__init__(self, IMAGE)
        self.rect.x, self.rect.y = x, y
