import pygame

class Settings:
    """A class to store all settings for Zombie Assault"""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.background = pygame.image.load("images/background.jpg")
        
        # Player settings
        self.player_speed = 2.0
        
        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)