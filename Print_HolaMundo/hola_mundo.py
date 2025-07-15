# 1. Imprime "Hola, mundo"

print( "Hola, mundo" )

# 2. Imprime "Hola, Valeria" con el nombre en una variable

nombre = "Catalina"

print( "Hola,", nombre ) # con una coma

print( "Hola, " + nombre + "!" ) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable

numero = 193

print( "Hola", numero ) # con una coma

print( "Hola " + str( numero ) + "!" ) # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables

comida1 = "completos"

comida2 = "sushi"

print("Me encanta comer {} y {}".format(comida1, comida2)) # con .format()

print(f"Me encanta comer {comida1}  y  {comida2}" ) # con una cadena f

# BONUS NINJA: Otros métodos de cadena

# upper(): convienrte a mayúsculas

print(nombre.upper())

nombre = "CATALINA"
# lower(): convierte a minúsculas

print( nombre.lower() )

# title(): convierte la primera letra de cada palabra a mayúscula

frase = "me encanta salir a correr"

print( frase.title() )

#count(): cuantas veces aparece una letra en una cadena

frase = "me encanta salir a correr"

print( frase.count("a") )

# replace(): reemplaza una letra por otra

frase = "me encanta salir a correr"

print( frase.replace("a", "e") )