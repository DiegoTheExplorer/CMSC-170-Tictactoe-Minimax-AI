from copy import deepcopy

# Checks if the game is done at the current state
# 0 if game is not over
# 1 if X wins
# 2 if O wins
# 3 if the game is a draw
def isEndState(gameState):

  #Checking rows and columns for a win
  for i in range(0,3):
    rChk = set([gameState[i][0],gameState[i][1],gameState[i][2]])
    cChk = set([gameState[0][i],gameState[1][i],gameState[2][i]])

    if (len(rChk) == 1):
      for e in rChk:
        if e == 1:
          return 1
        else:
          return 2
    if (len(cChk) == 1):
      for e in rChk:
        if e == 1:
          return 1
        else:
          return 2
  
  #Checking diagonals for a win
    diag1 = set([gameState[0][0],gameState[1][1],gameState[2][2]])
    diag2 = set([gameState[0][2],gameState[1][1],gameState[2][0]])

    if (len((diag1)) == 1):
      for e in diag1:
        if e == 1:
          return 1
        else:
          return 2
    if (len((diag2)) == 1):
      for e in diag2:
        if e == 1:
          return 1
        else:
          return 2
  
  #Checking for a draw
    drawStateSet = {0,1}
    gameStateSet = set()
    for i in range(0,3):
      for j in range(0,3):
        gameStateSet.add(gameState[i][j])
    if(drawStateSet == gameStateSet):
      return 3
    
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

def minimax(gameState, maximizer, val, aiMark):
  currState = isEndState(gameState)
  if (currState == 1):
    eval = 1 if maximizer else -1
    print("**********")
    for row in gameState:
      print(row)
    print("eval: ",eval)
    return eval

  actions = possibleActions(gameState,val)
  if (maximizer):
    maxEval = -2
    for resState in actions:
      val = 1 if val == 0 else 0
      eval = minimax(resState, False, val, aiMark)
      maxEval = max(maxEval,eval)
    return maxEval

  else:
    minEval = 2
    for resState in actions:
      val = 1 if val == 0 else 0
      eval = minimax(resState, True, val, aiMark)
      minEval = min(minEval,eval)
    return minEval