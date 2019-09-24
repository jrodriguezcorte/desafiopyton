import sys, string

def gen(numero_letra):
    # obtener letras del alfabeto
    alfabeto = string.ascii_lowercase
    # creando una lista con los elementos del alfabeto
    list_alfabeto = list(alfabeto)
    # pasar mi parametro a intentos
    numero = int(numero_letra)
    concatenar = ''
    for i in range(numero):
        concatenar += list_alfabeto[i]
    print(concatenar)

# numero de la letra a mostrar
parametro = sys.argv[1]

gen(parametro)
