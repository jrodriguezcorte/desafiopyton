# Entrada: n
# Salida: Imprime el rango de número de pares desde 0 hasta n (incluyendo n si es par)

# ingrese el valor de n
n = int(input("Ingrese un número para comenzar la cuenta\n"))

# inicializando variable de suma
suma = 0

for i in range(2,n+1,2):
    #print(str(i)+"\n")
    suma += i

print(suma)
