"""
# ingrese el valor de n
n = int(input("Ingrese un número para comenzar la cuenta\n"))
"""
# Entrada: n
# Salida: Imprime la suma de número de pares sin incluir el 0 hasta n (incluyendo n si es par)
import sys
# ingrese el valor de n
n = int(sys.argv[1])

# inicializando variable de suma
suma = 0

for i in range(2,n+1,2):
    #print(str(i)+"\n")
    suma += i

print(suma)
