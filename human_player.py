from player import Player
import board_ui as user_ui
import pygame as pg
import constants as const


class HumanPlayer(Player):

    def make_move(self, game_board):
        user_selected_quadrant = True
        user_select = None
        while user_selected_quadrant:
            for event in pg.event.get():
                m_pos = pg.mouse.get_pos()
                m_press = pg.mouse.get_pressed()
                if m_press == const.MOUSE_BUTTON_1:
                    if m_pos[0] <= const.BOARD_WIDTH and m_pos[1] <= const.BOARD_HEIGHT:
                        user_select = user_ui.BoardOnScreen.get_selected_quadrant(m_pos[0], m_pos[1])
                        user_selected_quadrant = False
        return user_select
