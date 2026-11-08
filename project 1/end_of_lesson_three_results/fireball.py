# fireball.py
import os
import pygame

from pygame.sprite import Sprite

# We are going to create this class soon.
from stopwatch import StopWatch

class Fireball(Sprite):
    # A representation of a fireball.

    def __init__(self, game_instance):
        # Initialize the fireball resources

        # Since Fireball is an instance of Sprite, we need a call
        # to super()
        super().__init__()
        self.settings = game_instance.settings
        self.surface = game_instance.surface

        # load all 8 fireball images located in one image file.
        self.sheet = pygame.image.load(os.path.join("images/", "fireball.png"))
        
        # will create the stopwatch class shortly after we finish fireball.
        # I found that my animations were drawing too quickly.
        self.animation_stop_watch = StopWatch(
            self.settings.fire_ball_animation_interval
        )

        # For now, make the scale normal.
        self.scale = 1

        # current frame is frame 0
        self.current_frame = 0
        
        # 8 frames of fireball magic being loaded from the sheet.
        # we will use this list to advance through our fireball animation.
        self.key_frames = [0, 1, 2, 3, 4, 5, 6, 7]
        
        self.frames = [
            self.get_image(
                0, # column number
                0, # row number
                self.settings.fire_ball_width,
                self.settings.fire_ball_height,
                self.scale,
                self.settings.alpha_color,
            ),
            self.get_image(
                1,
                0,
                self.settings.fire_ball_width,
                self.settings.fire_ball_height,
                self.scale,
                self.settings.alpha_color,
            ),
            self.get_image(
                0,
                1,
                self.settings.fire_ball_width,
                self.settings.fire_ball_height,
                self.scale,
                self.settings.alpha_color,
            ),
            self.get_image(
                1,
                1,
                self.settings.fire_ball_width,
                self.settings.fire_ball_height,
                self.scale,
                self.settings.alpha_color,
            ),
            self.get_image(
                0,
                2,
                self.settings.fire_ball_width,
                self.settings.fire_ball_height,
                self.scale,
                self.settings.alpha_color,
            ),
            self.get_image(
                1,
                2,
                self.settings.fire_ball_width,
                self.settings.fire_ball_height,
                self.scale,
                self.settings.alpha_color,
            ),
            self.get_image(
                0,
                3,
                self.settings.fire_ball_width,
                self.settings.fire_ball_height,
                self.scale,
                self.settings.alpha_color,
            ),
            self.get_image(
                1,
                3,
                self.settings.fire_ball_width,
                self.settings.fire_ball_height,
                self.scale,
                self.settings.alpha_color,
            ),
        ]
        
        # The size of the fireball hit rectangle will be the same size
        # as the rectangle of the first frame.
        self.rect = self.frames[0].get_rect() # NEW
        self.x = float(self.rect.x) # NEW
        self.y = float(self.rect.y) # NEW
        self.width = self.rect.width # NEW
        self.height = self.rect.height # NEW

        # Fireballs need a way to be removed from memory and this
        # is how we will accomplish this.
        self.remove_from_screen = False # NEW

        # Get that animation timer going!
        self.animation_stop_watch.start_timer() # NEW
        
    def get_image(self, col_x, row_y, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(
            self.sheet, (0, 0), ((col_x * width), (row_y * height), width, height)
        )

        # if we want the image larger or smaller, this is where that 
        # happens.
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image

    def set_rect_location(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.x += self.settings.fire_ball_speed
        self.rect.x = self.x
        self.animation_stop_watch.tick()

        # alarm trips when enough time has passed to signal
        # advancing to the next frame.
        if self.animation_stop_watch.trip_alarm():
            self.current_frame += 1
            self.animation_stop_watch.reset()
            self.animation_stop_watch.start_timer()

        # We only have 8 frames, when we reach the end
        # it is time to return to the beginning of the 
        # frame list.
        if self.current_frame % len(self.key_frames) == 0:
            self.current_frame = 0

        # Fireball is OFF the screen! Signal for removal.
        if self.rect.x > self.settings.screen_width:
            self.remove_from_screen = True
            
    def blitme(self):
        self.surface.blit(self.frames[self.key_frames[self.current_frame]], self.rect)