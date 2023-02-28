import sys
"""
player1 = "Player 1"
player2 = "Player 2"
symbol1 = "\033[1;32mX\033[0;37m"
symbol2 = "\033[1;31mO\033[0;37m"

player = player1
symbol = symbol1

def changePlayer(player, symbol):
  if player == player1: 
    player = player2
    symbol = symbol2 # specify symbol on board for player1
    #print(player, symbol)
  else:
    player = player1 # switch players for next round
    symbol = symbol1 # specify symbol on board for player1
    #print(player, symbol)
  print(player, symbol)
  return player, symbol

#changePlayer(player, symbol)
player = changePlayer(player, symbol)[0]
symbol = changePlayer(player, symbol)[1]

print(player)
print(symbol)
#changePlayer(player, symbol)
"""

board = ['X','X','X','X','','','']
board2 = [['X','',''],['X','',''],['X','',''],['X','','']]
symbol = 'X'
player = 'Player 1'

def announceWinner(count, player):
  if count == 4:
    print(f"{player} wins the game, whoop whoop!")
    sys.exit()

def checkHorizontalWin(board, symbol):
  count = 0
  for i in range(len(board)):
    if board[i] == symbol:
      count += 1
      announceWinner(count, player)
    else:
      count -= 1
      print(count)
    print(board[i])










checkHorizontalWin(board, symbol)


