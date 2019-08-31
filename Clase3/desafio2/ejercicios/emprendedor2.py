import sys

precio_venta = float(sys.argv[1]) # precio al que planea venderse el producto ($) dólares
usuarios_totales = int(sys.argv[2]) # cantidad de usuarios totales
cantidad_usuarios_premium = int(sys.argv[3]) # cantidad de usuarios premium (pagan el doble)
cantidad_usuarios_gratuitos = int(sys.argv[4]) # cantidad de usuarios gratuitos  (no pagan nada)
gastos = float(sys.argv[5]) # gastos al año ($) dólares

# calculo de utilidades para usuarios premium
utilidades_premium = (2*precio_venta*cantidad_usuarios_premium)

# cantidad de usuarios regulares
cantidad_usuarios_regulares =  usuarios_totales - cantidad_usuarios_premium - cantidad_usuarios_gratuitos

# calculo de utilidades para usuarios regulares
utilidades_regulares = (precio_venta*cantidad_usuarios_regulares)

# fórmula de utilidades: (precio_venta*usuarios) - gastos
utilidades = (utilidades_premium + utilidades_regulares) - gastos

# impresión de resultado final
print("Las utilidades para el caso son de {}$".format(utilidades))
