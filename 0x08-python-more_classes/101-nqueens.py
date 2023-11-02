#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def is_safe(board, row, col):
    """Check if it's safe to place a queen at the given position."""
    # Check the row to the left
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def recursive_solve(board, col):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        col (int): The current working column.
    Returns:
        solutions (list): A list of lists of solutions.
    """
    if col == len(board):
        solutions.append(get_solution(board))
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 'Q'
            recursive_solve(board, col + 1)
            board[i][col] = ' '

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for c in range(len(board)):
        for r in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
    return solution

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = []
    recursive_solve(board, 0)

    for sol in solutions:
        print(sol)
