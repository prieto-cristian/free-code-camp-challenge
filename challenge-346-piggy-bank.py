##############################################################################
# Piggy Bank
# Given an object representing a piggy bank, return the total value as a
# string formatted as "$D.CC".
#
# The object may contain any of the following:
#
# Coin	Value
# pennies	$0.01
# nickels	$0.05
# dimes	    $0.10
# quarters	$0.25
#
# Tests:
# 1. piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6})
#   should return "$1.98".
# 2. piggy_bank({"pennies": 1, "nickels": 1, "dimes": 1, "quarters": 1})
#   should return "$0.41".
# 3. piggy_bank({"nickels": 8, "dimes": 6, "quarters": 5})
#   should return "$2.25".
# 4. piggy_bank({}) should return "$0.00".
# 5. piggy_bank({"pennies": 146, "nickels": 11, "dimes": 0, "quarters": 19})
#   should return "$6.76".
##############################################################################
def piggy_bank(coins):
    valores = {"pennies": 0.01, "nickels": 0.05, "dimes": 0.1,
               "quarters": 0.25}
    res = 0
    for coin, value in coins.items():
        res += valores[coin] * value
    coins = f"${res:.2f}"
    return coins

print(piggy_bank({"pennies": 3, "nickels": 5, "dimes": 2, "quarters": 6}))
print(piggy_bank({}))