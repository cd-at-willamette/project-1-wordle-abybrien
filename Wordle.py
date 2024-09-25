########################################
# Name: Abygale Brien
# Collaborators (if any): QUAD People
# GenAI Transcript (if any):
# Estimated time spent (hr): 1.5 Hours
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        row_number = gw.get_current_row()
        string = "" # Empty string to add stuff to it
        for i in range(N_COLS):
           w = gw.get_square_letter(row_number, i)
           string += w
        is_english_word(string)
        if is_english_word(string) and len(string) == 5:
            gw.show_message("")
        else:
            gw.show_message("Not In Word List")
        
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    word = "TRAIN"
    gw.set_square_letter(0, 0, word[0])
    gw.set_square_letter(0, 1, word[1])
    gw.set_square_letter(0, 2, word[2])
    gw.set_square_letter(0, 3, word[3])
    gw.set_square_letter(0, 4, word[4])
    

# Startup boilerplate
if __name__ == "__main__":
    wordle()
