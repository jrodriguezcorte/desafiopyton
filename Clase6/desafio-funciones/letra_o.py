import sys
# funcion letra_o
# Entrada: n numero de dimension de letra "o"
# Salida: print funcion
def letra_o(n):
    n = int(n)
    resultado = ''
    contain_bounds = ''
    for i in range(n):
        contain_bounds += '*'
    contain_middle = "*"
    for j in range(n - 2):
        contain_middle += " "
    contain_middle += "*\n"

    resultado = contain_bounds+'\n'+(contain_middle * (n - 2))+contain_bounds
    return resultado

# ingrese el valor de n
n = int(sys.argv[1])
print(letra_o(n))
