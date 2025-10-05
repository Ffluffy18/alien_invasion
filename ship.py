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
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

