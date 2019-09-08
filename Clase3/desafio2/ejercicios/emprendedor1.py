import sys

precio_venta = float(sys.argv[1]) # precio al que planea venderse el producto ($) dólares
usuarios = int(sys.argv[2]) # cantidad de usuarios a tener en el año
gastos = float(sys.argv[3]) # gastos al año ($) dólares

# fórmula de utilidades: (precio_venta*usuarios) - gastos
utilidades = (precio_venta*usuarios) - gastos

# si la utilidad es mayor a cero se multiplica por el 0.65
if utilidades > 0:
    utilidades = utilidades*0.65

# impresión de resultado final
print(utilidades)
