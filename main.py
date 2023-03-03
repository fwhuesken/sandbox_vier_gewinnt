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
    symbol = symbol2 # specify symbol on horizontalBoard for player1
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

horizontalBoard = ['','X','X','X','','','']
verticalBoard = [['X','X',''],['X','',''],['X','',''],['X','','']]
symbol = 'X'
player = 'Player 1'

def announceWinner(player):
  print(f"{player} wins the game, whoop whoop!")
  sys.exit()

def checkHorizontalWin(horizontalBoard, symbol, player):
  count = 0
  for i in range(len(horizontalBoard)):
    if horizontalBoard[i] == symbol:
      count += 1
      if count == 4:
        announceWinner(player)
    else:
      count = 0 # resets count to 0
    #print(horizontalBoard[i])


counts = [0] * len(verticalBoard[0])
def checkVerticalWin(verticalBoard, symbol, player):
  for sublist in verticalBoard:
      for i in range(len(sublist)):
          if sublist[i] == symbol:
              counts[i] += 1
  print(counts)
  
  for row in counts:
    if row >= 4:
      announceWinner(player)
  
  






checkHorizontalWin(horizontalBoard, symbol, player)
checkVerticalWin(verticalBoard, symbol, player)

