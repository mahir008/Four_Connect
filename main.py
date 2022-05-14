import numpy as np #python library for matrix array
import random #uniform selection for range
import pygame #python game library
import sys #system-specific parameters and functions
import math #import math  give access to the mathematical functions

WHITE = (255, 255, 255) #board
BLACK = (0, 0, 0)  #background
RED = (255, 0, 0) #piece player_1
YELLOW = (255, 255, 0) #piece player 2

no_of_rows = 6
no_of_columns = 7


def board_create(): #creating board
    board = np.zeros((no_of_rows, no_of_columns))
    return board


def piece_drop(board, row, col, piece): #creating the the circular pieces to be dropped
    board[row][col] = piece


def is_valid_location(board, col): #checking to see if the pieces dropped by player is in a valid location
    return board[no_of_rows - 1][col] == 0


def next_open_row(board, col): #checking the next no of rows to be dropped
    for r in range(no_of_rows):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))

#checking win locations
def winner_move(board, piece):
    # Checking  horizontal locations for to win the game
    for c in range(no_of_columns - 3):
        for r in range(no_of_rows):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Checking vertical locations for win the game
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


#initializting graphical interface  using pygame
def draw_board(board):
    for c in range(no_of_columns):
        for r in range(no_of_rows):
            pygame.draw.rect(screen, WHITE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(no_of_columns):
        for r in range(no_of_rows):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


board = board_create()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 100

width = no_of_columns * SQUARESIZE
height = (no_of_rows + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("Arial", 70)
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # print(event.pos)
 # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = next_open_row(board, col)
                    piece_drop(board, row, col, 1)

                    if winner_move(board, 1):
                        label = myfont.render("PLAYER 1 WINNER", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True


            # # Ask for Player 2 Input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = next_open_row(board, col)
                    piece_drop(board, row, col, 2)

                    if winner_move(board, 2):
                        label = myfont.render("PLAYER 2 WINNER", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
