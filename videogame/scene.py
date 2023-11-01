# Anthony Seng
# CPSC 386-05
# 2023-04-20
# aseng6825@csu.fullerton.edu
# @aseng2
#
# Lab 05-00
#
# scene.py
#

"""Scene objects for making games with PyGame."""

import os
import random
import pickle
import pygame
import assets
import player
import rgbcolors
from animation import Explosion


# If you're interested in using abstract base classes, feel free to rewrite
# these classes.
# For more information about Python Abstract Base classes, see
# https://docs.python.org/3.8/library/abc.html


class Scene:
    """Base class for making PyGame Scenes."""

    def __init__(self, screen, background_color, soundtrack=None):
        """Scene initializer"""
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(background_color)
        self._frame_rate = 60
        self._is_valid = True
        self._soundtrack = soundtrack
        self._render_updates = None

    def draw(self):
        """Draw the scene."""
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        """Process a game event by the scene."""
        # This should be commented out or removed since it generates a lot of noise.
        # print(str(event))
        if event.type == pygame.QUIT:
            print("Good Bye!")
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            print("Bye bye!")
            self._is_valid = False

    def is_valid(self):
        """Is the scene valid? A valid scene can be used to play a scene."""
        return self._is_valid

    def render_updates(self):
        """Render all sprite updates."""

    def update_scene(self):
        """Update the scene state."""

    def start_scene(self):
        """Start the scene."""
        if self._soundtrack:
            try:
                pygame.mixer.music.load(self._soundtrack)
                pygame.mixer.music.set_volume(0.2)
            except pygame.error as pygame_error:
                print("Cannot open the mixer?")
                print('\n'.join(pygame_error.args))
                raise SystemExit("broken!!") from pygame_error
            pygame.mixer.music.play(-1)

    def end_scene(self):
        """End the scene."""
        if self._soundtrack and pygame.mixer.music.get_busy():
            # Fade music out so there isn't an audible pop
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()

    def frame_rate(self):
        """Return the frame rate the scene desires."""
        return self._frame_rate


class PressAnyKeyToExitScene(Scene):
    """Empty scene where it will invalidate when a key is pressed."""

    def process_event(self, event):
        """Process game events."""
        # TODO: Have the super/parent class process the event first before
        # processing the event yourself.
        super().process_event(event)
        # TOOD: If the event type is a keydown event, set self._is_valid to False.
        if event.type == pygame.KEYDOWN:
            self._is_valid = False


class PolygonTitleScene(PressAnyKeyToExitScene):
    """Scene with a title string and a polygon."""

    def __init__(
        self,
        screen,
        title,
        title_color=rgbcolors.ghostwhite,
        title_size=72,
        background_color=rgbcolors.papaya_whip,
        soundtrack=None,
    ):
        """Initialize the scene."""
        # TODO: Have the super/parent class initialized
        super().__init__(screen, background_color, soundtrack)
        # TODO: Ask pygame for the default font at title_size size. Use the font to render the string title and assign this to an instance variable named self._title in the color title_color.
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, title_color)
        # TODO: Ask pygame for the default font at 18 point size. Use the font to render the string 'Press any key.' in the color black. Assign the rendered text to an instance variable named self._press_any_key.
        press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._press_any_key = press_any_key_font.render("Press an key.", True, rgbcolors.black)

    def draw(self):
        """Draw the scene."""
        # TODO: Have the super/parent class draw first before
        # drawing yourself.
        super().draw()
        # TODO: Draw a 100 pixel by 100 pixel rectangle that has it's center located 100 pixels below the center of the window.
        pygame.draw.rect(self._screen, rgbcolors.yellow, (350 , 450, 100, 100))
        # TODO: Blit the title text to the center of the window.
        self._screen.blit(self._title, (300, 350))
        # TODO: Blit the press any key message to the bottom of the window. The text should be centered horizontally and be 50 pixels above the bottom edge of the window.
        self._screen.blit(self._press_any_key, (350, 750))

class Enemy:
    """Class representing the enemy"""

    def __init__(self, center_x, center_y, radius, color, name = "None"):
        self._center_x = center_x
        self._center_y = center_y
        self._radius = radius
        self._color = color
        self._name = name
        self._is_exploding = False
        surface = pygame.image.load(assets.get('alien'))
        self._image = surface.convert()
        self._enemy_position = pygame.Vector2(center_x, center_y)
        #self._target_position1 = pygame.math.Vector2(width //2, height - 100)

    @property
    def radius(self):
        """return radius"""
        return self._radius

    @property
    def center(self):
        """return center"""
        return pygame.Vector2(self._center_x, self._center_y)

    @property
    def rect(self):
        """return a rect"""
        left = self._center_x - self._radius
        top = self._center_y - self._radius
        width = 2 * self._radius
        return pygame.Rect(left, top, width, width)

    @property
    def width(self):
        """return width"""
        return 2 * self._radius

    @property
    def height(self):
        """return height"""
        return 2 * self._radius

    @property
    def is_exploding(self):
        """return if it is exploding"""
        return self._is_exploding

    @is_exploding.setter
    def is_exploding(self, val):
        """is the exploding setter"""
        self._is_exploding = val

    def draw(self, screen, delta_time):
        #pygame.draw.circle(screen, self._color, self.center, self.radius)
        self._center_y += (delta_time * 0.01)
        left = self._center_x - self._radius
        top = self._center_y - self._radius
        screen.blit(self._image, pygame.Vector2(left, top))
        #screen.blit(self._image, self._enemy_position))


    #def update(self, position, delta_time):
        #center1 = center()
        #self._enemy_position.move_towards_ip(position, 0.01 * delta_time)


