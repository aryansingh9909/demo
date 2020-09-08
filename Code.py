
def display_board():
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9\n")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3\n")

# manages the turn of single player at a time
def handle_turn(player):
  print("Player",player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")
  board[position] = player
  display_board()

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

