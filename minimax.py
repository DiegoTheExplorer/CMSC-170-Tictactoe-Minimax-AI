from copy import deepcopy

# Checks if the game is done at the current state
# 0 if game is not over
# 1 if current player wins
# 2 if the game is a draw
def isEndState(gameState):

  #Checking rows and columns for a win
  for i in range(0,3):
    rChk = set([gameState[i][0],gameState[i][1],gameState[i][2]])
    cChk = set([gameState[0][i],gameState[1][i],gameState[2][i]])

    if (len(rChk) == 1 or len(cChk) == 1):
      return 1
  
  #Checking diagonals for a win
    diag1 = set([gameState[0][0],gameState[1][1],gameState[2][2]])
    diag2 = set([gameState[0][2],gameState[1][1],gameState[2][0]])

    if (len((diag1)) == 1 or len((diag2)) == 1):
      return 1
  
  #Checking for a draw
    drawStateSet = {0,1}
    gameStateSet = set()
    for i in range(0,3):
      for j in range(0,3):
        gameStateSet.add(gameState[i][j])
    if(drawStateSet == gameStateSet):
      return 2
    
  return 0

def possibleMovesWithInd(gameState,val):
  retList = []
  for i in range(0,3):
    for j in range(0,3):
      if gameState[i][j] not in {0,1}:
        tempList = []

        #store the index for the move 
        tempList.append(i)
        tempList.append(j) 

        #apply the move to the gameState
        newState = deepcopy(gameState)
        newState[i][j] = val
        tempList.append(newState)
        retList.append(tempList)
  return retList

def possibleMoves(gameState,val):
  retList = []
  for i in range(0,3):
    for j in range(0,3):
      if gameState[i][j] not in {0,1}:
        newState = deepcopy(gameState)
        newState[i][j] = val
        retList.append(newState)
  return retList

def minimax(gameState,maximizer,val):
  gameStatus = isEndState(gameState)
  if(gameStatus == 1): #game has a winner
    eval = -1 if maximizer else 1
    return eval
  elif(gameStatus == 2): #game is a draw
    return 0
  else:
    #generate possible moves from current state
    moveList = possibleMoves(gameState, val)

    #switch val to the opposite value
    val = 1 if val == 0 else 0
    #if maximizer's turn
    if(maximizer):
      maxEval = -2
      for move in moveList:
        eval = minimax(move,False,val)
        maxEval = max(maxEval,eval)
      return maxEval

    #if minimizer's turn
    else:
      minEval = 2
      for move in moveList:
        eval = minimax(move,True,val)
        minEval = min(minEval,eval)
      return minEval