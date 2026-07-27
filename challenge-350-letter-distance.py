#######################################################################
# Letter Distance
# Given two strings of equal length, return the sum of the shortest
# distances between each pair of characters.
#
# The input will only contain lowercase letters
# The alphabet is treated as a circle,
# so the distance between a and z is 1.
#
# Tests:
# 1. letter_distance("abc", "bcd") should return 3.
# 2. letter_distance("abc", "xyz") should return 9.
# 3. letter_distance("encrypt", "decrypt") should return 10.
# 4. letter_distance("algorithm", "codeblock") should return 43.
# 5. letter_distance("lobster", "penguin") should return 47.
# 6. letter_distance("alligator", "crocodile") should return 55.
#######################################################################

def letter_distance(str1, str2):
    distancia = 0
    for i in range(len(str1)):
        distancia_directa = abs(ord(str1[i]) - ord(str2[i]))
        distancia_reversa = 26 - distancia_directa
        distancia += min(distancia_directa, distancia_reversa)
    return distancia

print(letter_distance("algorithm", "codeblock"))
