##############################################################################
# Game Theory
# Given two equal length strings representing two players' strategies
# for a game, return the scores as an array [player1, player2].
#
# The given strings will only contain one of two letters:
# "C" (cooperate) or "D" (defect).
#
# Each character represents one round, scored as follows:
#   If both players cooperate, each scores 3.
#   If both players defect, each scores 1.
#   If one player defects and the other cooperates, the defector scores 5 and
#   the cooperator scores 0.
#
# Tests:
# 1. play_game("CCCC", "CCCC") should return [12, 12].
# 2. play_game("DDDD", "DDDD") should return [4, 4].
# 3. play_game("CCDD", "CDDD") should return [5, 10].
# 4. play_game("CCCDCDCCCDDC", "CCDDCDCDDCCD") should return [24, 34].
# 5. play_game("DDCCDDDDCDDCDDDCDD", "CCDCCCDCCCDCCCCDCC")
# should return [66, 21].
##############################################################################
def play_game(p1, p2):
    res = [0,0]
    for i in range(len(p1)):
        if p1[i] == "C" == p2[i]:
            res[0] += 3
            res[1] += 3
        elif p1[i] == "D" == p2[i]:
            res[0] += 1
            res[1] += 1
        elif p1[i] == "D":
            res[0] += 5
        else:
            res[1] += 5
    return res

print(play_game("CCCC", "CCCC"))