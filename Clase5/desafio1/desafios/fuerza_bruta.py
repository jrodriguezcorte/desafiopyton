import string

# ingrese la contraseña
password = input("Ingresa contraseña\n")
# se considera mayúsculas y minúsculas como una misma letra.
password =  password.lower()
# longitud de palabra
longitud_password = len(password)
# separando la palabra en una lista
list_password = list(password)
# obtener letras del alfabeto
alfabeto = string.ascii_lowercase
# longitud de letras alfabeto
longitud_alfabeto = len(alfabeto)
# creando una lista con los elementos del alfabeto
list_alfabeto = list(alfabeto)

intentos = 0
for i in range(longitud_password):
    for j in range(longitud_alfabeto):
        intentos += 1
        if (list_password[i] == list_alfabeto[j]):
            break

print("{} intentos".format(intentos))
