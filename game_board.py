import numpy as np
import constants as const
from collections import namedtuple

GameBoardState = namedtuple('GameBoardState', [
                                'game_state',
                                'winning_combination'
                            ])


class GameBoard(object):
    __game_board = None

    def __init__(self):
        self.__game_board = np.ndarray([const.FIELD_SIZE, const.FIELD_SIZE], dtype=int)
        self.__game_board.fill(-1)

    def get_board(self):
        return self.__game_board

    def update_board(self, move, player):
        board_coord = const.QUADRANT_BOARD_MAPPINGS[move]
        self.get_board()[board_coord] = player

    def is_valid_move(self, move):
        board_coord = const.QUADRANT_BOARD_MAPPINGS[move]
        return self.get_board()[board_coord] == const.EMPTY_QUADRANT

    def get_board_state(self):

        first_player = 1
        second_player = 0

        first_player_result = self.get_player_result(first_player)
        second_player_result = const.PLAYER_NOT_WIN

        if first_player_result == const.PLAYER_NOT_WIN:
            second_player_result = self.get_player_result(second_player)

        if first_player_result > const.PLAYER_NOT_WIN:
            return GameBoardState(first_player, first_player_result)
        elif second_player_result > const.PLAYER_NOT_WIN:
            return GameBoardState(second_player, second_player_result)

        if self.game_in_progress():
            return GameBoardState(const.GAME_IN_PROGRESS, None)
        else:
            return GameBoardState(const.GAME_COMPLETED, None)

    def game_in_progress(self):
        return (self.__game_board.any(const.GAME_IN_PROGRESS)).any()

    def get_player_result(self, player):

        result = const.PLAYER_NOT_WIN
        winning_combination = np.array([player, player, player])
        # in result rows are in range from 1 to 3
        for i in range(3):
            row = self.__game_board[i, :]
            if np.array_equal(row, winning_combination):
                result = i
                return result

        # columns are from rows i.e. in range from 3 to 5
        for i in range(3):
            col = self.__game_board[:, i]
            if np.array_equal(col, winning_combination):
                result = i + 3
                return result

        # diagonals are after columns i.e. in range from 6 to 7
        diagonal = np.array([self.__game_board[i, i] for i in range(3)])
        if np.array_equal(diagonal, winning_combination):
            result = 6
            return result

        cross_diagonal = np.array([self.__game_board[2-i, i] for i in range(3)])
        if np.array_equal(cross_diagonal, winning_combination):
            result = 7

        return result

