"""
Un hincha de fútbol desea conocer la cantidad de puntos que su equipo lleva acumulados en el campeonato, para ello recibe cada semana la
información de la cantidad total de partidos, desde el inicio del campeonato, que el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos.

"""
partidos_ganados = int(input('Cuantos partidos se ganaron: '))
partidos_perdiero = int(input('Cuantos partidos se perdieron: '))
partidos_empataron = int(input('Cuantos partidos se empataron: '))

puntos_1 = partidos_ganados * 3

total_puntos = puntos_1 + partidos_empataron

total_partidos = partidos_empataron + partidos_ganados + partidos_perdiero

print('El total de puntos acumulados es de ', total_puntos, ' en ', total_partidos, ' partidos jugados')