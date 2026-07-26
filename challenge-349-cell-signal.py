#######################################################################
# Cell Signal
# Given a grid containing three cell tower readings, determine the
# location of the phone.
#
# 1. Each cell in the grid is either 0 (no tower) or a positive integer
# representing the number of cells to the phone, measured in a straight
# line: horizontal, vertical, or diagonal.
#
# 2. Return the [row, col] of the cell that is the correct number of
# cells from all three towers.
#
# 3.There is always exactly one solution.
#
# Tests:
# 1. find_signal([[0, 0, 1], [0, 1, 0], [0, 0, 1]]) should return[1, 2]
# 2. find_signal([[0, 2, 0], [1, 0, 0], [0, 0, 1]]) should return[2, 1]
# 3. find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0,0,0,1]])
# should return [2, 2].
# 4. find_signal([[0, 3, 0, 0, 0], [0, 0, 0, 0, 2], [0, 0, 0, 0, 0]
#   , [4, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) should return [3, 4].
# 5. find_signal([[3, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]
# , [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]
# , [0, 2, 0, 0, 0, 2]]) should return [3, 3].

# Alternativas inventadas: sumar filas y columnas
# coincidencias
# ir fila por fila y saltar cuando encuentre una señal. En la primera senial que encuentre saltar.
#######################################################################
# [0, 2, 0] 0 1 | 2 1 | 0 2
# [1, 0, 0] 1 0
# [0, 0, 1] 2 2 | 1 2 | 2 1
# 2 1

# [0, 0, 1] 0 2 | 1 2 | 0 3
# [0, 1, 0]
# [0, 0, 1] 2 2 | 1 2 | 2 1
# [1, 2]


def find_signal(grid):
    """Fijarse en la primera y ultima fila"""
    combinaciones = {}
    tamanio = len(grid[0])
    for fila, row in enumerate(grid):
        distancia_antena = max(row)
        if distancia_antena > 0:
            columna = row.index(distancia_antena)
            for f in range(fila - distancia_antena, fila + distancia_antena + 1, distancia_antena):
                if 0 <= f < tamanio:
                    for c in range(columna - distancia_antena, columna + distancia_antena + 1, distancia_antena):
                        combinacion = (f, c)
                        if combinacion == (fila, columna) or c < 0 or c > tamanio:
                            continue
                        elif not combinacion in combinaciones:
                            combinaciones[combinacion] = 1
                        else:
                            combinaciones[combinacion] += 1
    return list(max(combinaciones, key=combinaciones.get))
print(find_signal([[0, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 1]]))


# [0, 2] |
# [3, 3]
# [0, 4]

# [0, 0, 2, 0] | 0 2
# [0, 0, 0, 0]
# [2, 0, 0, 0]
# [0, 0, 0, 1]