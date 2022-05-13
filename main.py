import numpy as np

 def create_board(board,col):
     board = np.zeros((6,7))
     return board


 def pieces_to_be_dropped():
 pass


 def is_no_in_valid_location():
     pass

 def get_next_open_row():
 pass


 board = create_board()
 game_over = False
 turn=0
 while not game_over:
     # Ask for player 1 input
 if turn == 0:
     col= int(input("Player 1 make your selection (0-6):"))

     #ask for player 2 input
 else:
     col = int(input("Player 2 make your selection (0-6):"))

                     turn +=1
                     turn= turn % 2