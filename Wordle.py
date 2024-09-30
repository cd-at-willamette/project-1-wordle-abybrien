########################################
# Name: Abygale Brien
# Collaborators (if any): QUAD People
# GenAI Transcript (if any):
# Estimated time spent (hr): 9 Hours 
# Description of any added extensions:
########################################

from WordleGraphics import    WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import  ENGLISH_WORDS, is_english_word
import random 

def wordle(): # The main function to play the Wordle game.
    # RANDOM LETTERS THATS ONLY 5 LETTERS -----------------------------------------
    answer = "" # Start with an empty string 
    while len(answer) != 5: # Exludes words that are greater or less than 5
        answer = random.choice(ENGLISH_WORDS) # choose random word import that is 5 letters long
    print(answer) # Gives a visual base point 
    
    # answer = "sassy" # Practice word for duplicate letters 

    def enter_action(): # What should happen when RETURN/ENTER is pressed
        # CHECKS TO SEE IF ITS WORD LIST OR NOT --------------------------------------
        row_number = gw.get_current_row()
        string = "" # Empty string to add stuff to it
        for i in range(N_COLS): 
           w = gw.get_square_letter(row_number, i)
           string += w # += permanently assigns it 
        is_english_word(string)
        if is_english_word(string) and len(string) == 5: # if it's in english words and length = 5 chars -> show it's in word list
            gw.show_message("In Word List!")
             # GUESS STRING ----------------------------------------------------------
            guess = "" # Empty string for wordle guess
            for i in range(N_COLS): 
                guess += gw.get_square_letter(gw.get_current_row(), i) # += permanently assigns it to guess
                guess = guess.lower()  # Turns guess to lower case (look in terminal for clarification)
            print(guess)

            unmatched = str(answer)
            # COLORING SQUARE LETTERS GREEN -------------------------------------------
            for i in range(N_COLS):
                if guess[i] == answer[i]:
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR) # guess[i] refers to the letter typed into box in wordle
                    unmatched = unmatched.replace(answer[i], "", 1) # Gets rid of duplicate letters
            for i in range(N_COLS): 
            # COLORING SQUARES LETTERS YELLOW --------------------------------------
                if guess[i] in unmatched and gw.get_square_color(gw.get_current_row(), i) != CORRECT_COLOR: # Take whatever letter that is and see if it's in that unmatched variable and it not already green
                    gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                    if gw.get_square_color(gw.get_current_row(), i) != CORRECT_COLOR: 
                        gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR) # Come back too!
                    unmatched = unmatched.replace(answer[i], "", 1) # Gets rid of duplicate letters
            for i in range(N_COLS): 
            # COLORING SQUARE LETTERS GREY -----------------------------------------
                if guess[i] != answer[i] and gw.get_square_color(gw.get_current_row(), i) != PRESENT_COLOR:
                    gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR) # guess[i] refers to the letter typed into box in wordle
                    unmatched = unmatched.replace(answer[i], "", 1) # Gets rid of duplicate letters
                # COLORING THE KEYS --------------------------------------------------------
            for i in range(N_COLS):
                letter = guess[i]
                color = gw.get_square_color(gw.get_current_row(), i)
                if color == CORRECT_COLOR:
                    gw.set_key_color(letter, CORRECT_COLOR)
                elif color == PRESENT_COLOR:
                    if gw.get_key_color(letter) != CORRECT_COLOR:
                        gw.set_key_color(letter, PRESENT_COLOR)
                else:
                    if gw.get_key_color(letter) == UNKNOWN_COLOR:
                        gw.set_key_color(letter, MISSING_COLOR)  
            # NEXT ROW(S)
            gw.set_current_row(gw.get_current_row()+1) # Moves onto the next row by using the + 1 following the row     
            if guess == answer:
                 gw.show_message("Congratulations!")
                 gw.set_current_row(N_ROWS) # stops me from typing 
            elif gw.get_current_row() == N_ROWS: # last row
                 gw.show_message("You Failed")
        else:
            gw.show_message("Not In Word List") # if not either of those -> show it's not in word list
            
        
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    
    # DON'T NEED ANYMORE ----------------------------------------------------------------
    # word = "TRAIN"
    # gw.set_square_letter(0, 0, word[0])
    # gw.set_square_letter(0, 1, word[1])
    # gw.set_square_letter(0, 2, word[2])
    # gw.set_square_letter(0, 3, word[3])
    # gw.set_square_letter(0, 4, word[4])
    

# Startup boilerplate
if __name__ == "__main__":
    wordle()
