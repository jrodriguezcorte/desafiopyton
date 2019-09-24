import sys
# funcion letra_o
# Entrada: n numero de dimension de letra "o"
# Salida: print funcion
def letra_i(n):
    n = int(n)
    resultado = ''
    contain_bounds = ''
    for i in range(n):
        contain_bounds += '*'
    contain_middle = ''
    # caso par
    if (n%2 == 0):
        rango = int(n/2)-1
        for j in range(rango):
            contain_middle += ' '
        contain_middle += '**'
        for j in range(rango):
            contain_middle += ' '
        contain_middle += '\n'
    # caso impar
    else:
        rango = int(n/2)
        for j in range(rango):
            contain_middle += ' '
        contain_middle += '*'
        for j in range(rango):
            contain_middle += ' '
        contain_middle += '\n'
    resultado = contain_bounds+'\n'+(contain_middle * (n - 2))+contain_bounds
    return resultado

# ingrese el valor de n
n = int(sys.argv[1])
print(letra_i(n))
