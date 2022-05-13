import numpy as np
import random
import pygame
import sys
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

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


def winner_move(board, piece):
    # Check horizontal locations for win
    for c in range(no_of_columns - 3):
        for r in range(no_of_rows):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(no_of_columns):
        for r in range(no_of_rows - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(no_of_columns - 3):
        for r in range(no_of_rows - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(no_of_columns - 3):
        for r in range(3, no_of_rows):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True
