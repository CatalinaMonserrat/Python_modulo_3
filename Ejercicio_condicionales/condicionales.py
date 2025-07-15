# Comenzarmos con la definición de productos y precios 

productos = {"polera": 15.95,"blusa": 20.95,"abrigo": 70,"zapatillas": 75.95,"botas_largas": 99.99,"botines": 90.90,"sandalias": 55.95,"jeans": 29.99,"falda": 25.99,"pantalon": 30.99,"remera": 15.99,"camiseta": 20.99}

print("Productos disponibles:" ) #imprime los productos dispobubles y sus precios
for producto, precio in productos.items():
    print(f"{producto}: ${precio:.2f}")

lista_compra = [] #lista de compras vacia para guardar tuplas (producto, cantidad)
precio_total = 0

while True:
    producto = input("\n Ingrese el producto que desea comprar (o 'fin' para terminar): ").lower() #preguntamos al usuario que producto desea comprar
    if producto == "fin":
        break
    if producto in productos:   
        try:
            cantidad = int(input("Ingrese la cantidad deseada: "))
            if cantidad > 0:
                lista_compra.append((producto, cantidad))
                precio_total += productos[producto] * cantidad
            else:
                print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Ingrese una cantidad válida.")
    else:
        print("Producto no disponible.")

print("Productos comprados:") #imprime "productos comprados"
for producto, cantidad in lista_compra:
    subtotal = productos[producto] * cantidad
    print(f"- {producto} x{cantidad}: ${subtotal:.2f}") # imprime los productos por su cantidad y el subtotal (valor total por producto)

# Calculo del descuento por compras sobre 10 productos
total_productos = sum(cantidad for _, cantidad in lista_compra)
descuento_total = 0

if total_productos > 10:
    descuento_total += 10
    print("Aplicando descuento del 10% por comprar más de 10 productos.")

# Calculo cliente frecuente o no
cliente_frecuente = input("¿Tiene tarjte de cliente frecuente (sobre 05 compras)? (s/n): ").lower() == "s"

if cliente_frecuente:
    descuento_total += 5
    print("Aplicando descuento del 5% por ser cliente frecuente.")

# Calculo por compra sobre 500 dolares
if precio_total > 500:
    descuento_total += 7
    print("Aplicando descuento del 7% por comprar mas de $500.")

# Calculo Día de promoción (Lunes, Jueves y Sabado tiene 15% de descuento)
dia_promocion = input("¿Es lunes, jueves o sabado? (s/n): ").lower() == "s"

if dia_promocion:
    descuento_total += 15
    print("Aplicando descuento del 15% por ser lunes, jueves o sabado.")

# Calculo total descuento acumulado
if descuento_total > 30:
    descuento_total = 30

print(f"💰 Total sin descuento: ${precio_total:.2f}")

# Calculo total con descuento   

descuento_aplicado = descuento_total * precio_total / 100
precio_final = precio_total - descuento_aplicado

print(f"Total con descuento: ${precio_final:.2f}")