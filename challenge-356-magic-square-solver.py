#######################################################################
# Magic Square Solver
# Given a 3x3 grid with one missing number (represented as 0),
# return the missing number that completes the magic square,
# or "impossible" if no valid number exists.
#
# A magic square is a grid where every row, column, and diagonal adds
# up to the same number.
#
# Tests:
# 1. solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]])
# should return 5.
# 2. solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]])
# should return 4.
# 3. solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]])
# should return "impossible".
# 4. solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]])
# should return 39.
# 5. solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]])
# should return "impossible".
#######################################################################

# [15, 35, 31]
# [43, 27, 11]
# [23, 19, 0]
def solve_magic_square(grid):
    columnas = list(zip(grid[0], grid[1], grid[2]))
    numero_magico = 0
    suma_fila_cero = 0
    for i in range(3):
        if sum(grid[i]) != sum(columnas[i]):
            return "impossible"
        if sum(grid[i]) > numero_magico:
            numero_magico = sum(grid[i])
        if 0 in grid[i]:
            suma_fila_cero = sum(grid[i])
    return numero_magico - suma_fila_cero

print(solve_magic_square([
    [2, 7, 6],
    [9, 0, 1],
    [4, 3, 8]]))
print(solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]))
print(solve_magic_square([
 [8, 1, 6],
 [3, 0, 5],
 [4, 9, 2]
]))
print(solve_magic_square([
 [8, 1, 6],   # 15
 [3, 0, 5],   # 8
 [4, 9, 2]    # 15
]))