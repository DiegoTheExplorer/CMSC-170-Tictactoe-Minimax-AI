from copy import deepcopy

#Checks if the game is done at the current state
#Game is not over = 0
#Game has a winner = 1
#Game is a draw = 2
def isEndState(gameState):

  #Checking rows and columns for a win
  for i in range(0,3):
    rChk = set(gameState[i])
    cChk = set(gameState[:,i])

    if ((len(rChk) == 1 or len(cChk) == 1)):
      return 1
  
  #Checking diagonals for a win
    diag1 = set([gameState[0,0],gameState[1,1],gameState[2,2]])
    diag2 = set([gameState[0,2],gameState[1,1],gameState[2,0]])

    if (len(set(diag1)) == 1 or len(set(diag2)) == 1):
      return 1
  
  #Checking for a draw
    drawStateSet = {0,1}
    gameStateSet = set()
    for i in range(0,3):
      for j in range(0,3):
        gameStateSet.add(gameState[i,j])
    if(drawStateSet == gameStateSet):
      return 2
    
  return 0

def possibleActions(gameState, val):

  actionList = []
  for i in range(0,3):
    for j in range(0,3):
      if (gameState[i][j] not in (0,1)):
        newState = deepcopy(gameState)
        newState[i][j] = val
        actionList.append(newState)

  return actionList

def possibleActionsWithInd(gameState, val):
  actionList = []
  for i in range(0,3):
    for j in range(0,3):
      if (gameState[i][j] not in (0,1)):
        newState = deepcopy(gameState)
        newState[i][j] = val
        actionList.append([newState,i,j])
  return actionList

def minimax(gameState, maximizer, val):
  currState = isEndState(gameState)
  if (currState == 1):
    eval = -1 if maximizer else 1
    return eval
  elif (currState == 2):
    return 0

  actions = possibleActions(gameState,val)
  if (maximizer):
    maxEval = float("-inf") #m
    for resState in actions:
      val = 1 if val == 0 else 0
      eval = minimax(resState, False, val)
      maxEval = max(maxEval,eval)
      return maxEval

  else:
    minEval = float("inf") #m
    for resState in actions:
      val = 1 if val == 0 else 0
      eval = minimax(resState, True, val)
      minEval = min(minEval,eval)
      return minEval