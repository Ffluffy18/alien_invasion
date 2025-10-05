import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        # pygame.init() function initialized the background settings that Pygame needs to work properly
        # called pygame.display.set_mode to create a display window on which we'll draw all the game's graphical elements
        # set the display window to the attribue 'self.screen', so it will be available in all methods in the class
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        # the event 'pygame.QUIT' is the x button
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during eacch pass through the loop.
            self.screen.fill(self.settings.bg_color)
            # flip() is the display to put your work on screen(makes the most recently drawn screen visible).
            pygame.display.flip()
            self.clock.tick(60)
# checks wheter the file is being run directly.Also prevents some code from running when importing this file as a module
#  (so basically you need to call the function directly for it to run)
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


