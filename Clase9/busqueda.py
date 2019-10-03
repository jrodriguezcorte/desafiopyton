import sys

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

cantidad_parametros = len(sys.argv)


for i in range (1,cantidad_parametros):
    valor_parametro = sys.argv[i]
    no_existe = True
    for clave, valor in ventas.items():
        if valor == int(valor_parametro):
            print(clave)
            no_existe = False
    if (no_existe):
        print('no encontrado')
