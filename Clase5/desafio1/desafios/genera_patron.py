"""
# ingrese el valor de n
n = int(input("Ingrese un número para comenzar la cuenta\n"))
"""
# Entrada: n que representa el número de filas que se debe generar
# Salida: Imprime el patron

import sys

# ingrese el valor de n
n = int(sys.argv[1])
acumulador = ''

for i in range(n):
    for j in range(i+1):
        acumulador += str(j+1)
        if ((j == i) and (i+1 != n)):
           acumulador += '\n'

print(acumulador)
