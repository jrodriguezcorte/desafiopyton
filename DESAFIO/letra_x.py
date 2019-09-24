import sys
# funcion letra_x
# Entrada: n numero de dimension de letra "x"
# Salida: print funcion
def letra_x(n):
    n = int(n)
    resultado = ''

    contain_bounds = '*'
    for i in range(n - 2):
        contain_bounds += ' '
    contain_bounds += "*"

    contain_middle = ''
    rango = int(n/2)
    for j in range(rango):
        contain_middle += ' '
    contain_middle += '*\n'

    contain = ''
    rango = int(n/4)
    for j in range(rango):
        contain += ' '
    contain += '*'
    rango = int(n/4)
    for j in range(rango):
        contain += ' '
    contain += '*\n'

    resultado = contain_bounds+'\n'+(contain)+(contain_middle)+(contain)+contain_bounds

    return resultado


print(letra_x(5))
