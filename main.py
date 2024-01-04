#Tkinter imports
import tkinter as tk
import tkinter.messagebox as message

#Other imports
from functools import partial
import random 

#User imports
from tttAI import *

#UI FUNCTIONS
def disableAllBtns(frame):
  for btn in frame.grid_slaves():
    btn['state'] = 'disabled'
  return

def buttonClick(self, gameState, root, frame, turnCount, aiMark):

  row = self.grid_info()['row']
  col = self.grid_info()['column']
  mark = 'O' if turnCount % 2 == 0 else 'X'
  #0 is 'O' and 1 is 'X'

  #Mark current button and set as disabled
  self.config(text=mark, state='disabled')
  gameState[row][col] = 0 if mark == 'O' else 1
  turnCount += 1

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

  #Minimax AI Start 
  # print("ai turn")
  mark = "O" if turnCount % 2 == 0 else "X"
  val = 0 if mark == 'O' else 1
  inv = 1 if val == 0 else 0

  actionList = possibleActionsWithInd(gameState,val)
  for action in actionList:
    action[0] = minimax(action[0],False,inv,aiMark)

  aiMove = max(actionList,key=lambda x:x[0])
  gameState[aiMove[1]][aiMove[2]] = val
  currBtn = frame.grid_slaves(aiMove[1],aiMove[2])
  currBtn[0].config(text=mark,state='disabled')
  #Minimax AI end

  #Check if end state
  currState = isEndState(gameState)
  if currState == 2:
    print("COMPUTER WINS")
    disableAllBtns(frame)
    return
  elif currState == 3:
    print("GAME DRAW")
    disableAllBtns(frame)
    return

  turnCount += 1
  return

#INIT FUNCTIONS
#creates a 3x3 grid of buttons and assigns buttonClick to be called when a button is clicked
def initButtons(gameState, root, frame, turnCount, isPlayerTurn, aiMark):

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
        button.config(command= partial(buttonClick, button, gameState, root, frame, turnCount, aiMark))

  aiMark.set("O")
  isPlayerTurn = True #dbg
  #AI does a random move when AI goes first
  if not isPlayerTurn:
    aiMark.set("X")
    rRow = random.randint(0,2)
    rCol = random.randint(0,2)
    rBtn = frame.grid_slaves(rRow,rCol)
    rBtn[0].config(text="X",state='disabled')
    gameState[rRow][rCol] = 1
    turnCount += 1

  return

#APP START
root = tk.Tk()
root.title("Tictactoe")
root.resizable(False,False)
frame = tk.Frame(root, width = 600, height = 600)
frame.grid(columnspan = 3, rowspan = 3)

#Tictactoe Variables
# gameState = [[4,5,0],
#             [1,0,9],
#             [1,11,12]]
gameState = [[4,5,6],
            [7,8,9],
            [10,11,12]]
turnCount = 1
aiMark = tk.StringVar(root)
isPlayerTurn = random.randint(0,1)
isPlayerTurn = True if isPlayerTurn == 1 else False

initButtons(gameState,root,frame,turnCount,isPlayerTurn,aiMark)

root.mainloop()