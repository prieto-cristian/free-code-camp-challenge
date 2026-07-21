##############################################################################
# Dice Odds
# Given a number of six-sided dice to roll and a target sum, return the odds
# of rolling that sum as a string in the format "1 in X".
# The number of dice will be between 1 and 6.
# The target sum is always achievable with the given number of dice.
# Round "X" to the nearest whole number.
# Tests:
# 1. get_odds(1, 5) should return "1 in 6".
# 2. get_odds(2, 4) should return "1 in 12".
# 3. get_odds(3, 10) should return "1 in 8".
# 4. get_odds(4, 7) should return "1 in 65".
# 5. get_odds(5, 26) should return "1 in 111".
# 6. get_odds(6, 35) should return "1 in 7776".
##############################################################################

# RESTAR DICE Y COMPARAR AL FINAL SI TARGET ES CERO ENTONCES ES UNA COMBINACION POSIBLE
def get_odds(dice, target):
    # 1. Tu algoritmo de conteo como función interna
    def contar_combinaciones(d, t):
        if d == 0:
            return 1 if t == 0 else 0
        if t < 0:  # Pequeña optimización para no seguir sumando si ya nos pasamos
            return 0

        combinaciones = 0
        for i in range(1, 7):
            combinaciones += contar_combinaciones(d - 1, t - i)
        return combinaciones

    # 2. Calculamos los casos favorables con tu algoritmo
    favorables = contar_combinaciones(dice, target)

    # 3. Calculamos los casos totales (6^dice)
    totales = 6 ** dice

    # 4. Calculamos X y redondeamos al entero más cercano
    x = round(totales / favorables)

    # 5. Retornamos el string formateado
    return f"1 in {x}"
print(get_odds(4, 7))