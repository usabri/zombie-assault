import pygame

class Player:
    """A class to manage the player."""

    def __init__(self, ai_game):
        """Initialize the player and set the starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the player images and get their rects.
        self.player_images = {
            "down": pygame.image.load("images/PlayerDown.png"),
             "left": pygame.image.load("images/PlayerLeft.png"),
            "right": pygame.image.load("images/PlayerRight.png"),
            "up": pygame.image.load("images/PlayerUp.png"),
            "down_left": pygame.image.load("images/PlayerDownLeft.png"),
            "down_right": pygame.image.load("images/PlayerDownRight.png"),
            "up_left": pygame.image.load("images/PlayerUpLeft.png"),
            "up_right": pygame.image.load("images/PlayerUpRight.png"),
        }

        self.WALK_DOWN_IMAGES = [
            pygame.image.load(f"images/WalkDown{i}.png") for i in range(1, 9)
        ]
        self.WALK_LEFT_IMAGES = [
            pygame.image.load(f"images/WalkLeft{i}.png") for i in range(1, 9)
        ]
        self.WALK_RIGHT_IMAGES = [
            pygame.image.load(f"images/WalkRight{i}.png") for i in range(1, 9)
        ]
        self.WALK_UP_IMAGES = [
            pygame.image.load(f"images/WalkUp{i}.png") for i in range(1, 9)
        ]
        self.WALK_DOWN_LEFT_IMAGES = [
            pygame.image.load(f"images/WalkDownLeft{i}.png") for i in range (1, 9)
        ]
        self.WALK_DOWN_RIGHT_IMAGES = [
            pygame.image.load(f"images/WalkDownRight{i}.png") for i in range (1, 9)
        ]
        self.WALK_UP_LEFT_IMAGES = [
            pygame.image.load(f"images/WalkUpLeft{i}.png") for i in range (1, 9)
        ]
        self.WALK_UP_RIGHT_IMAGES = [
            pygame.image.load(f"images/WalkUpRight{i}.png") for i in range (1, 9)
        ]       

        # Animation delay
        self.FRAME_DELAY = 4
        
        # Start the player facing down in the center of the screen
        self.image = self.player_images["down"]
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        
        # Store a float for the player's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Store the current direction the player is facing.
        self.direction = "down"

        # Animation variables
        self.walk_down_frame_index = 0
        self.walk_left_frame_index = 0
        self.walk_right_frame_index = 0
        self.walk_up_frame_index = 0
        self.walk_down_left_frame_index = 0
        self.walk_down_right_frame_index = 0
        self.walk_up_left_frame_index = 0
        self.walk_up_right_frame_index = 0

        # Start with the player idle.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_down_left = False
        self.moving_down_right = False
        self.moving_up_left = False
        self.moving_up_right = False

        # Animation delay
        self.last_frame_change_time = pygame.time.get_ticks()

    def update(self):
        """Update the player's image based on the direction facing
        and update player x and y values."""
        if self.moving_down_left:
            self.image = self.player_images["down_left"]
            self.x -= self.settings.player_speed
            self.y += self.settings.player_speed
            self.direction = "down_left"
            self.walk_down_left_frame_index = self.animate_walk(
                self.WALK_DOWN_LEFT_IMAGES, self.walk_down_left_frame_index)
        if self.moving_down_right:
            self.image = self.player_images["down_right"]
            self.x += self.settings.player_speed
            self.y += self.settings.player_speed
            self.direction = "down_right"
            self.walk_down_right_frame_index = self.animate_walk(
                self.WALK_DOWN_RIGHT_IMAGES, self.walk_down_right_frame_index)
        if self.moving_up_left:
            self.image = self.player_images["up_left"]
            self.x -= self.settings.player_speed
            self.y -= self.settings.player_speed
            self.direction = "up_left"
            self.walk_up_left_frame_index = self.animate_walk(
                self.WALK_UP_LEFT_IMAGES, self.walk_up_left_frame_index)
        if self.moving_up_right:
            self.image = self.player_images["up_right"]
            self.x += self.settings.player_speed
            self.y -= self.settings.player_speed
            self.direction = "up_right"
            self.walk_up_right_frame_index = self.animate_walk(
                self.WALK_UP_RIGHT_IMAGES, self.walk_up_right_frame_index)        
        if self.moving_right:
            self.image = self.player_images["right"]
            if self.moving_right and self.rect.right <= self.screen_rect.right:
                self.x += self.settings.player_speed
                self.direction = "right"
            self.walk_right_frame_index = self.animate_walk(
                self.WALK_RIGHT_IMAGES, self.walk_right_frame_index)
        if self.moving_left:
            self.image = self.player_images["left"]
            if self.moving_left and self.rect.left >= self.screen_rect.left:
                self.x -= self.settings.player_speed
                self.direction = "left"
            self.walk_left_frame_index = self.animate_walk(
                self.WALK_LEFT_IMAGES, self.walk_left_frame_index)
        if self.moving_up:
            self.image = self.player_images["up"]
            if self.moving_up and self.rect.top >= self.screen_rect.top:
                self.y -= self.settings.player_speed
                self.direction = "up"
            self.walk_up_frame_index = self.animate_walk(
                self.WALK_UP_IMAGES, self.walk_up_frame_index)
        if self.moving_down:
            self.image = self.player_images["down"]
            if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
                self.y += self.settings.player_speed
                self.direction = "down"
            self.walk_down_frame_index = self.animate_walk(
                self.WALK_DOWN_IMAGES, self.walk_down_frame_index)
            
        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y
            
    def animate_walk(self, walk_images, frame_index):
        """Animate the player's walking motion based on the walk_images list."""
        frame_index = (frame_index + 1) % (len(walk_images) * self.FRAME_DELAY)
        image_index = frame_index // self.FRAME_DELAY
        image_name = walk_images[image_index]
        self.image = image_name
        return frame_index

    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)