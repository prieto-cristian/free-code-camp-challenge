##############################################################################
# Birthday Countdown
# Given today's date and a birthday, return the number of days until the
# person's next birthday.
#
# Today's date is given as a string in "YYYY-MM-DD" format, with leading
# zeros, for example: "2026-07-16".
# The birthday is given as a string in "M/D" format, without leading zeros,
# for example: "9/7".
# If today is their birthday, return the number of days until their next
# birthday (not 0).
# Leap years should be accounted for.
#
# 1. days_until_birthday("2026-07-16", "9/7") should return 53.
# 2. days_until_birthday("2026-07-16", "3/22") should return 249.
# 3. days_until_birthday("2026-07-16", "7/16") should return 365.
# 4. days_until_birthday("2024-02-28", "3/1") should return 2.
# 5. days_until_birthday("2023-04-24", "12/30") should return 250.
# 6. days_until_birthday("2024-03-01", "2/29") should return 1460.
# 7. days_until_birthday("2096-03-01", "2/29") should return 2920.
##############################################################################


def days_until_birthday(today, birthday):
    meses = { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30,
              10: 31, 11: 30, 12: 31}
    today = today.split("-")
    today = { "anio": int(today[0]), "mes": int(today[1]),
                     "dia": int(today[2]),}
    birthday = birthday.split("/")
    birthday = {"mes": int(birthday[0]), "dia": int(birthday[1])}

    dias_diferencia = 0
    meses_diferencia = birthday["mes"] - today["mes"]
    mes_actual = today["mes"]
    birthday["anio"] = today["anio"]

    if birthday["mes"] < today["mes"] or (birthday["mes"] == today["mes"]
                                          and birthday["dia"] == today["dia"]):
        meses_diferencia += 12
        birthday["anio"] += 1
        if birthday["mes"] == 2 and birthday["dia"] == 29:
            while birthday["anio"] % 4 != 0 or (birthday["anio"] % 100 == 0
                                                and not birthday["anio"] % 400 == 0):
                meses_diferencia += 12
                birthday["anio"] += 1
    else:
        if birthday["anio"] % 4 == 0 or (birthday["anio"] % 100 == 0
                                                and not birthday["anio"] % 400 == 0):
            dias_diferencia += 1
    while meses_diferencia > 0:
        dias_diferencia += meses[mes_actual]
        meses_diferencia -= 1
        mes_actual += 1
        if mes_actual == 13:
            mes_actual = 1
    dias_diferencia -= today["dia"]
    dias_diferencia += birthday["dia"]
    return dias_diferencia

print(days_until_birthday("2096-03-01", "2/29"))