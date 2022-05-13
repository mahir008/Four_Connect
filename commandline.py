import numpy as np

no_of_rows = 6
no_of_columns = 7


def board_create():
    board = np.zeros((no_of_rows, no_of_columns))
    return board

def piece_drop(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[no_of_rows - 1][col] == 0


def next_open_row(board, col):
    for r in range(no_of_rows):
        if board[r][col] == 0:
            return r



def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
	#check horizontal locations for win
	for c in range(no_of_columns - 3):
		for r in range(no_of_rows):
			if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
				c + 3] == piece:
				return True

	#check ver locations for win
	for c in range(no_of_columns):
		for r in range(no_of_rows - 3):
			if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
				c] == piece:
				return True
	#check pos slope for win
	for c in range(no_of_columns - 3):
		for r in range(no_of_rows - 3):
			if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
				c + 3] == piece:
				return True

	#check neg slope for win
	for c in range(no_of_columns - 3):
		for r in range(3, no_of_rows):
			if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
				c + 3] == piece:
				return True

board = board_create()
print_board(board)
game_over = False
turn = 0

while not game_over:
	#asking player 1
	if turn == 0:
		col = int(input("P1 make selection (0-6):"))

		if is_valid_location(board, col):
			row = next_open_row(board, col)
			piece_drop(board, row, col, 1)

			if winning_move(board, 1):
				print("Player 1 winner !")
				game_over = True



	#asking player 2
	else:
		col = int(input("P2 make selection (0-6):"))

		if is_valid_location(board, col):
			row = next_open_row(board, col)
			piece_drop(board, row, col, 2)

			if winning_move(board, 2):
				print("Player2 Winner")
				game_over = True

	print_board(board)

	turn += 1
	turn = turn % 2