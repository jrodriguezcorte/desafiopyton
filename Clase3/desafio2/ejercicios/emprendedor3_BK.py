import sys

precio_venta = float(sys.argv[1]) # precio al que planea venderse el producto ($) dólares
usuarios_totales = int(sys.argv[2]) # cantidad de usuarios totales
gastos = float(sys.argv[3]) # gastos al año ($) dólares
# utilidades del año anterior
if len(sys.argv) < 5:
    utilidades_anterior = 1000
else:
    utilidades_anterior = float(sys.argv[4])

# calculo de utilidades año actual
utilidades_ano_actual = (precio_venta*usuarios_totales) - gastos

# si la utilidad es mayor a cero se multiplica por el 0.65
if utilidades_ano_actual > 0:
    utilidades_ano_actual = utilidades_ano_actual*0.65

# porcentaje de la razón entre las utilidades actuales y las del año anterior.
razon_porcentaje_utilidades =  (utilidades_ano_actual/utilidades_anterior)*100

# impresión de resultado final de la razón de utilidades en %
print("{}%".format(razon_porcentaje_utilidades))
# utilidades
print(utilidades_ano_actual)
