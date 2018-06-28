import pygame as pg
import board_ui as user_ui
import game_board as board
import human_player as pl
import constants as const


def start_game():
    move_number = 1

    game_board = board.GameBoard()

    board_ui = user_ui.BoardOnScreen()
    board_ui.init_board_ui()

    player = [pl.HumanPlayer(), pl.HumanPlayer()]

    while True:
        active_player = get_active_player(move_number)

        move = None
        while move is None:
            current_move = player[active_player].make_move(game_board.get_board())
            if game_board.is_valid_move(current_move):
                move = current_move

        game_board.update_board(move, active_player)
        board_ui.draw(game_board.get_board())
        game_status = game_board.get_board_state()

        if game_status.game_state > const.GAME_IN_PROGRESS:
            board_ui.draw_winner(game_status)

        move_number += 1

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                pg.quit()
                quit()


def get_active_player(turn_to_play):
    return turn_to_play % 2
