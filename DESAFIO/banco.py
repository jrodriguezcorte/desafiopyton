import sys

def depositar(saldo, cantidad):
    saldo = saldo + cantidad
    return saldo

def girar(saldo, cantidad):
    if (saldo < cantidad):
       return False
    else:
       saldo = saldo - cantidad
       return saldo

def mostrar_menu(saldo = 0):
    print('Bienvenido al Banco Amigo. Escoja una opción:')
    print('1. Consultar saldo')
    print('2. Hacer depósito')
    print('3. Realizar giro')
    print('4. Salir')
    print()

if len(sys.argv) < 2:
    saldo = 0
else:
    saldo = int(sys.argv[1])

saldo_cliente = saldo
mostrar_menu(saldo)
opt_menu = int(input())
while opt_menu != 4:
    if opt_menu == 1:
        print("Su saldo es de {}\n".format(saldo))
        print()
        mostrar_menu(saldo) # Se llama a la función
        opt_menu = int(input())
    elif opt_menu == 2:
        cantidad = int(input("Ingrese la cantidad a depositar \n"))
        saldo = depositar(saldo, cantidad)
        saldo_cliente = saldo
        print("Su saldo es de {}\n".format(saldo))
        print()
        mostrar_menu(saldo) # Se llama a la función
        opt_menu = int(input())
    elif opt_menu == 3:
        if (saldo > 0):
            cantidad = int(input("Ingrese la cantidad a girar \n"))
            giro = girar(saldo, cantidad)
            if (giro is False):
                saldo = saldo_cliente
                print("No se puede girar esta cantidad. Su saldo es de {}\n".format(saldo))
            else:
                saldo = giro
                saldo_cliente = saldo
                print("Su saldo es de {}\n".format(saldo))
                print()
                mostrar_menu(saldo) # Se llama a la función
                opt_menu = int(input())
    elif opt_menu == 4:
                print('Saliendo')
    else:
                print("Opción inválida. Por favor ingrese 1, 2, 3 ó 4.")
                mostrar_menu(saldo) # Se llama a la función
                opt_menu = int(input())
