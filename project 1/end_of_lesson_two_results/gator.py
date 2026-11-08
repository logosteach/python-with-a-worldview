# -- gator.py ---
# This entire code block is NEW!

import os, pygame
from pygame.sprite import Sprite

class Gator(Sprite):
    # A class that represents our hero.
    def __init__(self, game_instance):
        
        super().__init__()

        # By getting a memory copy of the game_instance settings,
        # our gator can now have access to the settings that it
        # needs. Cool huh? Remember, this is just memory copy.
        # we are not actually creating a whole new settings object.
        # that would be a tragic waste of memory.
        self.settings = game_instance.settings

        # We do not need the screen, just the surface to draw to.
        # This is why we pass in a reference to our game instance
        # so that we can get access to draw to its surface.
        self.surface = game_instance.surface

        # The sheet is one image that contains both sub-images of 
        # our gator. Mouth opened and mouth closed.

        # os.path.join is recommended for you to use. Why?
        # because it is system independent. This means that this
        # should work on Windows, MacOS and Linux file systems.
        # without os.path.join, you will have to customize your own
        # path data for each system your users will use.
        # that is a total bummer dude!
        self.sheet = pygame.image.load(os.path.join("images", "gator.png"))

        # Each individual image will be called a frame. We grab each frame
        # and place them into a list.
        # frame[0] is mouth closed.
        # frame[1] is mouth opened.
        self.frames = [
            self.get_image(
                0, # the first gator is column 0
                0, # row 0
                self.settings.gator_width,
                self.settings.gator_height,
                1,
                self.settings.alpha_color,
            ),
            self.get_image(
                0, # the second gator is column 0
                1, # row 1
                self.settings.gator_width,
                self.settings.gator_height,
                1,
                self.settings.alpha_color,
            ),
        ]

        # This will help us scale the gator icon to a smaller size.
        self.image = self.get_image(
            0,
            1,
            self.settings.gator_width,
            self.settings.gator_height,
            self.settings.gator_icon_scale_factor,
            self.settings.alpha_color,
        )

        # A rectangle is different than the image. The rectangle is
        # the mathematical entity that is needed to draw the image
        # to an actual location on the screen. Also, we use the 
        # rectangle for enemy hit data. If an enemy hits our
        # hero or a projectile hits our hero, this is why
        # we need the self.rect attribute.
        self.rect = self.frames[0].get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.width = float(self.rect.width)
        self.height = float(self.rect.height)
        
        # Motion Settings
        self.NOT_MOVING = self.settings.GATOR_NOT_MOVING
        self.UP = self.settings.GATOR_MOVING_UP
        self.RIGHT = self.settings.GATOR_MOVING_RIGHT
        self.DOWN = self.settings.GATOR_MOVING_DOWN
        self.LEFT = self.settings.GATOR_MOVING_LEFT
        
        self.moving = self.NOT_MOVING

    # Our own customized, handy, dandy, get_image() method. This will
    # extract each image frame from our spritesheet.
    def get_image(self, col_x, row_y, width, height, scale, color):
        # Notice that it is possible to SCALE the image in this method,
        # but we are going to use a value of 1, because we don't need
        # to do this.
        
        # The colorkey (or color parameter) is the alpha_color. 
        # It is the magenta value that
        # we are going to ignore. This is how we get transparency.

        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(
            self.sheet, (0, 0), ((col_x * width), (row_y * height), width, height)
        )
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image

    def update(self):
        if self.moving == self.UP:
            self.y -= self.settings.gator_up_down_speed
        elif self.moving == self.DOWN:
            self.y += self.settings.gator_up_down_speed
        elif self.moving == self.RIGHT:
            self.x += self.settings.gator_left_right_speed
        elif self.moving == self.LEFT:
            self.x -= self.settings.gator_left_right_speed
            
        # boundary checker
        if self.x < self.settings.left_boundary:
            self.x = self.settings.left_boundary

        elif self.x + self.width > self.settings.middle_boundary:
            self.x = self.settings.middle_boundary - self.width

        elif self.y < self.settings.top_boundary:
            self.y = self.settings.top_boundary

        elif self.y + self.height > self.settings.bottom_boundary:
            self.y = self.settings.bottom_boundary - self.height

        # The rect object x and y values will automatically
        # be cast back to integers. Python will do this for you.
        self.rect.x = self.x
        self.rect.y = self.y

        # update the x and y values one more time.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        # We customize our own blit method and call it 'blitme' because
        # that is cute.
        self.surface.blit(self.frames[0], self.rect)

        # self.frames[0] contains the image to be drawn.
        # self.rect holds the location data and width/height data
        # on where and how to draw it.

        # For now, we have no animation, and only draw self.frames[0]
        # to the surface.
