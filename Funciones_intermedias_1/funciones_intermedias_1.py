# Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]

matriz[1][2] = 6

print(matriz)

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”

cantantes[0]["nombre"] = "Enrique Martin Morales"

print(cantantes)

#En ciudades, cambia “Cancún” por “Monterrey”

ciudades["México"][2] = "Monterrey"

print(ciudades)

# En las coordenadas, cambia el valor de “latitud” por 9.9355431

coordenadas[0]["latitud"] = 9.9355431

print(coordenadas)

# Iterar a través de una lista de diccionarios Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. Por ejemplo:
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

#Imprime "nombre": "Ricky Martin", "pais": "Puerto Rico" (está bien si lo imprime en líneas separadas)

def iterarDiccionario(lista):
    for persona in lista:
        print(f"nombre: {persona['nombre']}, pais: {persona['pais']}")
        print ()

iterarDiccionario(cantantes)


#Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for persona in lista:
        print(persona[llave])

iterarDiccionario2("nombre", cantantes)
print()
iterarDiccionario2("pais", cantantes)
print()

#Iterar a través de un diccionario con valores de lista

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for clave in diccionario:
        print(f"{clave}: {len(diccionario[clave])}")
        print()
        for item in diccionario[clave]:
            print(item)

imprimirInformacion(costa_rica)