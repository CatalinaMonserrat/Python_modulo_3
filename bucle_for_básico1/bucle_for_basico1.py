#imprimir numeros 0 al 100
for i in range(100+1):
    print(i)


#imprime todos los números múltiplos de 2 entre 2 y 500
for i in range(2,500+1,2):
    print(i)

# imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”

for i in range(1,100+1):
    if i % 5 == 0 and i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).

suma = 0
for i in range(0,500000+1,2):
    suma += i
print(suma)

# imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
for i in range(2024,-1,-3):
    print(i)

#establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

numInicial = 3
numFinal = 10
multiplo = 2
for i in range(numInicial,numFinal+1):
    if i % multiplo == 0:
        print(i)
        