# tic-tac-toe game using Tkinter. Future use will include AI 
# tkinter must be at least Version 8.6
import tkinter 
tkinter.TkVersion
from itertools import cycle
from tkinter import font
from typing import NamedTuple

class Player(NamedTuple):
        label: str
        color: str

class Move(NamedTuple):
        row: int
        col: int
        label: str = ""
    
BOARD_SIZE = 3
DEFAULT_PLAYERS = (
        Player(label="X", color="red"),
        Player(label="O", color="blue"),
)

class TicTacToeGame:
        def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
                self._players = cycle(players)
                self.board_size = board_size
                self.current_player = next(self._players)
                self.winner_combo = []
                self._current_moves = []
                self._has_winner = False
                self._winning_combos = []
                self._setup_board()
       
        def _setup_board(self):
                self._current_moves = [
                        [Move(row, col) for col in range(self.board_size)]
                        for row in range(self.board_size)
                ]
                self._winning_combos = self._get_winning_combos()
                