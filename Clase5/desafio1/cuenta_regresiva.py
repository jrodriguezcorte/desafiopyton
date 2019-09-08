"""
# Código mediante el uso de for
cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
for i in range(cuenta_regresiva):
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))
"""

# Código mediante el uso de while
# Entrada: cuenta_regresiva = número para imprimir la cuenta regresiva
# Salida: Imprime el valor de cada iteracion, partiendo del valor de entrada

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta\n"))
i = 0

while (i < cuenta_regresiva):
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))
    i += 1
