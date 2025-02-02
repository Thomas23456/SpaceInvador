import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (50,50,50)

        # Ship settings
        self.ship_speed = 2
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
