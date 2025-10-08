import sys

import pygame

from settings import Settings

from ship import Ship

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

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # calls the methods _check_events() into the loop
            # to call this methods from within the class, I used dot notation with the variable self and name of the methods
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # the event 'pygame.QUIT' is the x at the top right of screen
        # each event (keypress) is picked up by the pygame.event.get() method
        # each keypress is registered as a KEYDOWN event. 
        # when Pygame detects a KEYDOWN event, I need to check whether the key that was pressed triggers an action.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #redraw the screen during eacch pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # flip() is the display to put your work on screen(makes the most recently drawn screen visible).
        pygame.display.flip()

# checks wheter the file is being run directly.Also prevents some code from running when importing this file as a module
#  (so basically you need to call the function directly for it to run)
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


