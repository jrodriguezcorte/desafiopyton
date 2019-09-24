from statistics import mean

def promedio(lista):
    return mean(lista)

auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

autos = []
autos = [auto1,auto2,auto3,auto4,auto5,auto6]

l1 = []
l2 = []
l3 = []


for i in range(0,len(autos)):
    l1.append(autos[i][1])
    l2.append(autos[i][2])
    l3.append(autos[i][4])

print(promedio(l1))
print(promedio(l2))
print(promedio(l3))
