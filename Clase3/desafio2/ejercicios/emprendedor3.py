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

# porcentaje de la razón entre las utilidades actuales y las del año anterior.
razon_porcentaje_utilidades =  (utilidades_ano_actual/utilidades_anterior)*100

# redondeo de decimales
razon_porcentaje_utilidades = round(razon_porcentaje_utilidades, 2)

# impresión de resultado final
print("El porcentaje de la razón entre las utilidades actuales y las del año anterior es de {}%".format(razon_porcentaje_utilidades))
