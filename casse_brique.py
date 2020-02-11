# -*- Coding:utf8 -*-

from constants import *
from classes.classe_balle import *
from classes.classe_raquette import *
from classes.classe_brique import *


import pygame
import random
import sys

pygame.init()

continue_game = True
loose_scene = False
score = 0
sauv_score = 0

while continue_game:
    score = sauv_score
    loop_game = True

    FENETRE = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.key.set_repeat(40, 30)
    pygame.display.set_caption(" Jeu de Casse Brique ")
    clock = pygame.time.Clock()


    VIES = 1

    LISTE_GLOBALE_SPRITES = pygame.sprite.Group()
    LISTE_RAQUETTE_BRIQUES = pygame.sprite.Group()
    LISTE_BRIQUES = pygame.sprite.Group()

    balle = Balle("images/balle.png", BALLE_VITESSE, -BALLE_VITESSE)
    LISTE_GLOBALE_SPRITES.add(balle)

    raquette = Raquette("images/raquette.png")
    LISTE_GLOBALE_SPRITES.add(raquette)
    LISTE_RAQUETTE_BRIQUES.add(raquette)


    while loose_scene == True:
        liste_image_loose = ["images/loose5.png", "images/loose4.png", \
            "images/loose3.png", "images/loose2.png", "images/loose1.png", \
            "images/loose0.png"]
        restart0 = pygame.image.load("images/restart0.png")
        restart1 = pygame.image.load("images/restart1.png")

        i = 0
        iii = 300
        while i < len(liste_image_loose):
            
            image_loose = pygame.image.load(liste_image_loose[i]).convert()
            FENETRE.blit(image_loose, (0,0))
            pygame.display.flip()
            pygame.time.wait(1000)
            i += 1

        if i == len(liste_image_loose):
            replay_screen = pygame.image.load("images/replay.png").convert()
            FENETRE.blit(replay_screen, (0, 0))
            pygame.display.flip()

            pygame.event.wait()
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_y or pygame.K_Y]:
                ii = 20
                while ii > 0:
                    FENETRE.blit(restart0, (0, 0))
                    pygame.time.wait(iii)
                    iii -= 15
                    pygame.display.flip()
                    FENETRE.blit(restart1, (0, 0))
                    pygame.time.wait(iii)
                    iii -= 35
                    ii -= 1
                    pygame.display.flip()
                    replay = False
            elif key_pressed[pygame.K_n or pygame.K_N]:
                pygame.quit()
                sys.exit()
        loose_scene = False
        pygame.display.update()
    for i in range(8):
        for j in range(8):
            brique = Brique("images/brique.png", (i+1) * BRIQUE_LARGEUR + 5, (j+1) * BRIQUE_HAUTEUR + 5)
            LISTE_GLOBALE_SPRITES.add(brique)
            LISTE_RAQUETTE_BRIQUES.add(brique)
            LISTE_BRIQUES.add(brique)

    while loop_game == True:
        if balle.rect.y > HAUTEUR:
            print(" Dommage! Il vous reste ", VIES, "vies")
            VIES -= 1
            balle = Balle("images/balle.png", BALLE_VITESSE, -BALLE_VITESSE)
            LISTE_GLOBALE_SPRITES.add(balle)
            if VIES <= 0:
                loose_scene = True
                loop_game = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    raquette.deplacerGauche()
                elif event.key == pygame.K_RIGHT:
                    raquette.deplacerDroite()
        

        REBONDS = pygame.sprite.spritecollide(balle, LISTE_RAQUETTE_BRIQUES, False)
        if REBONDS:
            RECT = REBONDS[0].rect
            if RECT.left > balle.rect.left or balle.rect.right < RECT.right:
                balle.VITESSE_Y *= -1
            if balle.rect.top > RECT.top:
                balle.VITESSE_Y

            if pygame.sprite.spritecollide(balle, LISTE_BRIQUES, True):
                score += len(REBONDS)
                print("%s points" % score)

            if len(LISTE_BRIQUES) == 0:
                print("Gagné! Bravo!")
                loop_game = False
                sauv_score = score
            
        LISTE_GLOBALE_SPRITES.update()
        clock.tick(60)
        FENETRE.fill((0, 0, 0))
        LISTE_GLOBALE_SPRITES.draw(FENETRE)
        pygame.display.flip()