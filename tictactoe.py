#Tkinter imports
import tkinter as tk
import tkinter.messagebox as message

#Other imports
from functools import partial
import random 

#Global Variables
turnCount = 1

#UI FUNCTIONS
def disableAllBtns(frame):
  for btn in frame.grid_slaves():
    btn['state'] = 'disabled'
  return

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

def buttonClick(self, gameState, root, frame):
  global turnCount
  row = self.grid_info()['row']
  col = self.grid_info()['column']
  mark = 'O' if turnCount % 2 == 0 else 'X'

  #Mark current button and set as disabled
  self.config(text=mark, state='disabled')
  gameState[row][col] = 0 if mark == 'O' else 1
  turnCount = turnCount + 1

  #Check if end state
  currState = isEndState(gameState)
  if currState == 1:
    print("PLAYER WINS")
    disableAllBtns(frame)
    return
  elif currState == 3:
    print("GAME DRAW")
    disableAllBtns(frame)
    return

#INIT FUNCTIONS
#creates a 3x3 grid of buttons and assigns buttonClick to be called when a button is clicked
def initButtons(gameState, root, frame, isPlayerTurn):
  global turnCount
  for row in range(0,3):
    for col in range(0,3):
        button = tk.Button(frame,
                          text="", 
                          fg="black", 
                          bg="blue", 
                          font="Helvetica",
                          width = 10, 
                          height = 5)
        button.grid(row = row, column = col, sticky="nesw")
        button.config(command= partial(buttonClick, button, gameState, root, frame))

  #AI does a random move when AI goes first
  if not isPlayerTurn:
    rRow = random.randint(0,2)
    rCol = random.randint(0,2)
    rBtn = frame.grid_slaves(rRow,rCol)
    rBtn[0].config(text="X",state='disabled')
    gameState[rRow][rCol] = 1
    turnCount = turnCount + 1


#APP START
root = tk.Tk()
root.title("Tictactoe")
root.resizable(False,False)
frame = tk.Frame(root, width = 600, height = 600)
frame.grid(columnspan = 3, rowspan = 3)

#Tictactoe Variables
gameState = [[4,5,6],
            [7,8,9],
            [10,11,12]]
isPlayerTurn = random.randint(0,1)
isPlayerTurn = True if isPlayerTurn == 1 else False

initButtons(gameState,root,frame,isPlayerTurn,)

root.mainloop()