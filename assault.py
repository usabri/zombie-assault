import sys

import pygame

class ZombieAssault:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Zombie Assault v0.1.0")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = ZombieAssault()
    ai.run_game()