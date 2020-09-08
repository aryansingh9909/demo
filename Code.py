import numpy as np
print hello

def check_diagonals():
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  else:
    return None

# checks if the board is completely filled or not
def check_for_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
    return True
  else:
    return False

# swaps the players 
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"

# call the function
play_game()