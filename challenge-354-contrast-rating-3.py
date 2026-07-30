#######################################################################
# Contrast Rating 3
# Given two arrays representing RGB values and a boolean indicating
# whether the text is large, return the WCAG contrast rating using
# the following method:
#
# First, convert each RGB value to relative luminance:
#
# Divide each channel [R, G, B] by 255 to get a value between 0 and 1
# Apply the gamma correction formula to each channel:
# If the channel value is less than or equal to 0.04045: channel /12.92
# Otherwise: ((channel + 0.055) / 1.055) ^ 2.4
# Calculate luminance: 0.2126 * R + 0.7152 * G + 0.0722 * B
# Then, calculate the contrast ratio by adding 0.05 to each luminance
# value, then dividing the lighter one by the darker one.
# The lighter one will always be the first argument.
#
# Return the rating based on the contrast ratio using the
# following table:
#
# Rating	Normal Text	Large Text
# "AAA"	    7.0+	    4.5+
# "AA"	    4.5+	    3.0+
# "Fail"	below 4.5	below 3.0
#
# Tests:
# 1. get_contrast_rating([255, 255, 255], [0, 0, 0], False)
# should return "AAA".
# 2. get_contrast_rating([215, 188, 188], [55, 55, 55], False)
# should return "AA".
# 3. get_contrast_rating([143, 144, 210], [46, 47, 61], False)
# should return "Fail".
# 4. get_contrast_rating([167, 167, 210], [53, 10, 53], True)
# should return "AAA".
# 5. get_contrast_rating([135, 147, 155], [60, 70, 90], True)
# should return "AA".
# 6. get_contrast_rating([125, 210, 195], [105, 130, 90], True)
# should return "Fail".
#######################################################################


def get_contrast_rating(rgb1, rgb2, is_large_text):
    for index in range(len(rgb1)):
        rgb1[index] /=  255
        rgb2[index] /= 255
        if rgb1[index] <= 0.04045:
            rgb1[index] = rgb1[index] / 12.92
        else:
            rgb1[index] = ((rgb1[index] + 0.055) / 1.055) ** 2.4
        if rgb2[index] <= 0.04045:
            rgb2[index] = rgb2[index] / 12.92
        else:
            rgb2[index] = ((rgb2[index] + 0.055) / 1.055) ** 2.4
    lighter = (0.2126 * rgb1[0] + 0.7152 * rgb1[1] + 0.0722 * rgb1[2]) + 0.05
    darker = (0.2126 * rgb2[0] + 0.7152 * rgb2[1] + 0.0722 * rgb2[2]) + 0.05
    limites = {True: (3, 4.5), False: (4.5,7)}
    ratio = lighter / darker
    if ratio < limites[is_large_text][0]:
        return "Fail"
    elif ratio < limites[is_large_text][1]:
        return "AA"
    else:
        return "AAA"

print(get_contrast_rating([215, 188, 188], [55, 55, 55], False))
print(get_contrast_rating([135, 147, 155], [60, 70, 90], True))