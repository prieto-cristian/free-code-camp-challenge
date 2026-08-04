#######################################################################
# Golf Handicap Calculator
# Given an array of golf scores and a corresponding array of course
# par values, return the golfer's handicap index using the following
# method:
#
# Calculate the differential for each round by subtracting the par
# from the score, then return the average of all differentials rounded
# to one decimal place.
#
# Tests:
# 1. calculate_handicap([72, 72, 72], [72, 72, 72]) should return 0.
# 2. calculate_handicap([80, 76, 78, 78], [72, 72, 72, 72]) should return 6.
# 3. calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36]) should return 8.3.
# 4. calculate_handicap([85, 80, 76, 79, 82], [72, 72, 72, 71, 71]) should return 8.8.
# 5. calculate_handicap([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37]) should return 11.7.
#######################################################################
def calculate_handicap_original(scores, pars):
    """Solucion original planteada. No pasa el caso 3"""
    return round((sum(scores) - sum(pars)) / len(scores),2)

def calculate_handicap(scores, pars):
    """El challenge debe estar hecho en JS porque el redondeo del caso
    3 no pasa (redondea para abajo)"""
    media = (sum(scores) - sum(pars)) / len(scores)
    if media == 0:
        return 0
    else:
        if round(round(media, 2) % round(media, 1), 2) == 0.05:
            media += 0.01
    return round(media,1)

print(calculate_handicap([72, 72, 72], [72, 72, 72]))