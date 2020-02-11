# -*- Coding:utf8 -*-

from constants import *
from .classe_objet import *

import pygame

class Raquette(Objet):
    def __init__(self, IMAGE):
        Objet.__init__(self, IMAGE)
        self.rect.bottom = HAUTEUR
        self.division_raquette = 2
        self.rect.left = (LARGEUR - self.image.get_width()) / self.division_raquette

    def deplacerGauche(self):
        if self.rect.left > 0:
            self.rect.move_ip(-RAQUETTE_VITESSE, 0)

    def deplacerDroite(self):
        if self.rect.right < LARGEUR:
            self.rect.move_ip(RAQUETTE_VITESSE, 0)
