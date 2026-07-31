#######################################################################
# Morse Code
# Given a Morse code string, return the decoded message using the
# following table:
#
# Code	   Letter Code	Letter
# .-	A	-.	        N
# -...	B	---	        O
# -.-.	C	.--.	    P
# -..	D	--.-	    Q
# .	    E	.-.	        R
# ..-.	F	...	        S
# --.	G	-	        T
# ....	H	..-	        U
# ..	I	...-	    V
# .---	J	.--	        W
# -.-	K	-..-	    X
# .-..	L	-.--	    Y
# --	M	--..	    Z
# Letters are separated by a single space
# Words are separated by three spaces
# Tests:
# 1. decode_morse("--..") should return "Z".
# 2. decode_morse("... --- ...") should return "SOS".
# 3. decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--.")
# should return "FREECODECAMP".
# 4. decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
# should return "HELLO WORLD".
# 5. decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. ---
# .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.
# - .... .   .-.. .- --.. -.--   -.. --- --.")
# should return "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG".
#######################################################################


def decode_morse(code):
    valores_codigos = {".-":"A","-...": "B","-.-.": "C", "-..": "D",".": "E",
                       "..-.": "F", "--.": "G", "....": "H", "..": "I",
                       ".---": "J", "-.-": "K", ".-..": "L", "--": "M",
                       "-.": "N", "---": "O", ".--.": "P", "--.-": "Q",
                       ".-.": "R", "...": "S", "-": "T", "..-": "U",
                       "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
                       "--..": "Z"}
    palabras_codificadas = code.split("   ")
    frase = ""
    for p in palabras_codificadas:
        caracteres = p.split(" ")
        palabra_traducida = ""
        for caracter in caracteres:
            palabra_traducida += valores_codigos[caracter]
        frase += palabra_traducida + " "
    return frase.strip()


def decode_morse1(code):
    valores_codigos = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
                       "..-.": "F", "--.": "G", "....": "H", "..": "I",
                       ".---": "J", "-.-": "K", ".-..": "L", "--": "M",
                       "-.": "N", "---": "O", ".--.": "P", "--.-": "Q",
                       ".-.": "R", "...": "S", "-": "T", "..-": "U",
                       "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
                       "--..": "Z"}
    return " ".join("".join(valores_codigos[caracter] for caracter in palabra.split())
                    for palabra in code.split("   "))