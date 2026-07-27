#######################################################################
# Pronic Number
# Given a number, determine whether it is a pronic number.
#
# A pronic number is the product of two consecutive integers.
# For example, 6 is pronic because 2 * 3 = 6.
#
# Tests:
# 1. is_pronic(6) should return True.
# 2. is_pronic(15) should return False.
# 3. is_pronic(12) should return True.
# 4. is_pronic(132) should return True.
# 5. is_pronic(80) should return False.
# 6. is_pronic(0) should return True.
#######################################################################


def is_pronic(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        i = 1
        pronic = False
        while not pronic and (i * (i + 1)) <= n:
            if (i * (i + 1)) == n:
                pronic = True
            i += 1
    return pronic

print(is_pronic(6))