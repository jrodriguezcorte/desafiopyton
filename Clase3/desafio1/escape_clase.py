import sys
import math

g = float(sys.argv[1]) # gravedad del planeta
r = int(sys.argv[2]) # radio del planeta en kms

# velocidad de escpa del planeta
velocidad_escape = math.sqrt(2*(g*10**3)*r)

# impresión de resultado final
print("La velocidad de escape del planeta es de {} m/s".format(velocidad_escape))
