# Entrada: n
# Salida: Imprime el rango de número de pares desde 0 hasta n (incluyendo n si es par)

# ingrese el valor de n
n = int(input("Ingrese un número para comenzar la cuenta\n"))
acumulador = ''
"""
for i in range(n):
    for j in range(i+1):
        acumulador += str(j+1)
        if ((j == i) and (i+1 != n)):
           acumulador += '\n'

print(acumulador)
"""

"""
for i in range(1,n+1):
    for j in range(1,i+1):
        acumulador += str(j)
        if ((j == i) ):
           acumulador += '\n'

print(acumulador)
"""
concatenar = ''
for i in range(1,n+1):
    concatenar += str(i)
    print(concatenar)
