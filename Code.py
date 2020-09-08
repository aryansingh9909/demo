
# verifies if the game is completed
def check_if_game_over():
  check_for_winner()
  check_for_tie()

# finds if any player is the winner
def check_for_winner():
  global winner
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = Non



#changes done
#changes has been done


import numpy as np
print hello

def play_game():
  print("\n    X - O     G A M E\n")
  print("Note : Use the numpad to enter X or O in respective fields.\n")
  display_board()
  while game_still_going:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  if winner == "X" or winner == "O":
    print("PLAYER",winner,"IS THE WINNER !!.")
  elif winner == None:
    print("Tie.")
  print("\nT H A N K S     F O R     P L A Y I N G     ! ! ! ! !")
