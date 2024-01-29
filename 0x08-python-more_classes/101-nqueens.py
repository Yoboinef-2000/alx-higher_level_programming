#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    """Check if placing a queen at board[row][col] is safe."""
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N):
    """Recursive function to solve N-Queens problem."""
    if col >= N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, N) or res
            board[i][col] = 0  # Backtrack if placing a queen doesn't lead to a solution

    return res

def print_solution(board, N):
    """Print the N-Queens solution."""
    solution = []
    for i in range(N):
        row = ["Q" if board[i][j] == 1 else "." for j in range(N)]
        solution.append("".join(row))
    print("\n".join(solution))
    print()

def nqueens_solver(N):
    """Main function to solve N-Queens problem."""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]

    if not solve_nqueens(board, 0, N):
        print(f"No solution for N = {N}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens_solver(sys.argv[1])

