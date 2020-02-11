# -*- Coding:utf8 -*-

from constants import *

from .classe_objet import *

import pygame

class Balle(Objet):
    def __init__(self, IMAGE, VITESSE_X, VITESSE_Y):
        Objet.__init__(self, IMAGE)
        self.rect.bottom = HAUTEUR - RAQUETTE_LARGEUR
        self.rect.left = HAUTEUR / 2
        self.VITESSE_X = VITESSE_X
        self.VITESSE_Y = VITESSE_Y
    
    def update(self):
        self.rect = self.rect.move(self.VITESSE_X, self.VITESSE_Y)

        if self.rect.x > LARGEUR - self.image.get_width() or self.rect.x < 0:
            self.VITESSE_X *= -1
            if self.rect.y < 0:
                self.VITESSE_Y *= -1
    
        if self.rect.y < self.image.get_height():
            self.VITESSE_Y *= -1
            if self.rect.y <= 0:
                self.VITESSE_X *= -1