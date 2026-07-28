#######################################################################
# Contrast Rating 1
# Given a contrast ratio and a boolean indicating whether the text is
# large, return the WCAG rating using the following table:
#
# Rating  | Normal Text | Large Text
# "AAA"	      7.0+	       4.5+
# "AA"	      4.5+	       3.0+
# "Fail"	  below 4.5	   below 3.0
#
# Tests:
# 1. get_contrast_rating("7.5", False) should return "AAA".
# 2. get_contrast_rating("4.8", False) should return "AA".
# 3. get_contrast_rating("4.2", False) should return "Fail".
# 4. get_contrast_rating("4.5", True) should return "AAA".
# 5. get_contrast_rating("3.0", True) should return "AA".
# 6. get_contrast_rating("2.7", False) should return "Fail".
#######################################################################


def get_contrast_rating(ratio, is_large_text):
    ratio = float(ratio)
    limites = {False: [4.5, 7], True: [3, 4.5]}
    if ratio < limites[is_large_text][0]:
        return "Fail"
    elif ratio < limites[is_large_text][1]:
        return "AA"
    else:
        return "AAA"
