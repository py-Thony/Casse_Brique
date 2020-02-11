# -*- Coding:utf8 -*-


import pygame

class Objet(pygame.sprite.Sprite):
    """
    classe qui définit la nauture d'un sprite
    """
    
    def __init__(self, IMAGE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(IMAGE).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
