import random

def display_board(board):
  print("+-----+-----+-----+")
  for row in board:
    print("|     |     |     |")
    print(f"|  {row[0]}  |  {row[1]}  |  {row[2]}  |")
    print("|     |     |     |")
    print("+-----+-----+-----+")


def enter_move(board):
    ok = False
    while not ok:
        move = input()
        ok = len(move) == 1 and int(move) in range(1,10)
        if not ok:
            print("Bad move")
            print("Re-enter your move")
        move = int(move) - 1
        col = move % 3
        row = move // 3
        move = board[row][col]
        if move in ('X', 'O'):
            print ("This square is occupied")
            print("Please Re-enter")


    	
    


def make_list_of_free_fields(board):
  free_list = []
  for i in range(3):
    for j in range(3):
      if board[i][j] != 'X' and board[i][j] != 'O':
        free_list.append(board[i][j])
  return free_list
  



#def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
  

board = []
count = 1

for i in range(3):
  row = []
  for j in range(3):
    row.append(count)
    count += 1
  board.append(row)

play = True
while play:
  display_board(board)
  player = enter_move(board)
  comp = draw_move(board)
  print(player)
  free = make_list_of_free_fields(board)
  
  
  
