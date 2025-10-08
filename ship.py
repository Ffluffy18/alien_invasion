import pygame

class Ship:
    """A class to manage the ship."""
    # rect is short for rectangle
    # even if element is not a rectangle, treating it as such is efficient because rectangles are simple geometric shapes.
    # when Pygame needs to figure out whether two game elements have collided, it can do this more quickly if it treats each object as a rectangle

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        # ai_game is a reference to the AlienInvasion class
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the sihp's exact horizontal position.
        # self.rect.x is the current integer position of the ship's rectangle
        # self.x is the floating-point (precise) horizontal position
        # this way fractioanl speeds (like 1.5) aren't lost when updating rect
        self.x = float(self.rect.x)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

