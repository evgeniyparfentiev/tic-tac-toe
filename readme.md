NOTE: This project is not completed yet.
It is dedicated to create self-learning AI for a simple classic tic-tac-toe game in Python.
The AI part is not completed, but main difference of this project from many others is the module structure and separation of
the UI level, board object with game rules and player object which allows to add new AI types in general manner.

board_ui.py - Contains all the logic to show the board and game objects
constants.py - Contains all the constants
game_board.py - Store the active board state and calculate the current game state
human_player.py - Contains the methods which allows human player make a move
main.py - main module which runs the main cycle of the application
requirements.txt - external dependencies
tic-tac-toe.py - main loop of application which manage the game cycle and UI refresh.
player.py - base class, the expansion point of application  - inheriting it, new AI can be added