class VideoGameScene(PressAnyKeyToExitScene):
    def __init__(self, screen):
        """VideoGame scene"""
        super().__init__(screen, rgbcolors.black, assets.get('soundtrack'))
        self._explosion_sound = pygame.mixer.Sound(assets.get('soundfx'))
        self._enemies = None
        self.delta_time = 0
        self._bullets = []
        (width, height) = self._screen.get_size()
        self._player = player.Player(pygame.math.Vector2(width //2, height - 100))
        self.make_enemies()
        self._render_updates = pygame.sprite.RenderUpdates()
        Explosion.containers = self._render_updates
        self._score_value = 0

    def make_enemies(self):
        circle_width = 100
        circle_radius = circle_width // 2
        gutter_width = circle_width // 2
        (width, height) = self._screen.get_size()
        x_step = gutter_width + circle_width
        y_step = gutter_width + circle_width
        enemies_per_row = (width // x_step) - 1
        num_rows = 4
        print(
            f"There will be {num_rows} rows and {enemies_per_row} enemies in each row."
        )
        self._enemies = [
            Enemy(
                x_step + (j * x_step),
                y_step + (i * y_step),
                circle_radius,
                rgbcolors.ghost_white,
                f"{i+1}, {j+1}",
            )
            for i in range(num_rows)
            for j in range(enemies_per_row)
        ]

    def update_scene(self):
        super().update_scene()
        self._player.update()
        (width, height) = self._screen.get_size()
        #print(f"The delta time {self.delta_time}")
        for bullet in self._bullets:
            bullet.update(self.delta_time)
            if bullet.should_die():
                self._bullets.remove(bullet)
            else:
                index = bullet.rect.collidelist([c.rect for c in self._enemies])
                if index > -1:
                    Explosion(self._enemies[index])
                    self._enemies[index].is_exploding = True
                    self._enemies.remove(self._enemies[index])
                    self._explosion_sound.play()
                    self._bullets.remove(bullet)
                    self._score_value += 100
                    print(f"{self._score_value}")
                    print(len(self._enemies))


    def process_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            (width, height) = self._screen.get_size()

            bullet_target = self._player.position - pygame.math.Vector2(0, height)
            velocity = random.uniform(0.1, 1.0)
            self._bullets.append(player.Bullet(self._player.position, bullet_target, velocity))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self._player.move_left()
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            self._player.stop()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self._player.move_right()
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            self._player.stop()
        else:
            super().process_event(event)

    def render_updates(self):
        super().render_updates()
        self._render_updates.clear(self._screen, self._background)
        self._render_updates.update()
        dirty = self._render_updates.draw(self._screen)

    #def score(self):
        #score_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        #self._score = score_font.render("Score : " + str(self._score_value), True, rgbcolors.ghostwhite)
        #self._screen.blit(self._score, (300, 350))

    def draw(self):
        super().draw()
        score_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._score = score_font.render("Score : " + str(self._score_value), True, rgbcolors.ghostwhite)
        self._screen.blit(self._score, (10, 10))

        main_dir = os.path.split(os.path.abspath(__file__))[0]
        data_dir = os.path.join(main_dir, "data")
        pickle_file = os.path.join(data_dir, "scores.pk1")

        you_win_font = pygame.font.Font(pygame.font.get_default_font(), 72)
        self._you_win = you_win_font.render("You win", True, rgbcolors.yellow)

        you_lose_font = pygame.font.Font(pygame.font.get_default_font(), 72)
        self._you_lose = you_lose_font.render("You lose", True, rgbcolors.red1)

        press_up_save_font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self._save_data = press_up_save_font.render("Press up to save", True, rgbcolors.pink1)

        you_lose_game = False
        if len(self._enemies) == 0:
            self._screen.blit(self._you_win, (250, 350))
            self._screen.blit(self._save_data, (325, 425))
            if not os.path.exists(data_dir):
                os.mkdir(data_dir)
            with open(pickle_file, "wb") as fh:
                pickle.dump(self._score_value, fh, pickle.HIGHEST_PROTOCOL)

        for enemy1 in self._enemies:
            if not enemy1.is_exploding:
                enemy1.draw(self._screen, self.delta_time)

        for enemy2 in self._enemies:
            #print(f"{int(enemy2._center_y)}")
            if int(enemy2._center_y) >= 700:
                you_lose_game = True
        if you_lose_game:
            self._screen.blit(self._you_lose, (250, 350))
            self._screen.blit(self._save_data, (325, 425))
            if not os.path.exists(data_dir):
                os.mkdir(data_dir)
            with open(pickle_file, "wb") as fh:
                pickle.dump(self._score_value, fh, pickle.HIGHEST_PROTOCOL)

        for bullet in self._bullets:
            bullet.draw(self._screen)
        self._player.draw(self._screen)
