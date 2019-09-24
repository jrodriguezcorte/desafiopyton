def promedio(lista):
    promedio_acum = 0
    count = 0
    for i in range(0,len(lista)):
        for j in range(0,len(lista[i])):
            if type(lista[i][j]) is float :
                count += 1
                promedio_acum += lista[i][j]
            else:
                pass
    promedio_acum = promedio_acum/count
    return promedio_acum

auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

autos = []
autos = [auto1,auto2,auto3,auto4,auto5,auto6]

promedio_acum = promedio(autos)

lista_de_flotantes = []

for i in range(0,len(autos)):
    lista_de_flotantes.append(autos[i][1])

resultado = list(filter(lambda i: i > promedio_acum, lista_de_flotantes))
print(resultado)
