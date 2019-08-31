import sys, random

opcion_jugador = sys.argv[1] # opción del jugador
# Elegir la opción al azar entre tres numeros 1: piedra, 2: papel, 3: tijera
opcion_computador = random.randint(1,3)

if opcion_jugador != 'piedra' and opcion_jugador != 'papel' and opcion_jugador != 'tijera':
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    sys.exit()
else:
    if (opcion_computador == 1 ):
        opcion_computador = 'piedra'
    elif opcion_computador == 2:
        opcion_computador = 'papel'
    else:
        opcion_computador = 'tijera'
    print("Computador juega {}".format(opcion_computador))
    if opcion_jugador ==  opcion_computador:
        print("Empataste")
    elif ((opcion_jugador == "piedra" and opcion_computador == "tijera")
           or (opcion_jugador == "tijera" and opcion_computador == "papel")
           or (opcion_jugador == "papel" and opcion_computador == "piedra")):
        print("Ganaste")
    else:
        print("Perdiste")
