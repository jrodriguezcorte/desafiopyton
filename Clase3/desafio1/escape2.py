import sys
import math

g = sys.argv[1] # gravedad del planeta
r = sys.argv[2] # radio del planeta en kms

print(g)
print(r)

# pase de radio de kms a m y a float
r = float(r)*1000
# pase de gravedad a float
g = float(g)

# calculo de velocidad
velocidad = math.sqrt(2*g*r)

print(velocidad)

# impresión de resultado final
print("La velocidad de escape es de {} m/s".format(velocidad))
