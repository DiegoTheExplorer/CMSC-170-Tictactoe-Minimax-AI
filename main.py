#Tkinter imports
import tkinter as tk
import tkinter.messagebox as message
import tkinter.filedialog as filedialog

#other imports
from functools import partial
from copy import deepcopy
from collections import deque
import random 
import numpy as np

#TICTACTOE FUNCTIONS
def isWinState(gameState):

  #Checking rows and columns
  for i in range(0,3):
    rChk = set(gameState[i])
    cChk = set(gameState[:,i])

    if ((len(rChk) == 1 or len(cChk) == 1)):
      return True
  
  #Checking diagonals
    diag1 = set([gameState[0,0],gameState[1,1],gameState[2,2]])
    diag2 = set([gameState[0,2],gameState[1,1],gameState[2,0]])

    if (len(set(diag1)) == 1 or len(set(diag2)) == 1):
      return True
  return False

def buttonClick(self, gameState, root, frame, turnCount):

  row = self.grid_info()['row']
  col = self.grid_info()['column']
  mark = 10 if turnCount % 2 == 0 else 20
  #10 is 'O" and 20 is 'X'

  #Mark current button and set as disabled
  self.config(textvariable=mark, state='disabled')
  gameState[row][col] = mark
  turnCount += 1

  #Check if winstate
  if isWinState(gameState):
    print("PLAYER WINS")
    return

  #Put minimax ai 
  mark = "O" if turnCount % 2 == 0 else "X"
  print("ai turn")

  turnDone = False
  while turnDone:
    rRow = random.randint(0,2)
    rCol = random.randint(0,2)
    rBtn = frame.grid_slaves(rRow,rCol)
    print(rBtn)
    if rBtn.menu.cget('status') == 'enabled':
      rBtn.config(textvariable=mark,state='disabled')
      gameState[rRow][rCol] = mark
      turnDone = True
      
  turnCount += 1

  #Check if winstate
  if isWinState(gameState):
    print("COMPUTER WINS")
    return

  turnCount += 1
  return

#INIT FUNCTIONS
#creates a 3x3 grid of buttons and assigns buttonClick to be called when a button is clicked
def initButtons(gameState, root, frame, turnCount, isPlayerTurn):

  for row in range(0,3):
    for col in range(0,3):
        button = tk.Button(frame,
                          textvariable=tk.StringVar(""), 
                          fg="black", 
                          bg="blue", 
                          font="Helvetica",
                          width = 10, 
                          height = 5)
        button.grid(row = row, column = col, sticky="nesw")
        button.config(command= partial(buttonClick, button, gameState, root, frame, turnCount))

  if not isPlayerTurn:
    rRow = random.randint(0,2)
    rCol = random.randint(0,2)
    rBtn = frame.grid_slaves(rRow,rCol)
    print(rBtn)
    rBtn.config(text="X",state='disabled')
    gameState[rRow][rCol] = 20
    turnCount += 1

  return

#APP START
root = tk.Tk()
root.title("Tictactoe")
root.resizable(False,False)
frame = tk.Frame(root, width = 600, height = 600)
frame.grid(columnspan = 3, rowspan = 3)

#Tictactoe Variables
gameState = np.array([[1,2,3],[4,5,6],[7,8,9]])
turnCount = 1
isPlayerTurn = random.randint(0,1)
isPlayerTurn = True if isPlayerTurn == 1 else False

initButtons(gameState,root,frame,turnCount,isPlayerTurn)

root.mainloop()