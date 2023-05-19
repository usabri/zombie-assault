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
        
        # Load the player image and get its rect.
        self.image = self.player_images["down"]
        self.rect = self.image.get_rect()
        
        # Start the player in the center of the screen.
        self.rect.center = self.screen_rect.center
        
        # Start with the player idle.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update the player's image based on the direction."""
        if self.moving_right:
            if self.moving_up:
                self.image = self.player_images["up_right"]
            elif self.moving_down:
                self.image = self.player_images["down_right"]
            else:
                self.image = self.player_images["right"]
            self.rect.x += 1
        if self.moving_left:
            if self.moving_up:
                self.image = self.player_images["up_left"]
            elif self.moving_down:
                self.image = self.player_images["down_left"]
            else:
                self.image = self.player_images["left"]
            self.rect.x -= 1
        if self.moving_up:
            if not self.moving_left and not self.moving_right:
                self.image = self.player_images["up"]
            self.rect.y -= 1
        if self.moving_down:
            if not self.moving_left and not self.moving_right:
                self.image = self.player_images["down"]
            self.rect.y += 1

               
    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)