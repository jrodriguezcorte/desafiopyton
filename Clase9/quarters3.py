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

quarters = {}

longitud = len(ventas)
lista1 = []
lista2 = []
lista3 = []
lista4 = []

for clave, valor in ventas.items():
        if (clave== 'Enero' or clave== 'Febrero' or clave== 'Marzo'):
            lista1.append(valor)
        if (clave== 'Abril' or clave== 'Mayo' or clave== 'Junio'):
            lista2.append(valor)
        if (clave== 'Julio' or clave== 'Agosto' or clave== 'Septiembre'):
            lista3.append(valor)
        if (clave== 'Octubre' or clave== 'Noviembre' or clave== 'Diciembre'):
            lista4.append(valor)

quarters['Q1'] = lista1
quarters['Q2'] = lista2
quarters['Q3'] = lista3
quarters['Q4'] = lista4

print(quarters)
