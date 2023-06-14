from tictactoe import initial_state,player,actions,result,min_value,max_value,terminal

import math

X = "X"
O = "O"
EMPTY = None

board = initial_state()
plays = []

for i in actions(board):
    row,col = i[0] , i[1] , 5
    print(row,col) 


