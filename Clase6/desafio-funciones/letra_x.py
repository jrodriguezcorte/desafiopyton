import sys
# funcion letra_o
# Entrada: n numero de dimension de letra "o"
# Salida: print funcion
def letra_x(n):
    n = int(n)
    resultado = ''

    contain_bounds = '*'
    for i in range(n - 2):
        contain_bounds += ' '
    contain_bounds += "*"

    contain_center = ''
    contain = ''

    # caso par
    if (n%2 == 0):
        rango = int(n/2)-1
        for j in range(rango):
            contain_center += ' '
        contain_center += '**'
        for j in range(rango):
            contain_center += ' '
        contain_center += '\n'

    # caso impar
    else:
        for j in range(n):
            if (j%2 != 0) and ((j == 1) or (j == n-2)):
                contain += "*"
            else:
                contain += " "
        contain += '\n'
        rango = int(n/2)
        for j in range(rango):
            contain_center += ' '
        contain_center += '*'
        for j in range(rango):
            contain_center += ' '
        contain_center += '\n'

    resultado = contain_bounds+'\n'+(contain)+(contain_center)+(contain)+contain_bounds

    return resultado

# ingrese el valor de n
n = int(sys.argv[1])
print(letra_x(n))
