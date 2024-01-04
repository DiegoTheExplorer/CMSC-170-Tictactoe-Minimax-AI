from minimax import *

gameStates = [
  [#X turn
    [1,4,1],
    [0,1,8],
    [0,10,0],
  ],
  [#Draw
    [1,0,1],
    [0,1,1],
    [0,1,0],
  ],
  [#Draw
    [0,1,1],
    [1,1,0],
    [0,0,1]
  ],
  [#Win
    [1,0,5],
    [1,0,6],
    [7,0,1]
  ],
  [#Lose
    [1,1,1],
    [0,1,0],
    [0,0,1]
  ]
]

# for state in gameStates:
#   print("********************")
#   for i in range(0,3):
#     print(state[i])
#   print(minimax(state))

# for moves1 in possibleMoves(gameStates[0],1):
#   print("*******************************************")
#   for moves2 in possibleMoves(moves1,0):
#     print(moves2[0])
#     print(moves2[1])
#     print(moves2[2])