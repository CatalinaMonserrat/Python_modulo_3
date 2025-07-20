# Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
def actualizar_matriz(matriz, fila, columna, nuevo_valor):
    matriz[fila][columna] = nuevo_valor
    return matriz

resultado = actualizar_matriz(matriz, 1, 0, 6)

print(matriz)
print ()

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”

def actualizar_cantantes(cantantes, nombre, nuevo_nombre):
    cantantes[0][nombre] = nuevo_nombre
    return cantantes

cantantes = actualizar_cantantes(cantantes, "nombre", "Enrique Martin Morales")
print(cantantes)
print ()


#En ciudades, cambia “Cancún” por “Monterrey”
ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

def actualizar_ciudades(ciudades, pais, ciudad, nueva_ciudad):
    ciudades[pais][ciudad] = nueva_ciudad
    return ciudades
ciudades = actualizar_ciudades(ciudades, "México", 2, "Monterrey")

print(ciudades)
print ()

# En las coordenadas, cambia el valor de “latitud” por 9.9355431

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]
def actualizar_coordenadas(coordenadas, latitud, nueva_latitud):
    coordenadas[0][latitud] = nueva_latitud
    return coordenadas

coordenadas = actualizar_coordenadas(coordenadas, "latitud", 9.9355431)

print(coordenadas)
print ()

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