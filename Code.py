
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