# Entrada: n
# Salida: Imprime el rango de número de pares desde 0 hasta n (incluyendo n si es par)

# ingrese el valor de n
n = int(input("Ingrese un número para comenzar la cuenta\n"))

# inicializando variable
i = 0
while (i <= n):
    if (i%2 == 0) and (i != 0):
       print(i)
    i+=1
