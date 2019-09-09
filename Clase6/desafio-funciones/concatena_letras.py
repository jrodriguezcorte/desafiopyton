import string

# creación de la función gen
def gen(n):
    # pasar valor a int
    n = int(n)
    # obtener letras del alfabeto
    alfabeto = string.ascii_lowercase
    # creando una lista con los elementos del alfabeto
    list_alfabeto = list(alfabeto)
    resultado = ''
    for i in range(n):
        resultado += list_alfabeto[i]

    return resultado

# ingrese la contraseña
cantidad_letras = input("Ingresa la cantidad de letras\n")
# llamado a la funcion
resultado = gen(cantidad_letras)
# imprimiendo resultado
print(resultado)
