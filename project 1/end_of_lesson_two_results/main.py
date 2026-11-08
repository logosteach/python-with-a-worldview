# --- main.py ---

# All this code is NEW!

import sys, pygame

from pygame.sprite import Group
from settings import Settings
from game_tool_settings import GameToolSettings
from guide import Guide
from gator import Gator

class Game:
    # The root class that handles the game.
    def __init__(self):
        # Initialize the game assets.
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode( self.settings.scale_size )
        self.surface = pygame.Surface(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Gator Invader")
        
        self.running = True
        self.pause = False
        
        # Has the play button been pressed and are we in "play mode"?
        self.game_active = False
        
        # Create the Hero
        self.gator = Gator(self)
        
        # Create the game tool settings instance
        self.tool_settings = GameToolSettings(self)
        
        # ---- Game Tools ----
        self.toggle_guides = False
        self.guides = Group()
        for point in self.tool_settings.boundary_guides:
            guide = Guide()
            guide._color = self.tool_settings.guide_color
            guide._line_width = self.tool_settings.line_width
            guide._begin = point[0]
            guide._end = point[1]
            self.guides.add(guide)
        
        # Game Clock
        self.clock = pygame.time.Clock()
        
    """ Event Checking """

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)

            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)
                
    def _check_key_down_events(self, event):
        if event.key == pygame.K_UP:
            self.gator.moving = self.gator.UP
        elif event.key == pygame.K_RIGHT:
            self.gator.moving = self.gator.RIGHT
        elif event.key == pygame.K_DOWN:
            self.gator.moving = self.gator.DOWN
        elif event.key == pygame.K_LEFT:
            self.gator.moving = self.gator.LEFT
        # Toggle the Guidelines
        elif event.key == pygame.K_1:
            self.toggle_guides = not self.toggle_guides
    
    def _check_key_up_events(self, event):
        if event.key == pygame.K_UP:
            self.gator.moving = self.gator.NOT_MOVING
        elif event.key == pygame.K_DOWN:
            self.gator.moving = self.gator.NOT_MOVING
        elif event.key == pygame.K_RIGHT:
            self.gator.moving = self.gator.NOT_MOVING
        elif event.key == pygame.K_LEFT:
            self.gator.moving = self.gator.NOT_MOVING
    
    """ Update Game and Asset Logic """
    
    def update(self):
        """Controls the updating of screen items, such as coordinates
        and other properties that need to be updated each time a new
        frame is ready to be drawn."""
        self.gator.update()
    
    """ Drawing Methods """

    def _draw_items(self):
        # Draw the game items to the screen.
        self.surface.fill(self.settings.bg_color)
        self.gator.blitme()
        
        if self.toggle_guides:
            for guide in self.guides:
                guide.blitme(self.surface)
        
        self.screen.blit(
            pygame.transform.scale(self.surface, self.settings.scale_size),
            (0,0)
        )
        pygame.display.flip()
        
    """ Run Loop """

    def run(self):
        # The Main Game Loop
        
        """
            Using 1 instead of True makes the loop run
            just a little bit faster. Go figure. :-)
        """
        while 1:
            self._check_events()
            self.update()
            self._draw_items()
            
            # Set the default FPS to 60 frames per second.
            # Don't put too much hope in that this will
            # work all the time. It 'kind-of' works. :-)
            self.clock.tick(60)
            
            if not self.running:
                break
            
            # See how amazingly readable this run() method is?
            # this is again, the beauty of code clarity that comes
            # with using functions.
            
""" Main Program --------------------------------------------- """

if __name__ == "__main__":
    game = Game() # create the Game instance
    game.run() # run the main loop. That is it!