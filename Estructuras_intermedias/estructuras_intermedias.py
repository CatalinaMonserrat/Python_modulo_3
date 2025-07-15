#Cambio valor 3 en matriz por 6.

matriz = [ [10, 15, 20], [3, 7, 14] ]

matriz[1][0]=6
print(matriz)

#Cambia el nombre del primer cantante por "Enrique Martin Morales".
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

print(cantantes)

#En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".
ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"

print(ciudades)

#En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

coordenadas[0]["latitud"]=9.9355431

print(coordenadas)

#Recorrer una lista de diccionarios:  Utiliza estructuras de control para iterar la lista cantantes. Muestra el nombre y país de cada cantante.
# BONUS: Presenta cada entrada con el siguiente formato: nombre - [Nombre del cantante], pais - [País]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

for i, cantante in enumerate(cantantes):
   print(f"{i}. nombre - {cantante['nombre']}, pais - {cantante['pais']}")

#Obtener valores específicos desde una lista de diccionarios:  Utilizando la lista cantantes, imprime por separado todos los valores correspondientes a la clave "nombre".Luego, imprime todos los valores correspondientes a la clave "pais".

print([cantante['nombre'] for cantante in cantantes])
print([cantante['pais'] for cantante in cantantes])

#Recorrer un diccionario con listas como valores:  Dado el siguiente diccionario:
#Realiza un recorrido del diccionario que imprima lo siguiente: 
#La cantidad de elementos en cada lista seguida del nombre de la clave en mayúsculas.
#Cada elemento de la lista correspondiente, en líneas separadas.
costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for clave, valor in costa_rica.items():
   print(f"{len(valor)} {clave.upper()}")
   for elemento in valor:
      print(elemento)
