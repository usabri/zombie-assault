import sys
import pygame

from settings import Settings
from player import Player
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()
                
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.player.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """ Respond to keypresses."""
        if event.key == pygame.K_UP and event.key == pygame.K_RIGHT:
            self.player.moving_up_right = True
        elif event.key == pygame.K_UP and event.key == pygame.K_LEFT:
            self.player.moving_up_left = True
        elif event.key == pygame.K_DOWN and event.key == pygame.K_RIGHT:
            self.player.moving_down_right = True
        elif event.key == pygame.K_DOWN and event.key == pygame.K_LEFT:
            self.player.moving_down_left = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
            self.player.image = self.player.player_images["right"]
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
            self.player.image = self.player.player_images["left"]
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
            self.player.image = self.player.player_images["up"]
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False
            self.player.image = self.player.player_images["down"]

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.settings.background, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.player.blitme()
        
        pygame.display.flip()     
        
if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = ZombieAssault()
    ai.run_game()
