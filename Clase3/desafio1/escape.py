import sys, math

g = float(sys.argv[1]) # gravedad del planeta (mts/seg**2)
r = float(sys.argv[2]) # radio del planeta en (kms)

# paso del radio del planeta a (ms)
r = r*10**3

# velocidad de escpa del planeta
velocidad_escape = math.sqrt(2*g*r)

# impresión de resultado final
print("La velocidad de escape es de {} m/s".format(velocidad_escape))
