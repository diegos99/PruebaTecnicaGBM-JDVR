import random

G = 3 # Total gran premios
pilotos_id = [32,24,35,54,76,23,87,95,15,18,14,65,78,66,90] # Identificador unico de cada piloto
P = len(pilotos_id) # Total pilotos
SP1 = [[1,2,3,4,5,6,7,8], [10,8,6,5,4,3,2,1]] # Sistema de puntaje 1
SP2 = [[1,2,3,4,5,6,7,8,9,10], [25,18,15,12,10,8,6,4,2,1]] # Sistema de puntaje 2
puntos_por_carrera = []

# Inputs
print("----------------------INPUTS----------------------")
print("Total gran premios: ", G)
print("Total pilotos es: ", P)
print("Id's. Pilotos participantes: ", pilotos_id, "\n")
print("Sistema de puntajes 1: ", SP1[0], "\n                       ", SP1[1])
print("Sistema de puntajes 2: ", SP2[0], "\n                       ", SP2[1])

# Recibe como parámetro la posicion obtenida (entero positivo) al final de la carrera y asigna un punteo según el sistema de puntuación
# Devuelve un entero positivo, el cual representa los puntos obtenidos por el piloto al finalizar la carrera
def AsignarPunteoSP1(posicion):
    if posicion > 8:
        return 0
    else:
        return SP1[1][posicion-1]
# Recibe como parámetro la posicion obtenida (entero positivo) al final de la carrera y asigna un punteo según el sistema de puntuación
# Devuelve un entero positivo, el cual representa los puntos obtenidos por el piloto al finalizar la carrera
def AsignarPunteoSP2(posicion):
    if posicion > 10:
        return 0
    else:
        return SP2[1][posicion-1]

# Recibe valores enteros positivos. Donde G es el total de gran premios; y P el total de pilotos en la temporada
# no posee return pero imprime en pantalla los resultados de cada carrera (imprime array por array)
def SimulacionCarreras(G, P):
    # Ciclo For para simular cada carrera/gran premio
    for gran_premio in range(1,G+1):
        print("GRAN PREMIO NO.",gran_premio)
        parrilla = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # Dado a que son 15 pilotos, hay 15 posiciones en la parrilla inicial.
        resultados_gran_premio = [] # Almacena las posiciones de la carrera

        # Ciclo For para simular la posicion obtenida de cada piloto al finalizar la carrera y 
        # asignarle punteo en cada tipo de sistema de puntuación
        for no_piloto in range(P):
            posicion_obtenida = random.choice(parrilla)
            print('Piloto:', pilotos_id[no_piloto],'Posicion', posicion_obtenida)
            if gran_premio > 1:
                puntos_por_carrera[0][no_piloto][1] = puntos_por_carrera[0][no_piloto][1] + AsignarPunteoSP1(posicion_obtenida)
                puntos_por_carrera[0][no_piloto][2] = puntos_por_carrera[0][no_piloto][2] + AsignarPunteoSP2(posicion_obtenida)
            else:
                resultados_gran_premio.append([pilotos_id[no_piloto], AsignarPunteoSP1(posicion_obtenida), AsignarPunteoSP2(posicion_obtenida)])
                puntos_por_carrera.append(resultados_gran_premio)
            parrilla.remove(posicion_obtenida)

SimulacionCarreras(G, P)

# OUTPUTS
# Muestra en consola los punteos finales de cada piloto. La primera columna detalla el id del piloto, 
# la 2da columna muestra el punteo final en el Sistema de punteo 1, y la 3ra columna muestra el punteo final en el sistema de punteo 2.
print("\n----------------------OUTPUTS----------------------")
def VisualizarPunteosFinales():
    print("PUNTEOS AL FINAL DE TEMPORADA (sistema de puntuación 1 y 2)")
    for item in range(P):
        print(puntos_por_carrera[0][item])

VisualizarPunteosFinales()

# Campeon(es) mundiales Sistema de puntuación 1 y 2
def ResultadosSP12(sistema_p):
    if sistema_p == 1:
        print("CAMPEON(ES) DEL MUNDO - SISTEMA PUNTUACIÓN", sistema_p)
        DeteccionGanador(sistema_p)
    elif sistema_p == 2:
        print("CAMPEON(ES) DEL MUNDO - SISTEMA PUNTUACIÓN", sistema_p)
        DeteccionGanador(sistema_p)
    else:
        print("SISTEMA DE PUNTUACION NO VALIDO")

def DeteccionGanador(sistema_p):
    resultados_finales = []
    ganadores = []

    for item in range(P):
        resultados_finales.append(puntos_por_carrera[0][item][sistema_p])
    valor_max = max(resultados_finales)
    for item in range(P):
        if puntos_por_carrera[0][item][sistema_p] == valor_max:
            ganadores.append(puntos_por_carrera[0][item][0])
    print(ganadores)

ResultadosSP12(1) # Sistema puntuación 1
ResultadosSP12(2) # Sistema puntuación 2