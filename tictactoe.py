#Tkinter imports
import tkinter as tk
import tkinter.messagebox as message
import tkinter.font as font

#External library imports
from functools import partial
import random 

#Custom imports
from minimax import *

#Global Variables
turnCount = 1

#UI FUNCTIONS
def disableAllBtns(frame):
  for btn in frame.grid_slaves():
    if (btn['text'] != 'Restart'):
      btn['state'] = 'disabled'
  return

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
    message.showinfo("Game Over","You won! ※\(^o^)/※")
    disableAllBtns(frame)
    return
  elif currState == 2:
    print("GAME DRAW")
    message.showinfo("Game Over","The Game was a draw ¯\(°_o)/¯")
    disableAllBtns(frame)
    return

  #AI minimax start
  mark = 'O' if turnCount % 2 == 0 else 'X'
  val = 0 if mark == 'O' else 1

  #Generate all possible moves for the AI
  moves = possibleMovesWithInd(gameState, val)

  #Find the minimax evaluation for each move
  invVal = 1 if val == 0 else 0
  for move in moves:
    move[2] = minimax(move[2],False,invVal,-2,2)

  #Select the move with the highest minimax evaluation
  bestMove = max(moves, key=lambda x:x[2])
  #AI minimax end

  #apply the move decided by the minimax AI
  bmRow = bestMove[0]
  bmCol = bestMove[1]
  gameState[bmRow][bmCol] = val #update gameState

  moveBtn = frame.grid_slaves(bestMove[0],bestMove[1])#update the ui
  moveBtn[0].config(text=mark,state='disabled')

  #Check if end state
  currState = isEndState(gameState)
  if currState == 1:
    print("COMPUTER WINS")
    message.showinfo("Game Over","The Computer won ( ╥﹏╥) ノシ")
    disableAllBtns(frame)
    return
  elif currState == 2:
    print("GAME DRAW")
    message.showinfo("Game Over","The Game was a draw ¯\(°_o)/¯")
    disableAllBtns(frame)
    return

  turnCount += 1

#INIT FUNCTIONS
#creates a 3x3 grid of buttons and assigns buttonClick to be called when a button is clicked
def initButtons(gameState, root, frame):
  global turnCount

  #Randomly decide if Player or AI goes first
  isPlayerTurn = random.randint(0,1)
  isPlayerTurn = True if isPlayerTurn == 1 else False

  btnFont = font.Font(family='Helvetica', size=26, weight='bold')

  for row in range(0,3):
    for col in range(0,3):
        button = tk.Button(frame,
                          text="", 
                          fg="white", 
                          bg="blue", 
                          font=btnFont,
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

def restartGame(gameState,root,frame):
  global turnCount
  turnCount = 1
  gameState = [[4,5,6],
            [7,8,9],
            [10,11,12]]
  initButtons(gameState,root,frame)

#APP START
root = tk.Tk()
root.title("Tictactoe")
root.resizable(False,False)
frame = tk.Frame(root, width = 600, height = 700)
frame.grid(columnspan = 4, rowspan = 3)
restartBtn = tk.Button(frame,
                      text="Restart")
restartBtn.grid(row = 3, column = 0, sticky="nesw")


#Tictactoe Variables
gameState = [[4,5,6],
            [7,8,9],
            [10,11,12]]
restartBtn.config(comman=partial(restartGame,gameState,root,frame))

initButtons(gameState,root,frame)

root.mainloop()