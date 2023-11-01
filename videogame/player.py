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

"""The player class and bullet class"""
import math
import rgbcolors
import pygame
import assets

class Player:
    """Player class"""
    def __init__(self, position):
        self._position = position
        self._radius = 40
        self._color = rgbcolors.orange
        self._velocity = pygame.math.Vector2(0, 0)
        surface = pygame.image.load(assets.get('spaceship'))
        self._image = surface.convert()
        self._num_lives = 3

    def update(self):
        """Updates player"""
        player_velocity = self._position.x + self._velocity.x
        if player_velocity > 0 and player_velocity < 800:
            self._position = self._position + self._velocity

    @property
    def position(self):
        """player's position"""
        return self._position

    def stop(self):
        """stops the player"""
        self._velocity = pygame.math.Vector2(0, 0)

    def move_left(self):
        """moves left"""
        self._velocity = pygame.math.Vector2(-10, 0)

    def move_right(self):
        """moves right"""
        self._velocity = pygame.math.Vector2(10, 0)

    def _move(self, velocity1):
        """moves player"""
        self._position = self._position + velocity1

    def draw(self, screen):
        """Draw the circle to screen."""
        #pygame.draw.circle(screen, self._color, self._position, self._radius)
        left = self._position.x - self._radius
        top = self._position.y - self._radius
        screen.blit(self._image, pygame.math.Vector2(left,top))


class Bullet:
    """Bullet"""
    def __init__(self, position, target_position, speed):
        """Bullet Class"""
        self._position = pygame.math.Vector2(position)
        self._target_position = pygame.math.Vector2(target_position)
        self._speed = speed
        self._color = rgbcolors.mult_color(self._speed, rgbcolors.red)
        self._radius = 10
        #print(f"The position of the bullet is {self._position}")

    @property
    def rect(self):
        """return rect"""
        left = self._position.x - self._radius
        top = self._position.y - self._radius
        width = 2 * self._radius
        return pygame.Rect(left, top, width, width)

    def should_die(self):
        """Tell bullet to die"""
        squared_distance = (self._position - self._target_position).length_squared()
        return math.isclose(squared_distance, 0.0, rel_tol=1e-01)

    def update(self, delta_time):
        """Updaytes bullet"""
        self._position.move_towards_ip(self._target_position, self._speed * delta_time)

    def draw(self, screen):
        """Draw the circle to screen."""
        pygame.draw.circle(screen, self._color, self._position, self._radius)
    