# Entrada: n que representa el número de parrafos que se debe generar
# Salida: Imprime los parrafos deseados

import sys

# parrafo lorem ipsum
parrafo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a commodo enim. Etiam tincidunt nibh sagittis sapien malesuada, nec aliquam turpis gravida. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam non arcu malesuada elit vehicula porta. Aliquam ante ligula, fermentum nec odio in, placerat facilisis elit. Vivamus sit amet est convallis, scelerisque urna sed, dignissim nibh. Integer eget ultricies velit, vitae pellentesque metus."

# ingrese el valor de n
n = int(sys.argv[1])

# variable acumuladora
acumulador = ''
for i in range(n):
    acumulador += parrafo
    if (i+1 != n):
        acumulador += '\n\n'

print(acumulador)
