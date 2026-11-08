# Create a file named: guide.py and place the code you find here in that file.

# --- guide.py ---
# All the code in the block below is NEW! 

import pygame

from pygame.sprite import Sprite

class Guide(Sprite):

    def __init__(self):
        super().__init__()
        self._begin = None
        self._end = None
        self._color = None
        self._line_width = None

    def update(self):
        pass

    def blitme(self, surface):
        pygame.draw.line(surface, self._color, self._begin, self._end, self._line_width)

    def __str__(self):
        return f"{self._begin}:{self._end}, color:{self._color}"