import sys

numero_uno = int(sys.argv[1]) # opción uno  5
numero_dos = int(sys.argv[2]) # opción dos  7
numero_tres = int(sys.argv[3]) # opción tres 1

if ((numero_uno > numero_dos) and (numero_uno > numero_tres)):
    print(numero_uno)
elif ((numero_dos > numero_uno) and (numero_dos > numero_tres)):
    print(numero_dos)
else:
    print(numero_tres)
