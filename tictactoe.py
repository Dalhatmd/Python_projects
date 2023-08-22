import random

def display_board(board):
  print("+-----+-----+-----+")
  for row in board:
    print("|     |     |     |")
    print(f"|  {row[0]}  |  {row[1]}  |  {row[2]}  |")
    print("|     |     |     |")
    print("+-----+-----+-----+")


def enter_move(board):
  try:
    move = int(input("Enter a number corresponding to a free square: "))
    if move not in range(0, 10):
      print("Enter a number between 1 and 9")
  except ValueError:
      print("Enter a number please")
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == move:
        board[i][j] = 'O'
        return board[i][j]
    
  	
    	
    


def make_list_of_free_fields(board):
  free_list = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] in range(1, 9):
        free_list.append((i, j))
  return free_list



#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
  comp_move = random.randrange(0, 10)
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == comp_move:
        board[i][j] = 'X'
  return board[i][j]

board = []
count = 1

for i in range(3):
  row = []
  for j in range(3):
    row.append(count)
    count += 1
  board.append(row)



display_board(board)
player = enter_move(board)
print(player)
"""display_board(board)
comp = draw_move(board)
print(comp)
display_board(board)
free = make_list_of_free_fields(board)
print(free)"""
  
  
