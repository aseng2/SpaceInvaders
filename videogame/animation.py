# Anthony Seng
# CPSC 386-05
# 2023-04-20
# aseng6825@csu.fullerton.edu
# @aseng2
#
# Lab 05-00
#
# player.py
#

"""Explosion class"""

import os.path
import pygame

class Explosion(pygame.sprite.Sprite):
    """The Explision class"""

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, 'data')
    image_path = os.path.join(data_dir, 'explosion1.gif')

    defaultlife = 12
    animcycle = 3
    images = []

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        try:
            surface = pygame.image.load(Explosion.image_path)
        except pygame.error as pygame_error:
            raise SystemExit(
                f'Could not load image "{Explosion.image_path}" {pygame.get_error()}'
            ) from pygame_error
        img = surface.convert()
        if not Explosion.images:
            Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = Explosion.defaultlife
        self._actor = actor

    def update(self):
        """Updates the explosion"""
        self.life = self.life - 1
        self.image = self.images[self.life // Explosion.animcycle % 2]
        if self.life <= 0:
            self.kill()
            self._actor.is_exploding = False
