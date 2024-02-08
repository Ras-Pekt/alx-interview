#!/usr/bin/python3
"""a program that solves the N queens problem"""
from sys import argv, exit


def is_safe(board, row, col):
    """
    Check if there is a queen
    in the same column or diagonals
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    finds all possible solutions for a board size N
    """
    solutions = []

    def backtrack(row, board):
        """
        add the solution to the list
        """
        if row == N:
            solution_coordinates = []
            for i in range(N):
                solution_coordinates.append([i, board[i]])
            solutions.append(solution_coordinates)
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)

    board = [-1] * N
    backtrack(0, board)
    return solutions


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)
