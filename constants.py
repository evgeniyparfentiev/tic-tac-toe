# Object sizes
BOARD_WIDTH = 600
BOARD_HEIGHT = 600
FIELD_SIZE = 3
LINE_WIDTH = 10

WINNING_LINE_WIDTH = 20

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

MOUSE_BUTTON_1 = (1, 0, 0)

# Board state
EMPTY_QUADRANT = -1

PLAYER_NOT_WIN = -1
GAME_COMPLETED = -2
GAME_IN_PROGRESS = -1

# Colors
BACKGROUND_COLOR = (240, 240, 240)
LINE_COLOR = (30, 30, 30)

# Mappings
# Each quadrant has special coordinates in board matrix

QUADRANT_BOARD_MAPPINGS = [(0, 0),
                           (0, 1),
                           (0, 2),
                           (1, 0),
                           (1, 1),
                           (1, 2),
                           (2, 0),
                           (2, 1),
                           (2, 2)]

QUADRANT_COORDINATES_MAPPINGS = [(100, 110),
                                 (300, 110),
                                 (500, 110),
                                 (100, 315),
                                 (300, 315),
                                 (500, 315),
                                 (100, 520),
                                 (300, 520),
                                 (500, 520)]

WINNING_QUADRANT_START_POS = [(0, 90),
                              (0, 300),
                              (0, 500),
                              (90, 0),
                              (300, 0),
                              (500, 0),
                              (0,   0),
                              (600, 0)]

WINNING_QUADRANT_END_POS = [(600, 90),
                            (600, 300),
                            (600, 500),
                            (90, 600),
                            (300, 600),
                            (500, 600),
                            (600, 600),
                            (0, 600)]
SIGN_MAPPINGS = ["O", "X"]

SIGN_COLOR_MAPPINGS = [(40, 120, 181), (224, 73, 87)]
