import pygame

class Player:
    """A class to manage the player."""
    
    def __init__(self, ai_game):
        """Initialize the player and set the starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the player image and get its rect.
        self.player_images = {
            "down": pygame.image.load("images/PlayerDown.png"),
            "down_left": pygame.image.load("images/PlayerDownLeft.png"),
            "down_right": pygame.image.load("images/PlayerDownRight.png"),
            "left": pygame.image.load("images/PlayerLeft.png"),
            "right": pygame.image.load("images/PlayerRight.png"),
            "up": pygame.image.load("images/PlayerUp.png"),
            "up_left": pygame.image.load("images/PlayerUpLeft.png"),
            "up_right": pygame.image.load("images/PlayerUpRight.png"),
        }
        
        self.image = self.player_images["down"] # Set the initial image.
        self.rect = self.image.get_rect()
        
        # Start the player in the center of the screen.
        self.rect.center = self.screen_rect.center
        
    def update(self, direction):
        """Update the player's image based on the direction."""
        self.image = self.player_images[direction]
        
    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)