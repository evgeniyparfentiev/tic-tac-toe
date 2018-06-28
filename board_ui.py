import pygame as pg
import constants as const
from game_board import GameBoardState


class BoardOnScreen(object):

    __screen = None

    def init_board_ui(self):
        pg.init()
        pg.display.set_caption("Tic Tac Toe")
        self.__screen = pg.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
        self.__screen.fill(const.BACKGROUND_COLOR)
        self.draw_game_field()
        pg.display.update()

    def draw_game_field(self):
        self.draw_verticals()
        self.draw_horizontals()

    def draw_verticals(self):
        first_line_x_coord = const.BOARD_WIDTH / const.FIELD_SIZE
        second_line_x_coord = first_line_x_coord * 2

        rect1 = pg.Rect(first_line_x_coord, 0, const.LINE_WIDTH, const.BOARD_HEIGHT)
        pg.draw.rect(self.__screen, const.LINE_COLOR, rect1)

        rect1 = pg.Rect(second_line_x_coord, 0, const.LINE_WIDTH, const.BOARD_HEIGHT)
        pg.draw.rect(self.__screen, const.LINE_COLOR, rect1)

    def draw_horizontals(self):
        first_line_y_coord = const.BOARD_WIDTH / const.FIELD_SIZE
        second_line_y_coord = first_line_y_coord * 2

        rect1 = pg.Rect(0, first_line_y_coord, const.BOARD_WIDTH, const.LINE_WIDTH)
        pg.draw.rect(self.__screen, const.LINE_COLOR, rect1)

        rect1 = pg.Rect(0, second_line_y_coord, const.BOARD_WIDTH, const.LINE_WIDTH)
        pg.draw.rect(self.__screen, const.LINE_COLOR, rect1)

    def draw(self, game_board):

        self.draw_game_board(game_board)

        pg.display.update()

    @staticmethod
    def text_objects(text, font, board_value):
        text_color = const.SIGN_COLOR_MAPPINGS[board_value]
        text_surface = font.render(text, False, text_color)
        return text_surface

    @classmethod
    def get_selected_quadrant(cls, x, y):

        col = int((float(x) / const.BOARD_WIDTH) * const.FIELD_SIZE)
        row = int((float(y) / const.BOARD_HEIGHT) * const.FIELD_SIZE)
        return col + row * const.FIELD_SIZE

    def draw_game_board(self, game_board):
        text = pg.font.Font('freesansbold.ttf', 200)
        for x in range(0, 9):

            board_coordinates = const.QUADRANT_BOARD_MAPPINGS[x]
            board_value = game_board[board_coordinates]

            if board_value != const.EMPTY_QUADRANT:

                board_sign = const.SIGN_MAPPINGS[board_value]
                text_surface = self.text_objects(board_sign, text, board_value)

                screen_coordinates = const.QUADRANT_COORDINATES_MAPPINGS[x]
                mark_rectangle = text_surface.get_rect()
                mark_rectangle.centerx = screen_coordinates[0]
                mark_rectangle.centery = screen_coordinates[1]
                self.__screen.blit(text_surface, mark_rectangle)

    def draw_winner(self, game_status):

        assert isinstance(game_status, GameBoardState)

        start_pos = const.WINNING_QUADRANT_START_POS[game_status.winning_combination]
        end_pos = const.WINNING_QUADRANT_END_POS[game_status.winning_combination]
        color = const.SIGN_COLOR_MAPPINGS[game_status.game_state]
        pg.draw.line(self.__screen, color, start_pos, end_pos, const.WINNING_LINE_WIDTH)
        pg.display.update()
