# tic-tac-toe game using Tkinter. Future use will include AI 
# tkinter must be at least 8.6
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
