#######################################################################
# Spoken Duration
# Given a number of seconds, return the duration in spoken English.
#
# Break the duration into hours, minutes, and seconds.
# Skip any zero values.
# Use singular or plural as appropriate ("1 hour", "2 hours").
# If present, join the last two units with "and", and the second and \
# third to last units with a comma ("1 hour, 2 minutes and 3 seconds").
#
# Tests:
# 1. get_spoken_duration(3723) should return "1 hour, 2 minutes and 3
# seconds".
# 2. get_spoken_duration(7295) should return "2 hours, 1 minute and 35
# seconds".
# 3. get_spoken_duration(8521) should return "2 hours, 22 minutes and 1
# second".
# 4. get_spoken_duration(435) should return "7 minutes and 15 seconds".
# 5. get_spoken_duration(14455) should return "4 hours and 55 seconds".
# 6. get_spoken_duration(72000) should return "20 hours".
# 7. get_spoken_duration(1) should return "1 second".
#######################################################################
# seg min horas
def get_spoken_duration(seconds):
    lista_duracion = []
    palabras = ["second", "minute", "hour"]
    separadores = [" and ", ", "]
    i = 0
    separador = 0
    mensaje = ""
    while seconds % 60 >= 0 and seconds != -1:
        lista_duracion.append(seconds % 60)
        seconds = seconds // 60
        if seconds == 0:
            seconds = -1
    for t in lista_duracion:
        if t == 0:
            i += 1
            continue
        if t > 1:
            palabras[i] += "s"
        tiempo = f"{t} {palabras[i]}"
        if separador != 0:
            tiempo = tiempo + separadores[separador -1]
        mensaje = tiempo + mensaje
        i += 1
        separador += 1
    return mensaje

def get_spoken_duration1(seconds):
    horas = seconds // 3600
    seconds = seconds % 3600
    minutos = seconds // 60
    seconds = seconds % 60

    partes = []
    if horas > 0:
        partes.append(f"{horas} hour{"s" if horas > 1 else ""}")
    if minutos > 0:
        partes.append(f"{minutos} minute{"s" if minutos > 1 else ""}")
    if seconds > 0:
        partes.append(f"{seconds} second{"s" if seconds > 1 else ""}")

    if len(partes) == 1:
        return partes[0]
    elif len(partes) == 2:
        return "and".join(partes)
    else:
        return ", ".join(partes[:2]) + " and " + partes[-1]
