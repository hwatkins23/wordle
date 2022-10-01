# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

from multiprocessing import current_process
import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
from WordleGraphics import WordleGWindow

def wordle():

    """Milestone 2"""
    def enter_action(s):
        guess = s.lower()
        if guess in FIVE_LETTER_WORDS:
            gw.show_message("Yay! I found it in the dictionary!")
        else:
            gw.show_message("That word ain't in our dictionary")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    """Milestone 1"""
    N_COLS = 0
    N_ROWS = 0

    WORD = random.choice(FIVE_LETTER_WORDS)
    for char in WORD:
        gw.set_square_letter(row=N_ROWS, col=N_COLS, ch=char)
        N_COLS = N_COLS + 1


# Startup code

if __name__ == "__main__":
    wordle()
