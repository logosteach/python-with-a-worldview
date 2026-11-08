# --- settings.py ---
# Centralized game configuration for Gator Invader.

class Settings:
    """A class to manage all game settings."""

    def __init__(self):
        # ------------------------------------------------------------------
        # Screen & Display
        # ------------------------------------------------------------------
        self.screen_width = 320
        self.screen_height = 240

        self.screen_padding_right = 5
        self.screen_padding_left = 5
        self.screen_padding_top = 5
        self.screen_padding_bottom = 5

        # Short aliases for padding (top, right, bottom, left)
        self.tp, self.rp, self.bp, self.lp = (
            self.screen_padding_top,
            self.screen_padding_right,
            self.screen_padding_bottom,
            self.screen_padding_left,
        )

        # Final window is scaled up from the internal resolution
        self.scale_factor = 3
        self.scale_size = self.set_scaled_dimensions(self.scale_factor)

        # ------------------------------------------------------------------
        # Colors
        # ------------------------------------------------------------------
        self.water_color = (0, 92, 230)
        self.bg_color = self.water_color
        self.alpha_color = (255, 0, 255)          # magenta colorkey
        self.white = (255, 255, 255)
        self.midnight = (30, 30, 30)

        # ------------------------------------------------------------------
        # Fonts & UI
        # ------------------------------------------------------------------
        # Font attribution: https://www.fontspace.com/codeman38
        self.game_font = "PressStart2P"
        self.score_board_font_size = 8
        self.button_font_size = 24
        self.button_width, self.button_height = 300, 60
        self.button_color = (0, 135, 0)
        self.button_text_color = (255, 255, 255)

        # Scoreboard / lives panel
        self.bg_panel_color = (200, 200, 200)
        self.bg_panel_width = self.scale_size[0]
        self.bg_panel_height = 20

        # ------------------------------------------------------------------
        # Game Speed
        # ------------------------------------------------------------------
        self.frame_rate = 60

        # ------------------------------------------------------------------
        # Gator (Player) Settings
        # ------------------------------------------------------------------
        # Movement state constants
        self.GATOR_NOT_MOVING = 0
        self.GATOR_MOVING_UP = 1
        self.GATOR_MOVING_RIGHT = 2
        self.GATOR_MOVING_DOWN = 3
        self.GATOR_MOVING_LEFT = 4

        self.gator_width = 32
        self.gator_height = 12
        self.gator_scale_factor = 1
        self.gator_icon_scale_factor = self.gator_scale_factor / 1.2

        self.gator_left_right_speed = 4
        self.gator_up_down_speed = 3

        self.max_lives = 3
        self.gator_icon_gap = 5

        # ------------------------------------------------------------------
        # Enemy Settings
        # ------------------------------------------------------------------
        self.enemy_width = 32
        self.enemy_height = 23
        self.enemy_scale_factor = 1

        self.enemy_horiz_speed = 1
        self.enemy_vert_speed = 1

        self.fleet_direction = 1
        self.advance_fleet_forward = False
        self.enemy_left_boundary = self.gator_width // 2

        self.mouth_open_index = 5

        # Enemy type constants
        self.ENEMY_RED = 0
        self.ENEMY_PURPLE = 1
        self.ENEMY_BLUE = 2
        self.ENEMY_DEAD = -1

        # Scoring
        self.red_enemy_pts = 50
        self.purple_enemy_pts = 100
        self.blue_enemy_pts = 150

        self.red_enemy_hit_by_fireball = 10
        self.purple_enemy_hit_by_fireball = 20
        self.blue_enemy_hit_by_fireball = 30

        # ------------------------------------------------------------------
        # Fireball Settings
        # ------------------------------------------------------------------
        self.max_fire_balls = 5
        self.fire_ball_width = 16
        self.fire_ball_height = 8
        self.fire_ball_hit_width = 14
        self.fire_ball_hit_height = 14
        self.fire_ball_speed = 5
        self.fire_ball_animation_interval = 0.1

        # Duration the gator's mouth stays open when firing
        self.mouth_open_interval = 0.25

        # ------------------------------------------------------------------
        # Screen Boundaries
        # ------------------------------------------------------------------
        self.left_boundary = 10
        self.right_boundary = self.screen_width
        self.middle_boundary = self.right_boundary // 2
        self.top_boundary = self.bg_panel_height + self.screen_padding_top
        self.bottom_boundary = self.screen_height - self.bg_panel_height // 2

    @property
    def dimensions(self):
        """Return the internal screen dimensions as a tuple."""
        return (self.screen_width, self.screen_height)

    def set_scaled_dimensions(self, scale):
        """Return the scaled window size, ensuring scale is at least 1."""
        scale = max(scale, 1)
        return (scale * self.screen_width, scale * self.screen_height)
