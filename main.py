import sys

player1 = "Player 1"
player2 = "Player 2"
symbol1 = "\033[1;32mX\033[0;37m"
symbol2 = "\033[1;31mO\033[0;37m"

player = player1
symbol = symbol1


board = [['', 'X', '', '', '', '', '', 'O'], ['', '', 'X', '', '', '', '', ''], ['', '', '', 'X', '', '', '', ''], ['', '', '', '', 'X', '', '', ''], ['', '', '', '', '', '', '', ''], ['', '', '', '', '', '', '', ''], ['', 1, 2, 3, 4, 5, 6, 7]]

def prettyPrint(board):
  print() 
  for row in board:
    for item in row:  
     print(f"{item:^1}", end=" | ")
    print("\n")
  print()
prettyPrint(board)

def checkDownwardDiagonalWin(board, symbol, player):
  i = 1
  for row in board:
    print(row[i])
    i += 1
    
checkDownwardDiagonalWin(board, symbol, player)
# Can print diagonal starting at [0][0], how to start at [0][1]?

  