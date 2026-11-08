# create a file named: game_tool_settings.py in your root project folder and place the code you find here in that file.

# --- game_tool_settings.py ---
# The code block below is all NEW!
import pygame

class GameToolSettings:
    def __init__(self, game_instance):
        self.screen_width = game_instance.settings.screen_width
        self.screen_height = game_instance.settings.screen_height

        # Guideline Settings
        self.guide_color = (255, 255, 153)  # nice bright yellow.
        self.line_width = 1

        # Boundary settings
        self.left_boundary = 10
        self.lb_begin = (self.left_boundary, 0)
        self.lb_end = (self.left_boundary, self.screen_height)

        self.bottom_boundary = 20
        self.bb_begin = (0, self.screen_height - self.bottom_boundary)
        self.bb_end = (self.screen_width, self.screen_height - self.bottom_boundary)

        self.top_boundary = 20
        self.tb_begin = (0, self.top_boundary)
        self.tb_end = (self.screen_width, self.top_boundary)

        self.middle_boundary = self.screen_width // 2
        self.mb_begin = (self.middle_boundary, 0)
        self.mb_end = (self.middle_boundary, self.screen_height)

        self.boundary_guides = [
            (self.tb_begin, self.tb_end),
            (self.bb_begin, self.bb_end),
            (self.lb_begin, self.lb_end),
            (self.mb_begin, self.mb_end),
        ]