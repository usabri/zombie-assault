import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired by the player."""

    def __init__(self, ai_game):
        """Create a bullet object at the player's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                 self.settings.bullet_height)
        self.rect.midtop = ai_game.player.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

        # Store the bullet's direction.
        self.direction = ai_game.player.direction

    def update(self):
        """Move the bullet in the direction the player is facing."""
        if self.direction == "up_left":
            self.x -= self.settings.bullet_speed
            self.y -= self.settings.bullet_speed
        elif self.direction == "up_right":
            self.x += self.settings.bullet_speed
            self.y -= self.settings.bullet_speed
        elif self.direction == "down_left":
            self.x -= self.settings.bullet_speed
            self.y += self.settings.bullet_speed
        elif self.direction == "down_right":
            self.x += self.settings.bullet_speed
            self.y += self.settings.bullet_speed
        elif self.direction == "up":
            self.y -= self.settings.bullet_speed
        elif self.direction == "down":
            self.y += self.settings.bullet_speed
        elif self.direction == "left":
            self.rect.x -= self.settings.bullet_speed
        elif self.direction == "right":
            self.rect.x += self.settings.bullet_speed

        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
