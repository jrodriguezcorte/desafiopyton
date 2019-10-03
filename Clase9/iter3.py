def filter(diccionario, valor_filtrar):
 nuevo_diccionario = {}
 for clave, valor in ventas.items():
    if valor > int(valor_filtrar):
        nuevo_diccionario[clave] = valor

 return nuevo_diccionario

filter(ventas,valor_filtrar)
