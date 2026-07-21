##############################################################################
# Elevator Stops
# Given a number for the current floor of an elevator and an array of
# requested floors, return an array of the order the elevator should visit
# them to minimize number of floors traveled.
#
# If tied, go down first
# Floors with a request must be visited when the elevator first passes them
# Tests:
# 1. elevator_stops(5, [2, 8, 3, 9]) should return [3, 2, 8, 9].
# 2. elevator_stops(6, [2, 10, 8, 3, 1, 9]) should return [8, 9, 10, 3, 2, 1].
# 3. elevator_stops(1, [4, 8, 3, 6, 9]) should return [3, 4, 6, 8, 9].
# 4. elevator_stops(12, [6, 10, 7, 3, 1, 4]) should return [10, 7, 6, 4, 3, 1].
# 5. elevator_stops(11, [2, 8, 23, 5, 12, 10, 6, 9, 19]) should return [10, 9, 8, 6, 5, 2, 12, 19, 23].
##############################################################################

def elevator_stops(current_floor, stops):
    distancia_piso_arriba = current_floor
    distancia_piso_abajo = current_floor
    current_floor = []
    while len(stops) > 0:
        distancia_piso_abajo -= 1
        distancia_piso_arriba += 1
        if stops.count(distancia_piso_abajo) == 1:
            current_floor.append(stops.pop(stops.index(distancia_piso_abajo)))
            distancia_piso_arriba = distancia_piso_abajo
        if stops.count(distancia_piso_arriba) == 1:
            current_floor.append(stops.pop(stops.index(distancia_piso_arriba)))
            distancia_piso_abajo = distancia_piso_arriba
    return current_floor

print(elevator_stops(6, [2, 10, 8, 3, 1, 9]))