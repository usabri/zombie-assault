import pygame

class Settings:
    """A class to store all settings for Zombie Assault"""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.background = pygame.image.load("images/background.jpg")