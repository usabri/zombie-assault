import sys
import pygame

from settings import Settings
from player import Player

class ZombieAssault:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Zombie Assault v0.1.0")

        self.player = Player(self)
                
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.player.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move the player to the right.
                    self.player.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move the player to the left.
                    self.player.moving_left = True
                elif event.key == pygame.K_UP:
                    # Move the player up.
                    self.player.moving_up = True
                elif event.key == pygame.K_DOWN:
                    # Move the player down.
                    self.player.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Stop moving the player to the right.
                    self.player.moving_right = False
                elif event.key == pygame.K_LEFT:
                    # Stop moving the player to the left.
                    self.player.moving_left = False
                elif event.key == pygame.K_UP:
                    # Stop moving the player up.
                    self.player.moving_up = False
                elif event.key == pygame.K_DOWN:
                    # Stop moving the player down.
                    self.player.moving_down = False

                
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.settings.background, (0, 0))
        self.player.blitme()
        
        pygame.display.flip()     
        
if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = ZombieAssault()
    ai.run_game()