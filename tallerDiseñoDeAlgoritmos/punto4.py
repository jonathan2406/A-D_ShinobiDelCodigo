#punto 4 

def is_valid(matrix):
    
    for i in range(3):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(3))
        if row_sum != 16 or col_sum != 16:
            return False

    return True

def solve_sudoku(matrix, row, col):
    if row == 3:
        return is_valid(matrix)

    next_row = row + 1 if col == 2 else row
    next_col = (col + 1) % 3

    if matrix[row][col] != 0:
        return solve_sudoku(matrix, next_row, next_col)

    for num in range(1, 10):
        matrix[row][col] = num
        if solve_sudoku(matrix, next_row, next_col):
            return True
        matrix[row][col] = 0

    return False

def print_matrix(matrix):
    for row in matrix:
        print(row)

def solve_sudoku_puzzle():
    
    puzzle = [
        [3, 6, 7],
        [0, 7, 0],
        [8, 0, 5]
    ]

    if solve_sudoku(puzzle, 0, 0):
        print("Solución encontrada:")
        print_matrix(puzzle)
    else:
        print("No se encontró solución")


solve_sudoku_puzzle()

