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
       
        def _get_winning_combos(self):
            rows = [
                [(move.row, move.col) for move in row]
                for row in self._current_moves
            ]
            columns = [list(col) for col in zip(*rows)]
            first_diagonal = [row[i] for i, row in enumerate(rows)]
            second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
            return rows + columns + [first_diagonal, second_diagonal]

        # return a toggled player
        def toggle_player(self):
               self.current_player = next(self._players)
        
        def is_valid_move(self, move):
            #    Returns True if a valid move, otherwise False
            row, col = move.row, move.col
            move_was_not_played = self._current_moves[row][col].label
            no_wnner = not self._has_winner
            return no_winner and move_was_not_played
        
        def process_move(self, move):
            #    process current move and check if it is a win
            row, col = move.row, move.col
            self._current_moves[row][col] = move
            for combo in self._winning_combos:
                    results = set(self._current_moves[n][m].label for n, m in combo)
                    if is_win:
                           self._has_winner = True
                           self.winner_combo = combo
                           break
        
        def has_winner(self):
            #    return True if winner, else False
            return self._has_winner
        
        def is_tied(self):
            #    return True if the game is tied, else False
            no_winner = not self._has_winner
            played_moves = (
                  move.label for row in self._current_moves for move in row
            )
            return no_winner and all(played_moves)
        
        def reset_game(self):
            #   reset to play the game again
            for row, row_content in enumerate(self._current_moves):
                  for col, _ in enumerate(row_ccontent):
                        row_content[col] = Move(row, col)
            self._has_winner = False
            self.winner_combo = []

