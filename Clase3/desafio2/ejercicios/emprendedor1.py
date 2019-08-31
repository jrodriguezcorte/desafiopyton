import sys

precio_venta = float(sys.argv[1]) # precio al que planea venderse el producto ($) dólares
usuarios = int(sys.argv[2]) # cantidad de usuarios a tener en el año
gastos = float(sys.argv[3]) # gastos al año ($) dólares

# fórmula de utilidades: (precio_venta*usuarios) - gastos
utilidades = (precio_venta*usuarios) - gastos

# impresión de resultado final
print("Las utilidades para el caso son de {}$".format(utilidades))
