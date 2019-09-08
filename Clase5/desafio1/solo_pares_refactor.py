"""
# ingrese el valor de n
n = int(input("Ingrese un número para comenzar la cuenta\n"))
"""
# Entrada: n
# Salida: Imprime el rango de número de pares sin incluir el 0 hasta n (incluyendo n si es par)

import sys

# ingrese el valor de n
n = int(sys.argv[1])

# inicializando variable
i = 0
while (i <= n):
    if (i%2 == 0) and (i != 0):
       print(i)
    i+=1
